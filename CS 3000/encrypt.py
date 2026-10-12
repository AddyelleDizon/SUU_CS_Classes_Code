with open("e.txt", "r") as f:
    e = int(f.read())

with open("n.txt", "r") as f:
    n = int(f.read())

print("Public Key Loaded:")
print("e =", e)
print("n =", n)

with open("message.txt", "rb") as f:
    binary = f.read()

message_int = int.from_bytes(binary, "big")

print("Message as integer:", message_int)

cipher_int = pow(message_int, e, n)

print("Encrypted integer:", cipher_int)

with open("encrypted.txt", "w") as f:
    f.write(str(cipher_int))

print("Encryption complete → encrypted.txt created")