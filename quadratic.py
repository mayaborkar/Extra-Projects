import math

a=input("a=")
b=input("b=")
c=input("c=")
if a==0:
	print(-c/(b))
else:
	if (b**2-4*a*c)<0: 
		print("that is a complex problem...")
	else:
		quadraticplus=(-b+(math.sqrt(b**2-4*a*c)))/(2*a)
		print (quadraticplus)
		quadraticminus=(-b-(math.sqrt(b**2-4*a*c)))/(2*a)
		print (quadraticminus)
