import numpy as np

### Parity Check Code ###
def encode_paritycheck(message):
    #write your code here
    #returns message with appended check bit
    total = sum(message)
    check_bit = total % 2
    message_a = np.append(message, check_bit)
    return message_a

def detect_paritycheck(codeword):
    #write your code here
    #returns True or False
    new_codeword = encode_paritycheck(codeword)
    if new_codeword[-1] == 0:
        return False
    else:
        return True

decode_paritycheck = lambda codeword: np.delete(codeword, -1) #write your code here, removes check bit
        
### VERIFICATION ############################
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
 