### 27 / 08 / 2020
### Tommy Broekman
### Lesson 37 to 41

# Conditional tests 
password = 'tony'
password == 'tony'
True
password == 'Tony'
False
password1 = 'Frank'
# password1.lower = 'Frank'
password1.lower() == 'frank'
True

# When Values are not equal to eachother
my_birthday = 'November'
if my_birthday != 'March':
    print("It is not your birthday.")

# Comparing numbers
age = 18
age == 18
True
age = 23
if age != 22:
    print("Sorry no cake for you.")

age = 21
age < 21
False
age > 21
False
age <= 21
True
age >= 21
True

# Checking multiple conditions with the and condition
username = input("Welcome, what is your username:")
password = input("What is your password:")
if username != 'tommy' and password != '1234':
    print("Username or password is not correct!")
else:
    print("Welcome Tommy")

# or conditions 
your_age = input("How old are you?")
friends_age = input("How old is your friend?")
if int(your_age) >= 18 or int(friends_age) >= 18:
    print('congrats one of you is old enough!')
else:
    print('both of you are not old enough!')