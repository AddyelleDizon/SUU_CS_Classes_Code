import numpy as np

### Parity Check Code ###
def encode_paritycheck(message):
    #write your code here
    #returns message with appended check bit
    check_bit = 1
    message_a = np.append(message, check_bit)
    return message_a

def detect_paritycheck(codeword):
    #write your code here
    #returns True or False
    

decode_paritycheck = lambda codeword : #write your code here, removes check bit

### Triple Repetition Code ###     
def encode_triplerep(message):
    #write your code here
    #returns triple_repeated_message

def decode_triplerep(codeword):
    #write your code here
    #returns decoded_message (with errors corrected)
        
### VERIFICATION ############################
print(" Task 1\n")
print(encode_paritycheck([1,1,0,1]), "\n")

#The last bit is a parity-check bit.
Words = np.array([[0,0,1,1,0,1,1],
                  [1,1,1,0,1,1,0],
                  [1,0,0,1,0,1,1],
                  [1,1,0,0,1,1,1],
                  [1,1,1,1,1,1,0]])
for w in Words:
    if detect_paritycheck(w):
        print("Error: ", w)
    else:
        print(decode_paritycheck(w))
 
print("\n\n Task 2\n")
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
