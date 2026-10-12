import numpy as np
import matplotlib.pyplot as plt

### EXERCISE 1 ##########################
# interpolate the function f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 + a_5x^5 through the given points.
points = np.array([[-2,231],[-1,19],[0,5],[1,9],[2,19],[3,-169]])
x = points[:,0]
y = points[:,1]

#construct your model here. You may need to construct the matrix A in the line above.
V = np.vander(x, increasing=True)
f = np.linalg.solve(V,y)
print(np.poly1d(f))

### VERIFICATION 1 ############################
plt.ion()
t = np.linspace(-3,4,num = 100)
plt.axis([-3,4,-200,300])
plt.scatter(x,y)
plt.plot(t, np.poly1d(f)(t), 'r')
plt.show()

### EXERCISE 2 ##########################
# interpolate the function f(x) = (a_0 + a_1x + a_2x^2) / (1 + b_1x + b_2x^2) through the given points.
points = np.array([[-2,12/11],[-1,3/2],[0,2],[1,0],[2,0]])
x = points[:,0]
y = points[:,1]

#construct your model here. You may need to construct the matrix A in the line above.
A = np.column_stack([np.ones_like(x), x, x**2, -y*x, -y*x**2])

f = np.linalg.solve(A, y)
n = 2                       

numer = f[:n+1]
denom = np.concatenate((f[n+1:], [1]))
print(np.poly1d(numer), "/\n", np.poly1d(denom))

### VERIFICATION 2 ############################
plt.axis([-3,4,-10,10])
plt.scatter(x,y)
plt.plot(t, np.polyval(numer,t) / np.polyval(denom,t), 'r')
plt.show()
