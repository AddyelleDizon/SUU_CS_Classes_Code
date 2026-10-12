import numpy as np

### TASK 1 #########
def Hamming_dist(x,y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def Hamming_norm(x):
    total_sum = 0
    for i in x:
        total_sum += i
    return total_sum
    
Words = np.array([[1,0,1,0,1],[1,1,0,1,0],[0,0,0,1,1]])

#Compute Hamming Distances
for i in range(len(Words)):
    for j in range(i+1,len(Words)):
        print(f"Hamming distance between {Words[i]} and {Words[j]} is {Hamming_dist(Words[i], Words[j])}.")
        
#Compute Hamming Norms
for w in Words:
    print(f"Hamming norm of {w} is {Hamming_norm(w)}.")
print("\n")

### TASK 2 #########
C = np.array([[0,0,0,0,0],[1,1,1,1,0],[1,0,1,0,1],[0,1,0,1,1]])

def decode_C(w):
    distances = [(i, Hamming_dist(w, i)) for i in C]
    closest, dist_min = distances[0]
    for i, dist in distances[1:]:
        if dist < dist_min:
            closest, dist_min = i, dist
    return closest

Words = np.array([[0,1,0,1,1],[1,1,1,0,0],[1,0,0,0,1]])
for w in Words:
    print(f"{w} decodes as {decode_C(w)}.")
print("\n")
