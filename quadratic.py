import math


def mysquareroot(x):
	y = math.sqrt(x)
	y = int(math.floor(y))
	for i in range(y, 1, -1):
		z = x % (i*i)
		if z == 0:
			return i


a = input("a=")
b = input("b=")
c = input("c=")

if a == 0:
	if b == 0:
		print("Not a quadratic equation")
	else:
		print ("x = " + str(-c/b))
else:
	if (b ** 2 - 4 * a * c) < 0:
		print("that is a complex problem...")
	else:
		partroot = b**2-4*a*c
		if math.floor(math.sqrt(partroot)) == math.sqrt(partroot):
			print ("this is a perfect square")
			quadraticplus = (-b+(math.sqrt(b**2-4*a*c)))/(2*a)
			print (quadraticplus)
			quadraticminus = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
			print (quadraticminus)
		else:
			print ("this is not a perfect square")
			squarefactor = mysquareroot(partroot)
			remaining = partroot / (squarefactor * squarefactor)
			if b == 0:
				print ("x = " + str(squarefactor/(2*a)) + " sqrt(" + str(remaining) + ")")
				print ("x = " + "-" + str(squarefactor/(2*a)) + " sqrt(" + str(remaining) + ")")
			else:
				print ("x = " + str(-b) + "+" + str(squarefactor) + " sqrt(" + str(remaining) + ")" + "/" + str(2 * a))
				print ("x = " + str(-b) + "-" + str(squarefactor) + " sqrt(" + str(remaining) + ")" + "/" + str(2 * a))
