### 31 / 08 / 2020
### Tommy Broekman
### Lesson 42 to 45

# Using the OR keyword to check values in a list
registered_names = ['Tommy', 'Jens', 'Jose', 'Jannik']
username = input('Please enter an username: ')
if username in registered_names:
    print('Sorry, username is already taken!')
else:
    print('Username is available.')

#check if a value is not in the list 
admin_names = ['Tommy', 'Jens', 'Jose', 'Jannik']
username = input('Please enter an username: ')
if username not in admin_names:
    print('You do not have access')
else:
    print('Welcome lol')

# interest rate checker using if-elif-else
balance = input("What is your bank balance? ")
if int(balance) <= 0:
    print("Would you like to make a deposit?")
elif int(balance) <= 50: 
    print("You do not qualify for interest!")
elif int(balance) <= 100:
    print("Your interest is 1%")
else: 
    print("Your interest is 2%")

# Multiple conditions
booking_details = ['tony', 'middle row', 'screen two']

if 'tony' in booking_details:
    print("Welcome to the cinema!")
if 'middle_row' in booking_details:
    print('Your receipt is 010 in the middle row')
if 'screen two' in booking_details:
    print("Your film is in screen two")
