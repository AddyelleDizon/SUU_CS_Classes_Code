import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

def square_wave(x):
    k = np.floor(x / np.pi).astype(int)
    return (k % 2 == 0).astype(float) 

rng = np.random.default_rng(0)
x_pts = rng.uniform(-10, 10, 100)
y_pts = square_wave(x_pts)

n = 25 
m = len(x_pts)

A = np.empty((m, n))
for j in range(n):
    A[:, j] = np.sin((2*j + 1) * x_pts)

b = y_pts - 0.5

c, *_ = np.linalg.lstsq(A, b, rcond=None)

x_dense = np.linspace(-10, 10, 4000)
f_dense = square_wave(x_dense)
A_dense = np.empty((len(x_dense), n))
for j in range(n):
    A_dense[:, j] = np.sin((2*j + 1) * x_dense)

g_dense = 0.5 + A_dense.dot(c)

plt.figure(figsize=(12,5))
plt.plot(x_dense, f_dense, linewidth=1.5)
plt.plot(x_dense, g_dense, linewidth=2)
plt.scatter(x_pts, y_pts, s=25, color='k', zorder=4)

plt.xlim(-10, 10)
plt.ylim(-0.5, 1.5)
plt.legend()
plt.show()