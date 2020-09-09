# 09 / 09 / 2020
# Tommy Broekman
# Lesson 46 to Lesson 51

# Updated if with lists
shopping_cart = ['tomato', 'cheese', 'butter', 'ham']
for item in shopping_cart:
    if item == 'tomato':
        print('Sorry this item is out of stock!')
    else:
        print('Adding ' + item + ' to your order.')

print('Your order is complete.')

print("-----------------------------")
# Working with empty lists
shopping_cart = ['Tomato']
if shopping_cart:
    for item in shopping_cart:
        print("Adding " + item + ' to your cart.')
    print("your order is complete!")
else:
    print("You must select an intem before proceeding!")

print("-----------------------------")
# Multiple lists
in_stock = ['tomato', 'cheese', 'butter', 'ham']
shopping_cart = ['bread', 'cheese', 'butter', 'ham']

for item in shopping_cart:
    if item in in_stock:
        print("Adding " + item + " to your order!")
    else:
        print("Sorry, " + item + " is not available!")
print("Your order is complete!")

print("-----------------------------")
# Dictionaries
book_1 = {'Author': 'Tommy Broekman', 'price': 10}
print(book_1['Author'])
print(book_1['price'])

print("-----------------------------")
# Python in operator
terms = {'Variable': 'Represent or refers to a value stored in memory',
         'String': 'A sequence of characters'}
if 'Float' in terms:
    print("I know what Float means")
else:
    print("I do not know what Float is")
print(terms['Variable'])

terms_2 = {}
terms_2['Variable'] = 'Represent or refers to a value stored in memory'
print(terms_2)
terms_2['Integer'] = 'A whole number'
print(terms_2)
print(terms_2['Integer'])

print("-----------------------------")
# Get method
terms_3 = {'Integer': 'A whole number'}
print(terms_3.get('Integer'))
print(terms_3.get('float', 'Not in the dictionary'))
