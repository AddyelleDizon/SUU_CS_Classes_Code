import numpy as np


### Task 1 ################
print("~Task 1~")
A = np.array([
    [0, 1, 0, 0, 1, 1], # A connects to B, E, F
    [1, 0, 1, 1, 0, 1], # B connects to A, C, D, F
    [0, 1, 0, 1, 1, 0], # C connects to B, D, E
    [0, 1, 1, 0, 1, 0], # D connects to B, C, E
    [1, 0, 1, 1, 0, 1], # E connects to A, C, D, F
    [1, 1, 0, 0, 1, 0] # F connects to A, B, E
])
#Let A denote the adjacency matrix for this graph Γ
print(f"Adjacency Matrix\n {A}\n")

### Task 2 ###############################
print("~Task 2~")
k=100
T = A / A.sum(axis=1, keepdims=True)
#The transition matrix T will be time-invariant and can be considered a modification of the adjacency matrix A for Γ
print(f"Transition Matrix\n {T}\n")
print() #What is the relationship between these two matrices?

print("Starting at vertex A")
X = np.zeros((k+1,6))
X0 = np.array([1,0,0,0,0,0])

def random_walk(T, x0, t):
    xt = x0.copy()
    for i in range(t):
        xt = T @ xt
    return xt

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex A after t steps.

x_t3 = random_walk(T, X0, 3)
x_t10 = random_walk(T, X0, 10)
x_t100 = random_walk(T, X0, 100)

print(f"x_3 = {x_t3}\nx_10 = {x_t10}\nx_100 = {x_t100}")
print() #What pattern do you see emerging? 

### Task 3 ###############################
print("~Task 3~")
print("Starting at vertex B")

X = np.zeros((k+1,6))
Y = np.array([0,1,0,0,0,0])

y_t3 = random_walk(T, Y, 3)
y_t10 = random_walk(T, Y, 10)
y_t100 = random_walk(T, Y, 100)

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex B after t steps.

print(f"x_3 = {y_t3}\nx_10 = {y_t10}\nx_100 = {y_t100}")
print() #What pattern do you see emerging? 

#What happens if another vertex is the starting location? 
#Make a conjecture about X[t] as t -> infinity. 
#How could this information had been gleaned from the original graph in retrospect?
print()
