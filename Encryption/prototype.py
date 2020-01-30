from Utils import mtk
from random import randint
from string import printable as src
import math

def getKey():
    k = str(mtk.getRandPrime())
    # print("key asli: ",k)
    x = []
    for c in k:
        x.append(src[(int(c)+27)%100])

    return "".join(x[::-1])

def encrypt(m, k):
    y = []
    for i in k:
        y.append(src[src.find(i)-27])

    key = int("".join(y[::-1]))

    x = []
    x.append("=")
    for c in m:
        x.append(src[int(key*src.find(c))%100])
    x.append("=")

    return "".join(x[::-1])

def decrypt(m, k):
    y = []
    for i in k:
        y.append(src[src.find(i)-27])

    key = int("".join(y[::-1]))

    x = []
    x.append("=")
    for c in m:
        x.append(src[int(src.find(c)*key)%100])
    x.append("=")

    return "".join(x[::-1])
