#Tracking memory address of different variables

#Integer

x = 10
print(id(x))
x = 20
print(id(x))
print("Id of x changed")

x = 25
print(id(x))
x += 1
print(id(x))
print("Id of x changed")

x = 30
print(id(x))
x *= 2
print(id(x))
print("Id of x changed")

x = 50
print(id(x))
y = x
print(id(y))
print("Both x and y have same Id")

#Hence we can see integer is an immutable data type because any change leads to new id

#Float 

x = 1.5
print(id(x))
x = 2.4
print(id(x))
print("Id of x changed")

x = 3.6
print(id(x))
x -= 1
print(id(x))
print("Id of x chnaged")

x = 4.2
print(id(x))
x = round(x,2)
print(id(x))
print("Id of x changed")

#Hence we can see float is an immutable data type as id changes with operations on it.
