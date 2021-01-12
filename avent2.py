f1 = open("aventlist1.txt", "r")
# print(f1.readlines())
mylist = f1.readlines()
for i in range(0, len(mylist)-1):
    for j in range(i+1, len(mylist)):
        for k in range(j+1, len(mylist)):
            stx = mylist[i]
            x = int(stx[0:len(stx)-1])
            stx = mylist[j]
            y = int(stx[0:len(stx)-1])
            stx = mylist[k]
            z = int(stx[0:len(stx)-1])
            if x + y + z == 2020:
               print x
               print y
               print z
               print x * y * z
