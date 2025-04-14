# write a programm, get 5 prices by the user, and print the total, if total>1000, then the user will get 10% dicount
print("Enter prices: ")
price1 = int(input())
price2 = int(input())
price3 = int(input())
price4 = int(input())
price5 = int(input())

sum = price1 + price2 + price3 + price4 + price5

print("Total sum is: :", sum)

if sum>1000:
    dis = sum*(10/100)
else:
    dis = 0;
print("Discount is: ", dis)
print("Total price: ", sum-dis)           
