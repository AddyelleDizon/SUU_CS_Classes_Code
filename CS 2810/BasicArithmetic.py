def negate(strBinary):
    flipped = ""
    for bit in strBinary:
        if bit == '0':
            flipped += '1'
        else:
            flipped += '0'
    result = ""
    carry = 1 
    for bit in reversed(flipped): 
        if bit == '1' and carry == 1:
            result = '0' + result
        elif bit == '0' and carry == 1:
            result = '1' + result 
            carry = 0 
        else:
            result = bit + result
    return result
 
def convert(num):
    if num < 0:
        num += (1**32)
    strBinary = ""
    for i in range(32):
        strBinary = str(num % 2) + strBinary
        num //= 2  
    return strBinary

def printbinary(strBinary):
    for i in range(0, 32, 4):
        print(strBinary[i:i+4], end=" ")
    print()
    return

def add(a, b):
    result = ""
    carry = "0"
    for i in range(31, -1, -1):
        aBit = a[i]
        bBit = b[i]
        sum_bit = int(aBit) + int(bBit) + int(carry)
        if sum_bit == 0:
            result = "0" + result
            carry = "0"
        elif sum_bit == 1:
            result = "1" + result
            carry = "0"
        elif sum_bit == 2:
            result = "0" + result
            carry = "1"
        else:
            result = "1" + result
            carry = "1"
    return result

def sub(a, b):
    negB = negate(b)
    return add(a, negB)

def main():
    while True:
        print("\nChoose an operand:")
        print("1. Addition")
        print("2. Subtraction")
        print("0. Quit")
        choice = input("Choose: ")
        
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1" or choice == "2":
            num1 = int(input("Enter the first operand: "))
            num2 = int(input("Enter the second operand: "))
            
            bin1 = convert(num1)
            bin2 = convert(num2)
            
            if choice == "1":
                result = add(bin1, bin2)
                printbinary(bin1)
                print("+")
                printbinary(bin2)
            else:
                result = sub(bin1, bin2)
                printbinary(bin1)
                print("-")
                printbinary(bin2)
                
            print("-----------------------------------")
            printbinary(result)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()