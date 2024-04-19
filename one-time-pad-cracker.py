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
    for i in range(len(c1))[:-len(crib)+1]:
        for j in range(len(crib)):
            m[j] = a[i+j] ^ crib[j]
        print(f"{i}\t{m.decode()}")

if __name__=="__main__":

    c1_hex = ("111141184e1c071508010153411901001f04171700030e530d1641064f52170"
    "81308030952540b175904061a1607531f4f061800151c455703040d001c1d491d0b174905"
    "160001011100051d561e0c0410000d170009100009411a0a554206410f00001a590c1d071"
    "653154c1e051c1253520403014d090b1d57070b0b100945130245411b1600040712451e45"
    "100c4f0a4f45161f1143124f07144914000004161f0b1a194f0000")
    c1_bytes = bytes.fromhex(c1_hex)

    c2_hex = ("05005441071b4e1f1f0018534d0e45571207121b540841110e5346110e521e0"
    "00516410e4554090b4f1a0b181b1d534c1b070e00111553041f0e0644491a53491a1b0c44"
    "1641030a54411254541f0d411f45164e4e1c55140300114549060041124e0e1c1c4d0d001"
    "f4c04180713161c46520104024d03115254030b4f05030a10144549070054150e13451d46"
    "570f55171b00060e174b0f011547080245540d1d50090615561000")
    c2_bytes = bytes.fromhex(c2_hex)

    print("Type '/quit' to exit this program.")

    while True:
        crib = input("Enter the text you would like to try: ").encode()
        if crib == b"/quit":
            break
        crack(c1_bytes, c2_bytes, crib)