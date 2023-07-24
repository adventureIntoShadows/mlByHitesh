# wap to find second largest number

listSize = int(input("enter the list size: "))

mylist = []

for i in range(0, listSize):
    lElement = int(input('enter your number: '))
    mylist.append(lElement)

mylist.sort()

print("second largest number is: ", mylist[listSize-2])
#   if you want to undertand why listSize-2 , use pen and paper
