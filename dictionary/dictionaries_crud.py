# Chapter 6: Dictionary - mutable data structure (key-value pair)
# CRUD ( create, read, update, delete)
print("####### 1. creating the empty dictionary (C)")
person0 = {}  # empty dictionary, so python knows person2 is dictionary object
person2 = dict()  # empty dictionary, so python knows person2 is dictionary object
languages_list = ['eng', 'ru', 'esp', 'marsian']
person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny',
           'cars': ['audi', 'bmw', 'subaru', 'toyota'],  # independent value
           'languages': languages_list}   # two-way reference to the list (connected)

print("#### 2. accessing the values (R)")
# person1['name']
print(f"getting name of person1 '{person1['name']}' ...")
print(f"getting age of person1 '{person1['age']}' ...")

print("#### 3. adding/updating key value pair to the dictionary (U)")
print('Original dictionary: ', person1)
person1['phone'] = '(123) 456-7891'
# phone does not exist in keys in person1 dictionary, so it adds new key-value pair (element)
print('Updated with new key dictionary: ', person1)
print("updating the value of 'age' in the person1 dictionary....")
person1['age'] = 30  # pay attention that you are mentioning the existing key
print('Updated age in person1 dictionary: ', person1)

print("updating the list value inside the dictionary...")
# cars[0] = 'merc'
person1['cars'][0] = 'merc'
print('Updated list (audi to merc) in person1 dictionary: ', person1)

print("updating the list languages_list (marsian to ger)....")
languages_list[3] = 'ger'
print('updated list: ', languages_list)
print('dictionary: ', person1)

print("updating the value of the list in the dictionary....")
person1['languages'][2] = 'french'
print('updated list: ', languages_list)
print('dictionary: ', person1)

# copying the list to a value of the dictionary (independent values)
# languages_list = ['eng', 'ru', 'esp', 'marsian']
# person1['languages'] = languages_list[:]
# print(person1)

print("####### 4. Delete key-value pair from the Dictionary (D) ")
print("Deleting the location key-value pair from person1....")
del person1['location']
print("updated person1 dictionary: ", person1)
person1['age'] = None  # no value, like Null in sql
print("updated age in person1 dictionary: ", person1)

# exercise: 6-2 Favourite Numbers
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
# Print each person’s name and their favorite number.
print(f"Nicole's favourite number is : {fav_nums['nicole']}")
print(f"Alex's favourite number is : {fav_nums['alex']}")
print(f"Yulia's favourite number is : {fav_nums['yulia']}")

# H/w: 6-1, 6-3
