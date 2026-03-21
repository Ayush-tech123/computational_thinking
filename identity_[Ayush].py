#Tracking memory address of different variables

#Integer

x = 10
print(id(x))
x = 20
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = 25
print(id(x))
x += 1
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = 30
print(id(x))
x *= 2
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = 50
print(id(x))
y = x
print(id(y))
print("Both x and y have same Id")
print("---------------------------------")

#Hence we can see integer is an immutable data type because any change leads to new id

#Float 

x = 1.5
print(id(x))
x = 2.4
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = 3.6
print(id(x))
x -= 1
print(id(x))
print("Id of x chnaged")
print("---------------------------------")

x = 4.2
print(id(x))
x = round(x,2)
print(id(x))
print("Id of x changed")
print("---------------------------------")

#Hence we can see float is an immutable data type as id changes with operations on it.

#String

x = "ayush"
print(id(x))
x = "sharma"
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = "Hi "
print(id(x))
x = x + "!"
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = "AYUSH"
print(id(x))
x = x.lower()
print(id(x))
print("Id of x changed")
print("---------------------------------")

#Hence we can see string is also an immutable data type

#Boolean

x = True
print(id(x))
x = False
print(id(x))
print("Id of x changed")
print("---------------------------------")

x = False
print(id(x))
x = x or True
print(id(x))
print("Id of x changed")
print("---------------------------------")

#Hence it is observed boolean is also a immutable data type

#Tuple

x = (1, 2, 3)
print(id(x))
x = (4, 5, 6)
print(id(x))
print("Id of x changed")
print("---------------------------------")

#Hence tuple is also a immutable data type

#List

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(id(x))
x.append(y)
print(id(x))
print("Id of x is same")
print("---------------------------------")

x = [2, 3, 1, 5, 4]
print(id(x))
x.sort()
print(id(x))
print("Id of x is same")
print("---------------------------------")

x = [95, 96, 97, 98, 98, 100]
print(id(x))
x[-2] = 99
print(id(x))
print("Id of x is same")
print("---------------------------------")

x = [1, 2, 3]
print(id(x))
x = [1, 2, 3, 4, 5]
print(id(x))
print("Id of x changed because we used = operation which created a brand new list")
print("---------------------------------")

#Hence list is an mutable data type

#Dictionary

x = {"ayush" : 100}
print(id(x))
x["rahul"] = 50
print(id(x))
print("Id of x is same")
print("---------------------------------")

x['aditya'] = 30
print(id(x))
x.pop('aditya')
print(id(x))
print("Id of x is same")
print("---------------------------------")

#Hence dictionary is also an mutable data type

#Set

x = {1, 2, 3}
print(id(x))
x.add(4)
print(id(x))
print("Id of x is same")
print("---------------------------------")

#Hence set is also a mutable data type
