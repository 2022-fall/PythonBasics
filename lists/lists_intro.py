# Chapter 3: Data structure - storage to hold multiple values, manage (create, add, update, remove)
# Python Data structures: Lists, Dictionary, (Set, Tuple)
# [4, 10, 6]  ['john', 'mark', 'jane'] [True, False, True]
# list, Dictionary is considered mutable object (we can make a change in the list)
# Tuple - immutable DS, can not add or remove values after defining

# Pycharm shortcut: ctrl + alt + l - autoformat the file

friends = []  # empty list
players = list()  # creates empty list

nums = [4, 10, 6]
names = ['john', 'marka', 'jane']
bool_values = [True, False, True]
print(nums)
print(names)
# add elements, remove, update, read through values (access each value)

print('Hi, ', names[1].title())
print('Hi, ', names[0].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[-2].title())
print('Hi, ', names[-3])
# print('Hi, ', names[3].title()) # IndexError: list index out of range
print("##### adding the elements to the list ######")
# listname.append(newvalue) - adds newvalue to the end of the list
names.append("alex")
print(names)
# listname.insert(index, value) - puts the 'value' to the 'index',
# other values shifter to the left, all indexes will be updated
names.insert(2, "araz")
print(names)
print("# updating the last element of the list 'alex'->'benny'")
names[-1] = 'benny'
print(names)
print("removing the values from the list--------")
print("# remove element by index : del listname[index]. removing 'jane' ")
del names[3]
print(names)
print("# remove element by index : listname.pop() removing last in the list")
deleted_name = names.pop()  # returns the value to the program after deleting
print(names)
names.pop(0)
print(names)
print('we deleted following names: ', deleted_name)
print("# remove element by value: listname.remove(value) ")
names.remove('araz')  # ValueError: list.remove(x): x not in list
print(names)

#### 10/16/2022
# Exercises: 3-4
guests = ['akmal', 'said', 'lenur']
print(f'Hello {guests[0].title()}, Welcome to the dinner')
print(guests[1], ',' 'Welcome to the dinner')
# to put them in 1 string
# Hello Akmal, Welcome to the party
print('Hello ' + guests[0] + ', Welcome to the party')
print('Hello ' + guests[0].title() + ', Welcome to the party')
print(f'Hello {guests[0].title()}, Welcome to the party')
removed_guest = guests.pop(1)
# removed_guest2 = guests.remove('akmal') # this will remove akmal but will not assign value to a var
# a= 'said' this is the same thing as line 57
print(f'{removed_guest}, cant make it to the party')
# print(f'{removed_guest2}, cant make it to the party')
print(guests)
guests.append('max')

print(guests)
print(f'Hello {guests[0].title()}, Welcome to the party')
print(f'Hello {guests[1].title()}, Welcome to the party')
# print(f'Hello {guests[2].title()}, Welcome to the party')

# HW: 3-6, 3-7
# removed_guest = guests.pop(1)
#
# 1. removes the element by index 1
# 2. returns the removed value
# 3. assigns saved to a variable
# removed_guest = guests.remove('akmal')
# 1. removes the element 'akmal'
# 2. Returns None (null)