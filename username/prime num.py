import math


def check_prime(your_num):
    sqrt = int(math.sqrt(your_num))
    is_prime = True
    for i in range(2, sqrt + 1):
        if your_num % i == 0:
            is_prime = False
    return is_prime


number = input("Put in a number to check if it is prime: ")
check_prime(int(number))

if check_prime(int(number)):
    print("This number is prime")
else:
    print("This number is not prime")
