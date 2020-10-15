import numpy as np

def mod2(A):
    for i in range(2):
        A[A%2==i] = i
    return A

def equal(a, b):
    if (a == b).all():
        return True
    return False

def syndrome_decode(codeword, n, k, G):
    A = G[:, k:n]
    I = np.identity(n-k, dtype=int)
    H = np.concatenate((A.T, I), axis = 1)
    
    c_decoded = mod2(np.dot(H, codeword.T))

    for i in range(k):
        P = np.zeros((n,), dtype=int)
        P[i] = 1
        syndrome = np.dot(H, P.T)
        if equal(syndrome, c_decoded):
            codeword[i] = int(not codeword[i])
            break

    return codeword[:k]



if __name__ == "__main__":
    n=7
    k=4
    G = np.array([1,0,0,0,1,1,0,
                  0,1,0,0,1,0,1,
                  0,0,1,0,0,1,1,
                  0,0,0,1,1,1,1
                ]).reshape(k,n)
    print("Generator Matrix:")
    print(G)
    codeword = np.array([1,1,1,0,1,0,1])
    
    print("Received message:")
    print(codeword[:k].tolist())
    
    message = syndrome_decode(codeword, n, k, G)
    print("Corrected message:")  
    print(message.tolist())