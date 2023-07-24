#WAP for identity matirix

matSize = int(input("enter matrix size: "))

for i in range(0,matSize):
    for j in range(0,matSize):
        if(i == j):
            print(1, sep=' ', end=' ')
        else:
            print(0, sep=' ', end=' ')

    print()


