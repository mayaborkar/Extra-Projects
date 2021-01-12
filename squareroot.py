import math


def mysquareroot(x):
    y = math.sqrt(x)
    y = int(math.floor(y))
    for i in range(y, 1, -1):
        z = x % (i*i)
        if z == 0:
            return i


a = input("what is the number? ")
squarefactor = mysquareroot(a)
b = mysquareroot(a)
remaining = a/(b*b)
print (str(squarefactor) + " sqrt(" + str(remaining) + ")")




