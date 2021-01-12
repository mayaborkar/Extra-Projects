import math

a = input("a=")
b = input("b=")
c = input("c=")
underroot = b**2-4*a*c
negb = -1*b
divtwo = 2*a

if a==0:
	print(-c/(b))
else:
	if (b**2-4*a*c)<0:
		print("that is a complex problem...")
	else:
        print ("(" + str(negb) + " + sqrt(" + str(underroot) + "))/" + str(divtwo))