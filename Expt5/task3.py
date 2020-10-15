from task2 import syndrome_decode, mod2, equal
import numpy as np


n = 7
k = 4
G = np.array([1,0,0,0,1,1,0,
                0,1,0,0,1,0,1,
                0,0,1,0,0,1,1,
                0,0,0,1,1,1,1
                ]).reshape(k,n)
# print(G)
print("Testing all 2**k = 16 valid codewords")

for number in range(2**k):
    word = np.array(list(bin(number)[2:].zfill(k)), dtype=int).reshape(1,k)
    # print(bin(number))
    # print(bin(number)[2:])
    # print(bin(number)[2:].zfill(k))
    # print(list(bin(number)[2:].zfill(k)))
    # print(np.array(list(bin(number)[2:].zfill(k)), dtype=int))
    # print(np.array(list(bin(number)[2:].zfill(k)), dtype=int).reshape(1,k))
    # print("Word:")
    # print(word)
    codeword = mod2(np.dot(word, G))
    # print("Codeword:")
    # print(codeword)
    decoded_word = syndrome_decode(codeword, n,k,G)
    # print("Decoded word:")
    # print(decoded_word)
    if not equal(codeword, decoded_word):
        print("Error decoding "+str(codeword)+" ... expected "+str(word)+" got " + str(decoded_word))
        break
else:
    print("...passed")

print("Testing all n*2**k = 112 single-bit error codewords")
for number in range(2**k):
    word = np.array(list(bin(number)[2:].zfill(k)),dtype=int).reshape(1,k)
    codeword = mod2(np.dot(word, G))
    for i in range(len(codeword)):
        codeword[0][i] = not(codeword[0][i])
        decoded_word = syndrome_decode(codeword, n,k,G)
        if not equal(codeword, decoded_word):
            print("Error decoding "+str(codeword)+" ... expected "+str(word)+" got " + str(decoded_word))
            break
        else:
            codeword[0][i] = not(codeword[0][i])
else:
    print("...passed")

print("All 0 and 1 error tests passed for (7,4,3) code with generator matrix G = \n",G)