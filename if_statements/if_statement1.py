# CHAPTER 5: IF STATEMENTS

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if (car == 'bmw') and (5 == 3 + 2) or ('hello' == 'HELLO'):
        print(f'car value was bmw so we are doing Upper() print: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() print: {car.title()}')

# and    results of the expression: car == 'bmw' and 2 == 2
# true + true = true
# true + false = false
# false + true = false
# false + false = false

# or
# true + true = true
# true + false = true
# false + true = true
# false + false = false


# car = 'tesla'  # assigning the 'tesla' as a value of car variable
# car == 'bmw'  # comparing the value of car value with 'bmw' string, this expression results in True/False

# Expressions: returns True/False
name = 'john'
password = 'johna53sr56waew2-@@@@@@@@@@e44444-38099232a465sdf64as'
num = 45.55
is_good = True
friends = []

# name.lower() == 'jane'  # False, checking if the value of the name var is equal to 'jane'
# name > 'abc'  # A-Z (a, b, ...j..), True
# num == 45  # False
# num < 45  # False
# num <= 45  # False
# num >= 45  # True
# num > 45  # True
# is_good == False  # False
# name.lower() != 'jane'  # True, Jane, jAne, JANE, jaNe, jaNE

# Multiple conditions with AND/OR
# name == 'john' and num > 45  # True and True >> True
# name == 'john' and num < 45  # True and False >> False
#
# name == 'john' or num > 45  # True or True >> True
# name == 'john' or num < 45  # True or False >> True
# name == 'jane' or num < 45  # False or False >> False

if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this mean it is a empty list')
# friends expression returned false, this mean it is a empty list

friends = ['jane']
if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this mean it is a empty list')
# friends is not empty list
# cars = ['audi', 'bmw', 'subaru', 'toyota']
print("---------------------------------------")
print(cars)
if 'tesla' in cars:
    print(f'cars list includes tesla')
else:
    print(f'tesla is not in the cars list.')

# H/W Exercise 5-1, 5-2
