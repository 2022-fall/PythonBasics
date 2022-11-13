# Chapter 4: Slicing the list
pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'funghi', 'sicilian']

print(pizzas[0:3])
print("**********")
# for pizza in pizzas[2:5]: # includes index 2, 3, 4
# print(f"we have {pizza} pizza today")
# for pizza in pizzas[3:]: # means from 3rd index to the last index
#     print(f"we have {pizza} pizza today")
# for pizza in pizzas[0:3]: # includes index 0, 1, 2
# print(f"we have {pizza} pizza today")
for pizza in pizzas[:3]:  # means from beginning of the list to third element
    print(f"we have {pizza} pizza today")

print("------------ copy the list --------------")
new_pizzas = pizzas  # creates the new reference list to the same list
copy_pizzas = pizzas[:]  # creates the totally independent list (copy_pizzas)
print(f"Lists before updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}")
pizzas.append('cheese steak')
new_pizzas.append('mushroom')
copy_pizzas.append('veggie')
copy_pizzas.append('granma')
print(f"Lists after updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}")

print("# Tuples - immutable data structure, can not be modified ==============")

animals = ('dog', 'cat', 'horse')

dog_index = animals.index('dog')
print(f'index of the dog element in the tuple: {dog_index}')
sorted_animals = sorted(animals)
print(f'sorted animals: {sorted_animals}')
for animal in animals[0:2]:
    print(f'each animal : {animal}')

# creating a new list from tuple
list_animals = list(animals)
print(list_animals)
print(animals)

# H/W: 4-10, 4-11, 4-12
# styling the code: ctrl + alt + l (pycharm shortcuts)
