from datetime import datetime

def getRandPrime(p = 0, k = None):
    t = datetime.now()
    h = 0
    if p == 0:
        key = int(t.microsecond*t.second)
    else:   
        key = k + 1

    # print(p, key)

    if isPrime(key):
        # print("{} adalah prima!".format(key))
        return key
    else:
        return getRandPrime(p+1, key)

def fpb(a, b):
    # Euclid's Algorithm
    x = max([a,b])
    y = min([a,b])
    z = x-y

    if z == 0:
        return y
    else:
        return fpb(y,z)

def isPrime(x):
    res = True
    hit = 0
    for i in range(1, x):
        if x % i == 0:
            hit = hit + 1 
        if hit > 2:
            res = False
            break
    return res

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
