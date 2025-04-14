 #leap year using nested if
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year:", year)
        else:
            print("It isn't a leap year:", year)
    else:
        print("It is a leap year:", year)
else:
    print("It isn't a leap year:", year)




x = int(input("Enter the year: "))
if x%100 == 0:
    if x%400 == 0:
        print("It is a leap year:", x)
    else:
         print("It isn't a leap year:", x)
else:
    if x%4 ==0:
         print("It is a leap year:", x)
    else:
         print("It isn't a leap year:", x) 


