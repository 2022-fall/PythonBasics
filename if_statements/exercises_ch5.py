# H/W Exercise 5-1, 5-2

# [on_true] if [expression] else [on_false]
# car = 'subaru'
# print("is car =='subaru'? i predict true.")
# print(car == 'subaru')
#
# car = 'bmw'
# print("is car =='subaru'? i predict false.")
# print(car == 'subaru')
# print(45 == 233)

# 5-5
alien_color = ['green', 'yellow', 'red', 'black']
# for color in alien_color:
#     if color == "green":
#         print(f'Player who shot {color} alien, 5 points shooting an alien')
#     elif color == "yellow":
#         print(F"player who shot {color} alien,earned 10 points")
#     elif color == "red":
#         print(F"player who shot {color} alien, earned 15 points")
#     else:
#         print(f'You are loser, wheee, your color {color.upper()}!!!')
print('-----------------------------------------------------')

age = 0
# for i in range(3):
#     age = int(input('enter your age : '))

print("---------------------")

# user_names = ['Admin', 'john', 23, '']
user_names = []
# if list is empty:
if not user_names:
    print('We need to find some users!')
else:
    for user in user_names:
        user = str(user)
        if user.lower() == "admin":
            print(f"$$$$$$  Hello admin, Would you like to see status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")

print("=============== FUZZ BUZZ ======================")
num = 30
if num % 3 == 0:
    print('Fuzz')
if num % 5 == 0:
    print('Buzz')
if num % 3 == 0 and num % 5 == 0:
    print('FuzzBuzz')

# num = int(input('Please enter a number'))
num = 3
if num != 0:
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print('This is not dividable by 3 or 5')
else:
    print("please enter different number than 0")

# Problem 2:
# how can you loot through the list of numbers and check that number 5 is in the list,
# when you find 5 then stop the loop print 'Hoooraa'
# Hint: use 'break' keyword to stop the loop
random_list = [4, 92, 20, 3, 5, 13, 22, 444]
for number in random_list:
    print(number)
    if number == 5:
        print(f'welcome {number} ')
        break
print('my awesome application is completed!!')

nums = [4, 92, 20, 3, 5, 13, 22, 444]
for num in nums:
    if num == 5:
        print("Hooraah")
    elif num >= 5:
        break
