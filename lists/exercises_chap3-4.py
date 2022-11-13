# 4-8 Cubes:
cubes = []
for num in range(1, 11):
    print(num ** 3)
    cubes.append(num ** 3)
print(f"This is our new list: {cubes}")

print('==================================')

# 4-9 List comprehension - short form,
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)
#
# cubes = []
# for num in range(1, 11):
#     cubes.append(num**3)

print("----- 4-1 ----")
pizzas = ['margherita', 'capriciosa', 'funghi']
for pizza in pizzas:
    print(pizza.title())
print('----------------------------------------------')
for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')
print('----------------------------------------------')
for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')
print('I absolutely adore pizza!!.\n')
print('----------------------------------------------')

print("----- 4-2 ----")
animals = ['dog', 'cat', 'horse']

for animal in animals:
    print(f' a {animal.title()} would make a great pet')
print(f'any of these animals would make a great pet')

# Summary: must-know on List (so far)
# list new, update the value, add value, delete value from the list
# sorting the list : list.sort(),list.sort(reverse=true),  newList = sorted(list), newList = sorted(list, reverse=true)
# simple for loop with list, list with range(start, stop, step), scope of the for loop
# Slicing the list (list[0:3], copy_list = list[:] )
