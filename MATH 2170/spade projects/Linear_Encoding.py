import numpy as np

### TASK 1 ###
def linear_code(A):
    #Write code here
    #will output canonical parity check matrix
    #and generator matrix associated to A
    a = A % 2
    m, nmm = A.shape

    im = np.identity(m)
    g = np.concatenate((im, a), axis=1)

    inmm = np.identity(nmm)
    h = np.concatenate((A.T, inmm), axis=1)
    
    return h, g

def linear_code_H(A):
    #Write code here
    #will output canonical parity check matrix
    #and generator matrix associated to A
    nk, k = A.shape

    ink = np.identity(nk)
    ik = np.identity(k)

    h = np.hstack((A, ink)) % 2
    g = np.vstack((ik, A.T)) % 2

    return h

def linear_code_G(A):
    nk, k = A.shape

    ink = np.identity(nk)
    ik = np.identity(k)

    h = np.hstack((A, ink)) % 2
    g = np.vstack((ik, A.T)) % 2

    return g

### TASK 2 ###
def linear_encode(G,message):
    #write code here
    #will output the encoded message for
    #the linear code associated to generator matrix G
    message = np.array(message) % 2
    G = np.array(G) % 2

    cw = (message @ G) % 2
    return cw


### VERIFICATION ############################
### TASK 1 ###
A = np.array([[0,1,1],[1,1,0],[1,0,1]])
G = linear_code_G(A)
H = linear_code_H(A)
print("H = \n", H,"\nG = \n",G,"\n")

### TASK 2 ###
A = np.array([[1,1],[1,0],[1,1]])
G,H = linear_code(A)
for w in [[0,0],[0,1],[1,0],[1,1]]:
    print(linear_encode(G,w))
print("\n")
