number = 1

for number in range(1 , 16 , +1):
    # checking if divisible by 15 before checking divisible by 3 or 5
    if number % 15 == 0 :
        print "FizzBuzz"
    # checking if divisible by 3
    elif number % 3 == 0 :
        print "Fizz"
    # checking if divisible by 5
    elif number % 5 == 0 :
        print "Buzz"
    else :
        print number
    # incrementing number to next value
    number = number+1

