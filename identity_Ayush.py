#Tracking memory address of different variables

#Integer

x = 10
print(id(x))
x = 20
print(id(x))
print("Address of x changed")

x = 25
print(id(x))
x += 1
print(id(x))
print("Address of x changed")

x = 30
print(id(x))
x *= 2
print(id(x))
print("Address of x changed")

x = 50
print(id(x))
y = x
print(id(y))
print("Both x and y have same address")

#Hence we can see integer is an immutable data type because any change leads to new id
