import math

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a == 0:
	print(-c/b)
else:
	if (b**2-4*a*c) < 0:
		print("that is a complex problem...")
	else:
		quadraticPlus = (-b+(math.sqrt(b**2-4*a*c)))/(2*a)
		print(quadraticPlus)
		quadraticMinus = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
		print(quadraticMinus)
