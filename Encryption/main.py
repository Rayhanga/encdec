from Utils import mtk
from random import randint
import math

def getKey():
    key = '0'
    x = 0
    while '0' in str(key) or len(str(key)) < 7:
        a = mtk.getRandPrime()
        b = mtk.getRandPrime()
        c = mtk.getRandPrime()
        key = mtk.getRandPrime(0,a*b*c)
        # x = x + 1
        # print("{} tries : {}".format(x, key))
    k = []
    for c in str(key):
        k.append(chr(int(c)+67))

    # print(key)
    # print("".join(k))

    return "".join(k[::-1])

def encrypt(msg, key):
    err = False
    k = []
    for c in key:
        try:
            k.append(str(ord(c)-67))
        except ValueError:
            err = True
            break

    try:
        k = int("".join(k[::-1]))
    except ValueError:
        err = True

    try:
        mtk.isPrime(k)
    except TypeError:
        err = True

    if(not err):
        if(mtk.isPrime(k) and len(key) >= 7):
            x = len(str(k))
            y = len(msg)

            if x <= y:
                z = y-x
                key = str(k)
                for i in range(math.ceil(z / x)):
                    z = len(msg) - len(key)
                    key = key + str(k)[0:z]
                s = []
                s.append("=")
                # debug = []
                for i, c in enumerate(msg):
                    # debug.append(str(ord(c) * int(key[i])))
                    s.append(chr(ord(c) * int(key[i])))
                s.append("=")
                # print(key)
                # print(msg)
                # print("".join(debug))
                return "".join(s)
            else:
                z = x-y
                key = str(k)[:7]
                s = []
                
                for i, c in enumerate(msg):
                    s.append(chr(ord(c) * int(key[i])))

                return "".join(s).encode().decode('utf-8')

    print("Kunci Invalid!")

def decrypt(msg, key):
    err = False
    k = []
    for c in key:
        try:
            k.append(str(ord(c)-67))
        except ValueError:
            err = True
            break

    try:
        k = int("".join(k[::-1]))
    except ValueError:
        err = True

    try:
        mtk.isPrime(k)
    except TypeError:
        err = True

    if(not err):
        if(mtk.isPrime(k) and len(key) >= 7):
            x = len(str(k))
            y = len(msg)

            msg = msg.replace('=', '').encode().decode('utf-8')

            if x <= y:
                z = y-x
                key = str(k)
                for i in range(math.ceil(z / x)):
                    z = len(msg) - len(key)
                    key = key + str(k)[0:z]
                s = []
                # debug = []
                for i, c in enumerate(msg):
                    # debug.append(str(ord(c) * int(key[i])))
                    try:
                        s.append(chr(int(ord(c) / int(key[i]))))
                    except:
                        print("Kunci Invalid!")
                        break
                return "".join(s) 
            else:
                z = x-y
                key = str(k)[:7]
                s = []
                for i, c in enumerate(msg):
                    s.append(chr(int(ord(c) / int(key[i]))))
                return "".join(s)      

    print("Kunci Invalid!")