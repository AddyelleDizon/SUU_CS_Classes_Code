import numpy as np

def linear_code(A):
    a = A % 2
    m, nmm = A.shape

    im = np.identity(m)
    g = np.concatenate((im, a), axis=1)

    inmm = np.identity(nmm)
    h = np.concatenate((A.T, inmm), axis=1)
    
    return h, g

def linear_decode(H,message):
    #write code here
    #will return the decoded message if no errors
    #correct the error if possible, then decode
    #return "Error uncorrectable" if cannot be corrected
    H = np.array(H) % 2
    w = np.array(message) % 2
    m, n = H.shape

    s = (H @ w.T) % 2

    if np.all(s == 0):
        info = w[:n - m] 
        return f"No errors.{info.tolist()}"

    for j in range(n):
        if np.array_equal(H[:, j], s):
            w[j] ^= 1
            info = w[:n - m]
            return f"Single-bit error corrected at bit {j+1}. Corrected 5-vector: {info.tolist()}"

    return "Error uncorrectable."

### VERIFICATION ############################
A = np.array([[1,1,1,0,0],
              [1,0,1,1,1],
              [1,1,0,1,0],
              [0,0,1,1,1],
              [0,1,0,0,1]])
H,G = linear_code(A)
words = [[1,0,0,1,0,1,1,1,0,0],
         [0,1,1,0,1,0,0,1,0,0],
         [1,1,0,0,0,0,0,0,1,1],
         [1,1,0,0,1,0,1,0,1,0],
         [1,1,1,0,1,1,1,0,0,0]]
for w in words:
    print(linear_decode(H,w))
