#calculate avg of nums in a list

listSize = int(input("enter your list size: "))

myList = []

for i in range(0,listSize):
    userNum = int(input("enter a number: "))
    myList.append(userNum)

avg = sum(myList)/listSize

print("average of the list numbers is: ", round(avg,3))
