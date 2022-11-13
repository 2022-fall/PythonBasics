# CHAPTER 6: Looping Through a Dictionary
# Dictionaries keys, only values, key and value

person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}

print("# default case, looping through keys only ----------")
for key in person1:
    print('key in this iteration is: ', key)
    print('value in this iteration is: ', person1[key])

print("# looping through keys only, keys() -----------------")
for key in person1.keys():
    print('key in this iteration is: ', key)
    print('value in this iteration is: ', person1[key])

print("# looping through values only , values()---------------")
for value in person1.values():
    print('value in this iteration is ', value)

print("# looping through keys and values (mostly used), items() -----------------")
for key, value in person1.items():
    print('key in this iteration is: ', key)
    print('value in this iteration is: ', value)

# Exercises 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers_countries = {'nile': 'egypt',
                    'amazon': 'brazil',
                    'volga': 'russia',
                    'mississippi': 'usa',
                    'thames': 'uk'}
print("##### # Exercises 6-5. -----------------------")
print("# 1.Use a loop to print a sentence about each river")
for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("# 2.Use a loop to print the name of each river included in the dictionary.")
for river in rivers_countries.keys():
    print(f"river : {river.title()}.")

print("# 3.Use a loop to print the name of each country included in the dictionary.")
for country in rivers_countries.values():
    print(f"Country: {country.title()}.")

# H/W: 6-4, 6-5
