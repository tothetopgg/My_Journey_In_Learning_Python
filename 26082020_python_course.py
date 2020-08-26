### 26 / 08 / 2020
### Tommy Broekman
### The range Function

# Using the range fucntion
for value in range(1,5):
    print(value)


# converting numbers in a list

numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1,101, 2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5]
print(min(digits))
print(max(digits))
print(sum(digits))

# slicing a list 
names = ['Tommy', 'Jannik', 'Philipp', 'jose']
print(names[1:4])
print(names[:3])
print(names[-3:])
print(names[3:])

# looping trough a slice with a for loop
names = ['Tommy', 'Jannik', 'Philipp', 'jose', 'Jens']
print("Here are the names of the last 3 registrations:")
for name in names[:3]:
    print(name.title())

# Copying a list
names = ['Tommy', 'Jannik', 'Philipp', 'jose', 'Jens']
first_names = names[:]
print(first_names)

# Tuples
dates = [1, 4, 7, 11]
print(dates[0])
print(dates[2])

coordinates = (1001, 5002)
print("Original coordinates:")
for coordinate in coordinates:
    print(coordinate) 

coordinates = (2001, 6002)
print("\nNew coordinates:")
for coordinate in coordinates:
    print(coordinate)

# input statements
welcome = input("Welcome what is your name: ")
print("Hello " + welcome)

# Python's if statement
print("To continue please log in.")

password = input("Please fill in your password: ")
if password == "janniksucks":
    print("Welcome Tommy")
else:
    print("Incorrect password. Please try again")
#conditional tests in Python.