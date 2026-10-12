with open("d.txt", "r") as f:
    d = int(f.read())

with open("n.txt", "r") as f:
    n = int(f.read())

print("Private Key Loaded:")
print("d =", d)
print("n =", n)

with open("encrypted.txt", "r") as f:
    cipher_int = int(f.read())

print("Encrypted integer:", cipher_int)

message_int = pow(cipher_int, d, n)

print("Decrypted integer:", message_int)

message_binary = message_int.to_bytes(
    (message_int.bit_length() + 7) // 8,
    "big"
)

with open("decrypted.txt", "wb") as f:
    f.write(message_binary)

print("Decryption complete → decrypted.txt created")