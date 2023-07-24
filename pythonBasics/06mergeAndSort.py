#wap to merge two lists and then sort them

mylist1 = []
mylist2 = []

listSize = int(input('enter size of list 1: '))

for i in range(1,listSize+1):
    element1 = int(input('enter your number: '))
    mylist1.append(element1)

listSize = int(input('enter size of list 2: '))

for i in range(1,listSize+1):
    element1 = int(input('enter your numnber: '))
    mylist2.append(element1)

mergeList = mylist1 + mylist2

mergeList.sort()

print(mergeList)
