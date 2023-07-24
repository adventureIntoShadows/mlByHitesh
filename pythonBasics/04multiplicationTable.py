#WAP to print multiplication table


number = int(input("enter the number you want multiplication table for: "))

for i in range(1,11):
    if (i == 10):
        print(number, ' * ' , i , '= ', number*i)
    else:
        print(number, ' * ' , i , ' = ', number*i)
    

