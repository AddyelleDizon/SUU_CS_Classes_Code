import numpy as np

### Compute the eigenvalues and eigenvectors of the matrices. ###
### EXERCISE 1 ###
A = np.array([[1,1],
              [1,1]])
eigenvalsA = np.linalg.eigvals(A)
eigenvecsA = np.linalg.eigvalsh(A)
# Find the eigenvalues (eigenvalsA) and eigenvectors (eigenvecsA) of A              
print(f"A : Eigenvalues = {eigenvalsA}\n Eigenvectors =\n {eigenvecsA}")
## solution:
#A : Eigenvalues = [2. 0.]
# Eigenvectors =
# [[ 0.70710678 -0.70710678]
# [ 0.70710678  0.70710678]]

### EXERCISE 2 ###
B = np.array([[1,0,-1],
              [0,1,-1],
              [1,-1,0]])
eigenvalsB = np.linalg.eigvals(B)
eigenvecsB = np.linalg.eigvalsh(B)
# Find the eigenvalues (eigenvalsB) and eigenvectors (eigenvecsB) of B
print(f"B : Eigenvalues = {eigenvalsB}\n Eigenvectors =\n {eigenvecsB}") 
## solution:
#B : Eigenvalues = [-1.  1.  2.]
# Eigenvectors =
# [[ 4.08248290e-01 -7.07106781e-01  5.77350269e-01]
# [ 4.08248290e-01  7.07106781e-01  5.77350269e-01]
# [ 8.16496581e-01  7.88210995e-17 -5.77350269e-01]]

### EXERCISE 3 ###
C = np.array([[1,0,1],
              [0,-1,1],
              [1,1,0]])
eigenvalsC = np.linalg.eigvals(C)
eigenvecsC = np.linalg.eigvalsh(C)
# Find the eigenvalues (eigenvalsC) and eigenvectors (eigenvecsC) of C                          
print(f"C : Eigenvalues = {eigenvalsC}\n Eigenvectors =\n {eigenvecsC}")
## solution:
#C : Eigenvalues = [ 1.73205081e+00 -2.86646153e-17 -1.73205081e+00]
# Eigenvectors =
# [[ 0.78867513  0.57735027 -0.21132487]
# [ 0.21132487 -0.57735027 -0.78867513]
# [ 0.57735027 -0.57735027  0.57735027]]
