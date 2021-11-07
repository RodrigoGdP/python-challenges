import math
def dbin (num):
    bin = []
    while num / 2 >= 0.5:
        bin.append(num % 2)
        num = math.floor(num / 2)
    bin.reverse()
    return bin
print (dbin(1025))