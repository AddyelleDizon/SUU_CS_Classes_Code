import numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    scaled_coefficient_matrix = coefficient_matrix.copy()
    scaled_constant_matrix = augmented_matrix.copy()

    scaled_coefficient_matrix[i] *= scalar
    scaled_constant_matrix[i] *= scalar

    return scaled_coefficient_matrix, scaled_constant_matrix

def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    replaced_coefficient_matrix = coefficient_matrix.copy()
    replaced_constant_matrix = augmented_matrix.copy()

    replaced_coefficient_matrix[i] = replaced_coefficient_matrix[i] + scalar * replaced_coefficient_matrix[j]
    replaced_constant_matrix[i] = replaced_constant_matrix[i] + scalar * replaced_constant_matrix[j]

    return replaced_coefficient_matrix, replaced_constant_matrix

def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    interchanged_coefficient_matrix = coefficient_matrix.copy()
    interchanged_constant_matrix = augmented_matrix.copy()

    interchanged_coefficient_matrix[[i, j]] = interchanged_coefficient_matrix[[j, i]]
    interchanged_constant_matrix[[i, j]] = interchanged_constant_matrix[[j, i]]

    return interchanged_coefficient_matrix, interchanged_constant_matrix

def zero_below(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.copy().astype(float)
    b = constant_matrix.copy().astype(float)
    i, j = pivot
    m, n = A.shape

    if abs(A[i, j]) < 1e-6:
        for k in range(i + 1, m):
            if abs(A[k, j]) >= 1e-6:
                A, b = row_interchange(A, b, i, k)
                break
        else:
            return A, b

    for k in range(i + 1, m):
        if abs(A[k, j]) >= 1e-6:
            factor = -A[k, j] / A[i, j]
            A, b = row_replacement(A, b, factor, k, i)

    return A, b

def zero_above(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.copy().astype(float)
    b = constant_matrix.copy().astype(float)
    i, j = pivot
    m, n = A.shape

    if abs(A[i, j]) < 1e-12:
        for k in range(i - 1, -1, -1):
            if abs(A[k, j]) >= 1e-12:
                A, b = row_interchange(A, b, i, k)
                break
        else:
            return A, b

    pivot_val = A[i, j]
    A[i] = A[i] / pivot_val
    b[i] = b[i] / pivot_val

    for k in range(i - 1, -1, -1):
        if abs(A[k, j]) >= 1e-12:
            factor = -A[k, j]
            A, b = row_replacement(A, b, factor, k, i)

    return A, b

### VERIFICATION ############################
aug_matrix = lambda A,B : np.array([np.concatenate((A[i],B.reshape(len(A),-1)[i])) for i in range(len(A))])

A = np.array([[0,2,3],[5,6,7], [9,10,11]])
b = np.array([4, 8, 12])
Ab = aug_matrix(A, b)
print(Ab, "\n")

#row reduce below using (1,1) pivot
A, b = zero_below(A,b,(0,0))
print(aug_matrix(A, b), "\n")

#row reduce below using (3,3) pivot
A, b = zero_above(A, b,(2,2))
print(aug_matrix(A, b))
