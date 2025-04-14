# write a programm to interchange two numbers
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
swap = a;
a = b;
b = swap
print("a = ", a, "b = ", b)


 #write a programm to interchange two numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a = a + b
b = a - b
a = a - b
print("a = ", a, "b = ", b)

# write a programm to check if the given number is equals to 100 or not

num = int(input("Enter a number: "))
if num == 100:
    print("Yes 100")
else:
    print("not 100")


# Write a promgramm to find the max of 2 nums
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

if x>y:
    print("x(",x,") is max")
else:
     print("y(",y,") is max")


#Write a promgramm to check the given number is odd even
x = int(input("Enter a number: "))
if x%2 == 0:
    print("x is even")
else:
    print("x is odd")




x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd numner: "))

if x>y and x>z:
    print("x(",x,") is max")
elif y>z:
    print("y(",y,") is max")
else:
    print("y(",y,") is max")




# nested if
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd numner: "))

if x>y:
    if x>z:
        print("x(",x,") is max")
    else:
        print("z(",z,") is max")
else:
    if y>z:
        print("y(",y,") is max")
    else:
        print("z(",z,") is max")







