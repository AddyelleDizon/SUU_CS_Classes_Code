

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclid_extended(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x1, y1 = euclid_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    
    strWithBits = format(exp, "b")
    
    for bit in strWithBits:
        result = (result * result) % mod
        if bit == '1':
            result = (result * base) % mod
    return result

def pseudoprime(n):
    if n <= 1:
        return "Composite"
    
    if mod_exp(2, n - 1, n) != 1:
        return "Composite"
    else:
        return "Prime"

d, x, y = euclid_extended(899, 493)

# Tests

print("gcd(899, 493) =", euclid(899, 493))
print("Extended Euclid:", d, x, y)
print("Modular Exp:", mod_exp(2, 20, 17))
print("Pseudoprime test 200:", pseudoprime(200))
print("Pseudoprime test 561:", pseudoprime(561))
print("Pseudoprime test 13:", pseudoprime(13))