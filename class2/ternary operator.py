a = 10
b = 20

print("a is max") if a>b else print("b is max")



a = 8
z = ("odd", "even")[a%2 == 0]
print("Z = ", z)

a = 100
b = 20
z = {True: a, False: b}[a>b]
print("Z = ", z)


a = 100
b = 20
z = (b,a) [a>b] 
print("Z = ", z)