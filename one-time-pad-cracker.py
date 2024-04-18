# Author: Ethan Skipsey
# Description: A program that can be used to crack a one-time-pad with key reuse.
# Date: 18/04/2024

def encrypt(m, k):
    if len(m) != len(k):
        raise Exception("Message and key must be the same length to encrypt.")
    
    c = bytearray(len(m))
    for i in range(len(m)):
        c[i] = m[i] ^ k[i]
    
    return c

def decrypt(c, k):
    if len(c) != len(k):
        raise Exception("Ciphertext and key must be the same length to decrypt.")
    
    m = bytearray(len(c))
    for i in range(len(c)):
        m[i] = c[i] ^ k[i]
    
    return m

def crack(c1, c2, crib):
    if len(c1) != len(c2):
        raise Exception("Ciphertexts must be the same length to crack.")

    a = bytearray(len(c1))
    for i in range(len(c1)):
        a[i] = c1[i] ^ c2[i]
    
    m = bytearray(len(crib))
    for i in range(len(c1))[:-len(crib)]:
        for j in range(len(crib)):
            m[j] = a[i+j] ^ crib[j]
        print(f"{i}\t{m.decode()}")

if __name__=="__main__":

    c1 = input("Enter the first encrypted message: ").encode()
    c2 = input("Enter the second encrypted message: ").encode()

    print("Type '/quit' to exit this program.")

    while True:
        crib = input("Enter the text you would like to try: ").encode()
        if crib == b"/quit":
            break
        crack(c1, c2, crib)