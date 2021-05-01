# with open("flag.txt") as f:
#     flag = f.read().strip()


# A = REDACTED
# B = REDACTED
A = 21
B = 14

# plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

# assert all(x in plaintext_space for x in flag)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

def decrypt(ciphertext: str, a: int, b: int) -> str:
    plaintext = ""
    for x in ciphertext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        plaintext += x

    return plaintext

if __name__ == "__main__":
    flag="HLIM{OCLSAQCZASPYFZASRILLCVMC}"
    ciphertext = decrypt(flag, a=A, b=B)
    print(ciphertext)
    # for A in range(1,25):
    #     #print(A)
    #     a_inv=egcd(A, 26)[1]
    #     print(a_inv*A%26)
    #     #print(a_inv)
    #     #for B in range(0,25):
    #         #ciphertext = decrypt(flag, a=A, b=B)
    #         #print(ciphertext)
