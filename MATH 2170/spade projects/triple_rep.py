import numpy as np

def encode_triplerep(message):
    #write your code here
    #returns triple_repeated_message
    return np.concatenate((message, message, message))

def decode_triplerep(codeword):
    #write your code here
    #returns decoded_message (with errors corrected)
    bit_amt = int(len(codeword)/3)
    code_1 = codeword[:bit_amt]
    code_2 = codeword[bit_amt:2*bit_amt]
    code_3 = codeword[2*bit_amt:3*bit_amt]

    return np.round((code_1 + code_2 + code_3)/3)

### VERIFICATION ############################
Words = np.array([[1,1,0,0],
                  [0,0,1,1],
                  [0,1,1,0]])
for w in Words:
    print(encode_triplerep(w))
print("\n")

Codewords = np.array([[0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1],
                      [0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
                      [1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1],
                      [0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1],
                      [1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1]])
for c in Codewords:
    print(decode_triplerep(c))
