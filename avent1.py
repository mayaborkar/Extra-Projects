f1 = open("aventlist1.txt", "r")
# print(f1.readlines())
mylist = f1.readlines()
print mylist
for i in range(0, len(mylist)-1):
    for j in range(i+1, len(mylist)):
        stx = mylist[i]
        x = int(stx[0:len(stx)-1])
        stx = mylist[j]
        y = int(stx[0:len(stx)-1])
        if x + y == 2020:
            print x * y
