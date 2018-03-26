perm1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51,
         43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7,
         62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20,
         12, 4]


perm2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16,
         7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44,
         49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

permInitial = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62,
               54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49,
               41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45,
               37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]


permExpansion = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12,
                 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24,
                 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-boxes
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
S = [S1, S2, S3, S4, S5, S6, S7, S8]

# permutation of B[j]
permP = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24,
         14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

# final permutation
permFinal = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38,
             6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4,
             44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42,
             10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def main():
    plaintext = "12345678"
    key = "ABCDEF1234567893"
    print "plaintext: ", plaintext
    print "key: ", key

    if len(plaintext) == 8:
        plaintext = toBinStr(plaintext) # ASCII
    if len(plaintext) == 16:
        plaintext = hexToBinStr(plaintext) # hex
    elif len(plaintext) != 64:
        print ('Error: Enter a string of 16 hex digits, 64 binary digits, or 8'
               ' ASCII characters.')
        return

    if len(key) == 8:
        key = toBinStr(key) # ASCII
    if len(key) == 16:
        key = hexToBinStr(key) # hex
    elif len(key) != 64:
        print ('Error: Enter a string of 16 hex digits, 64 binary digits, or 8 '
               ' ASCII characters.')
        return

    subkeys = sub_key_generation(key)
    #print subkeys
    
    plaintext = permute(plaintext, permInitial)

    ciphertext = round_alg(plaintext, subkeys)
    print "plaintext: ", plaintext
    print "key: ", key
    print "ciphertext is ", ciphertext
    

#s-box substitutions
def sBox(input, boxNum):
    assert(len(input) == 6)
    m = int(input[0]) * 2 + int(input[5]) * 1
    n = int(input[1]) * 8 + int(input[2]) * 4 + int(input[3]) * 2 + int(input[4]) * 1
    output = decToBin(S[boxNum][m][n])
    assert(len(output) == 4)
    return output

#permutation algorithm
def permute(original, permutation):
    newStr = ""
    for i in permutation:
        newStr += original[i-1]
    return newStr

#left rotation algorithm
def rotateLeft(binaryStr):
    length = len(binaryStr)
    binaryStr = binaryStr + binaryStr[0]
    binaryStr = binaryStr[1:]
    assert(len(binaryStr) == length)
    return binaryStr



#binary rep of a non-neg int.
def decToBin(n):
    assert(n >= 0)
    if n == 0:
        return '0000'
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        n = n >> 1
    assert(len(bin) <= 4)
    while len(bin) < 4:
        bin = '0' + bin
    return bin



def round_alg(plaintext, subkeys):
    
    L = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    R = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    L[0] = plaintext[0:32]
    R[0] = plaintext[32:64]
    for i in range(16):
        #we are expanding our 32 bit into 48 bit by using permExpansion
        E = permute(R[i], permExpansion)
        #we XOR with subkeys
        xor = strXOR(E, subkeys[i])
        #we divide 48 bits into 8x6 bits 
        B = ['', '', '', '', '', '', '', '']
        for j in range(8):
            B[j] = xor[j*6:j*6+6]
        #we apply substitution
        for k in range(8):
            B[k] = sBox(B[k], k)
        #combining all bits into one
        x = B[0] + B[1] + B[2] + B[3] + B[4] + B[5] + B[6] + B[7]
        x = permute(x, permP)
        R[i+1] = strXOR(x, L[i])
        L[i+1] = R[i]
       
    ciphertext = R[16] + L[16]
    ciphertext = permute(ciphertext, permFinal)
    return ciphertext


def sub_key_generation(key):
    C = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    D = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    K = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    key = permute(key, perm1)
    C[0] = key[0:28]
    D[0] = key[28:56]
    for i in range(1, 17):
        #rotation is done
        C[i] = rotateLeft(C[i-1])
        D[i] = rotateLeft(D[i-1])
        if i != 1 and i != 2 and i != 9 and i != 16:
            C[i] = rotateLeft(C[i])
            D[i] = rotateLeft(D[i])
        subkey = C[i] + D[i]
        subkey = permute(subkey, perm2)
        K[i-1] = subkey
    return K



# ascii to binary conversion
# convert ASCII string to binary string
def toBinStr(string):
    binaryStr = ''
    for c in string:
        binaryChar = bin(ord(c))[2:]
        while (len(binaryChar) < 8):
            binaryChar = '0' + binaryChar
        binaryStr += binaryChar
    return binaryStr

#hex to binary conversion
def hexToBinStr(string):
    conversion = {'0': '0000',
                  '1': '0001',
                  '2': '0010',
                  '3': '0011',
                  '4': '0100',
                  '5': '0101',
                  '6': '0110',
                  '7': '0111',
                  '8': '1000',
                  '9': '1001',
                  'A': '1010',
                  'B': '1011',
                  'C': '1100',
                  'D': '1101',
                  'E': '1110',
                  'F': '1111'}
    binaryStr = ''
    for c in string:
        binaryStr = binaryStr + conversion[c]
    return binaryStr

#binary to ascii conversion
def toASCIIstr(string):
    return int(string, 2)

#xor algorithm
def strXOR(x, y):
    #assert(len(x) == len(y))
    xor = ''
    for i in range(len(x)):
        if x[i] != y[i]:
            xor = xor + '1'
        else:
            xor = xor + '0'
    return xor


main()

    
    
