import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')#replace with 'seaborn-whitegrid' if error occurs

dilate = lambda a, b: np.array([[a, 0], [0, b]])

rotate = lambda theta: np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

reflect = lambda theta: np.array([[np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), -np.cos(2*theta)]])

project = lambda theta: 1/2*np.array([[1+np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), 1-np.cos(2*theta)]])

#create a scatter plot for "J"
points = np.concatenate([[[1+(0.1+0.01*i),1] for i in range(81)], 
                       [[1+0.5, 1-0.01*j] for j in range(76)],
                       [[1+0.25+0.25*np.cos(np.pi*(1+0.01*k)), 0.25+0.25*np.sin(np.pi*(1+0.01*k))] for k in range(101)]]) #np.concatenate([[[i*0.01,j*0.01] for i in range(101)] for j in range(101)])

plt.figure(figsize=(8, 8), dpi=80)
plt.axis([-9,3,-7,7])

#Transform the set of points
# J1   
Q11 = rotate(np.pi/3)
Q12 = reflect(np.pi/2)
Q13 = Q11 @ Q12
b1 = np.array([0, 0])
J_1 = (Q13 @ points.T).T + b1
plt.scatter([c[0] for c in J_1], [c[1] for c in J_1])

# J2
Q21 = rotate(np.pi/3)
Q22 = reflect(np.pi/2)
Q23 = Q21 @ Q22
b2 = np.array([-5, 3])
J_2 = (Q23 @ points.T).T + b2
plt.scatter([c[0] for c in J_2], [c[1] for c in J_2])

# J3
Q31 = rotate(np.pi/3)
b3 = np.array([-2.6, 1.5])
J_3 = (Q31 @ points.T).T + b3
plt.scatter([c[0] for c in J_3], [c[1] for c in J_3])

#Show the sets of points
plt.scatter([c[0] for c in points], [c[1] for c in points])

t = np.linspace(-10, 10, 100)
plt.plot(t, t*np.tan(5*np.pi/6), "-.r")
plt.show()
