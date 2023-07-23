billAmount = int(input("enter the bill amount: "))

if billAmount < 500:
    discount = billAmount * 0.05
    print('your discount is: ', discount)
else:
    discount = billAmount * 0.10
    print('your discount is: ',discount)

print("your final amount is: ", billAmount-discount)