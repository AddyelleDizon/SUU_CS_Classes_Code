import numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    A = coefficient_matrix.astype(float)
    A[i] = scalar*coefficient_matrix[i]
    b = augmented_matrix.astype(float)
    b[i] = scalar*augmented_matrix[i]    
    
    return A,b

def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    A = coefficient_matrix.astype(float)
    A[i] = coefficient_matrix[i] + scalar*coefficient_matrix[j]
    b = augmented_matrix.astype(float)
    b[i] = augmented_matrix[i] + scalar*augmented_matrix[j]    
    
    return A,b

def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    idx = np.arange(len(coefficient_matrix))
    idx[i] = j
    idx[j] = i  
    
    return coefficient_matrix[idx],augmented_matrix[idx]

def zero_below(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    if abs(A[pivot]) < 1e-6:
        for k in range(pivot[0],len(A)):
            if abs(A[k,pivot[1]]) > 1e-6:
                A,b = row_interchange(A,b,k,pivot[0])
                break
    for k in range(pivot[0]+1, len(A)): 
        A,b = row_replacement(A,b,-A[k,pivot[1]]/A[pivot],k,pivot[0])
    return A,b

def zero_above(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    A,b = row_scaling(A,b,1/A[pivot],pivot[0])
    for k in range(pivot[0]): 
        A,b = row_replacement(A,b,-A[k,pivot[1]],k,pivot[0])
    return A,b

def forward_phase(coefficient_matrix, constant_matrix):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    pivots = []
    if np.linalg.norm(A) < 1e-6: #checks for zero matrix
        return A,b,pivots
    i = 0
    for j in range(i,A.shape[1]):
        if np.linalg.norm(A[i:,j]) < 1e-6: #checks for zero column
            continue
        else:
            A,b = zero_below(A,b,(i,j))
            pivots.append((i,j))
            i += 1      
    return A,b,pivots

def backward_phase(coefficient_matrix, constant_matrix, pivots):
    reduced_coefficient_matrix = coefficient_matrix.copy().astype(float)
    reduced_constant_matrix = constant_matrix.copy().astype(float)

    for pivot in reversed(pivots):
        i, j = pivot  

        pivot_val = reduced_coefficient_matrix[i, j]
        if pivot_val != 0:
            reduced_coefficient_matrix[i] = reduced_coefficient_matrix[i] / pivot_val
            reduced_constant_matrix[i] = reduced_constant_matrix[i] / pivot_val

        reduced_coefficient_matrix, reduced_constant_matrix = zero_above(reduced_coefficient_matrix, reduced_constant_matrix, pivot)

    return reduced_coefficient_matrix, reduced_constant_matrix

def Null(matrix):
    #write your code here
    #returns null, that is, returns a basis for the null space of matrix
    A = matrix.astype(float)
    m, n = A.shape
    b = np.zeros((m,1))

    A_forward, b_forward, pivots = forward_phase(A, b)
    R, b_rref = backward_phase(A_forward, b_forward, pivots)

    pivot_cols = {j for (i,j) in pivots}
    free_cols = [j for j in range(n) if j not in pivot_cols]

    if len(pivots) == 0:
        return np.eye(n)

    basis = []

    for i in free_cols:
        vec = np.zeros(n)
        vec[i] = 1

        for (i,j) in pivots:
            s = 0
            for k in free_cols:
                s += R[i,k] * vec[k]
            vec[j] = -s

        basis.append(vec)

    return np.array(basis).T

   
### VERIFY ############################
A = np.array([[6,5,4,3,2,1],
              [5,4,3,2,1,6],
              [2,4,6,8,2,4],
              [0,1,0,1,2,6]])
print(np.round(Null(A),12))
print(Null(np.zeros((4,5))),"\n")
