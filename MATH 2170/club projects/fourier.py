import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

plt.axis([-10,10,-3,3])
x = np.linspace(-10, 10, 1000)

f = np.piecewise(x, [((-4*np.pi <= x) & (x < -3*np.pi)),  
                     ((-3*np.pi <= x) & (x < -2*np.pi)),
                     ((-2*np.pi <= x) & (x < -1*np.pi)), 
                     ((-1*np.pi <= x) & (x < 0)), 
                     ((0 <= x) & (x < np.pi)),
                     ((np.pi <= x) & (x < 2*np.pi)),
                     ((2*np.pi <= x) & (x < 3*np.pi))], 
                 [1,0,1,0,1,0,1])
plt.plot(x,f)

#create and solve your linear system here. You will need a coefficient matrix A and an augmented column b
#Recall that np.sin(x) gives the sine function in Python, where the angle is measured in radians.

# Task 1
n = 25
x_1 = np.array([j * np.pi / 12 for j in range(1, 13)])
y_1 = np.ones_like(x_1)

x_0 = np.array([np.pi + j * np.pi/13 for j in range(1, 14)])
y_0 = np.zeros_like(x_0)

x_p = np.concatenate((x_1, x_0))
y_p = np.concatenate((y_1, y_0))

# I had help from a tutor from this point on. I got lost since it was very wrong what I wrote.
A = np.array([[np.sin((2 * j + 1) * i) for j in range(n)] for i in x_p])
b = y_p - 0.5

c = np.linalg.solve(A,b)

# Task 2:
#plt.plot(x, 1/2 + sum([c[j]*np.sin((2 * j + 1) * x) for j in range(25)]))
g = 0.5 + sum([c[j] * np.sin((2 * j + 1) * x) for j in range(n)]) 
g = (g - np.min(g)) / (np.max(g) - np.min(g))

plt.plot(x, g)
plt.show()
