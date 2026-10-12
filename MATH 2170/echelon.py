import numpy as np

### EXERCISE 1#############################
#Solve the linear system [A|b]
A = np.array([[6, 5, 0], [4, 0, 3], [0, 2, 1]])
b = np.array([13, 5, 5])

solution = np.linalg.solve(A, b)

print(solution) #compute the solution here
#solution = [0.5 2.  1. ]
