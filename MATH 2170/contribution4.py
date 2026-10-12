import random            
import numpy as np       
import matplotlib.pyplot as plt 

# Firstly, this function generates 20 random integer x-values between 0 and 10
X = [random.randint(0, 10) for i in range(20)]

# Then, we generate corresponding y-values using y = 2.5*x + 1 with some random integers
y = [2.5*x + 1 + random.randint(-2, 2) for x in X]

# Then, we create the design matrix for least squares
# Each row: [x_i, 1] (1 is for the intercept term)
X_matrix = np.column_stack((X, np.ones(len(X))))

# After, we solve the least squares problem: use the np.linalg.lstsq function
m, b = np.linalg.lstsq(X_matrix, y, rcond=None)[0]

# Create a smooth range of x-values for plotting the fitted line
x_line = np.linspace(min(X), max(X), 100)

# Plot the original data points as blue dots
plt.scatter(X, y, color='blue', label='Data points')

# Plot the fitted least squares line in red
plt.plot(x_line, m*x_line + b, color='red', label=f'Fitted line: y = {m:.2f}x + {b:.2f}')

# Display the points and the line in MatPlotLib
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit Example')
plt.legend()
plt.grid(True)
plt.show()

# This is added since during the beginning of the fourth chapter, 
# I had trouble trying to use the MatPlotLib properly
# and trying to graph certain things.
# I believe that this can go right after example 4.1.8, as a sort of graphic.