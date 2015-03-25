#DES KEY GENERATION ALGORITHM
#Objective: We have 64-bit input. We apply first#
#permutation and have 56-bits left. We divide it#
#into two 28 bits of data. Then we shift them to#
#left for 1 digit, put them together and apply  #
#second permutation. Now we have 48 bits of data#
#and we have our first key. We do this until we #
#have all 16 keys.
#
#Author: Tugberk Kocatekin

print "This program is for DES key algorithm"

key = "ABCDEF1234567893"

print "Our key is ", key

def keytobin(string):
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
    text = ""
    for c in string:
        text += conversion[c]
    return text

mykey = keytobin(key)
print "Now we have 64 bits"
print mykey
print "-------------"



#now we have our 64bit string. we should permute it


perm1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51,
         43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7,
         62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20,
         12, 4]

perm2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16,
         7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44,
         49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]




#here we do permutation --> a is my key b is permutation
def permute(a,b):
    newstr = ""
    for i in b:
        newstr += a[i-1]
    return newstr

#print "We apply permutation"
firstperm = permute(mykey, perm1)
#print "We now have 56 bits"
#print firstperm, len(firstperm)

#simdi elimde ilk permutation var

#iki parca alacagim buradan.

C = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
D = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

C[0] = firstperm[0:28]
D[0] = firstperm[28:56]
'''
print "This is my first half"
print C[0]
print "This is the second half"
print D[0]
'''


def rotateLeft(text):
    length = len(text)
    text += text[0]
    text = text[1:]
    return text

rotated_c = rotateLeft(C[0])
rotated_d = rotateLeft(D[0])


#we need to get these together and apply second perm

#we concatenate two halves into one
together = C[0] + D[0]
secondperm = permute(together, perm2)




#lets create all shifts of C and D
for i in range(1, 16):
    C[i] = rotateLeft(C[i-1])
    D[i] = rotateLeft(D[i-1])
    


print "1", secondperm
for i in range(1, 16):
    connect = C[i] + D[i]
    secondperm = permute(connect, perm2)
    print i+1, secondperm





















    
    




