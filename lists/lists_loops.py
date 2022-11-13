# Chapter 4: Looping through the list

places = ['hawai', 'paris', 'bahamas', 'iceland', 'canada']
# Loops - executing the code repetitively (what to loop through, how many times)
print("Looping through entire list: ")
# for var_each_element in list_name:
#     print('lines of code to be repeated')

# sample for loop in Java to see the difference with Python loop
# for a in places{
#     print(a)
# }

print("we are looping through places")
for place in places:
    # comment line
    # print(place)
    print(f"I want to visit {place.title()} next summer")
    print(f"How far is the {place.title()} from new york?")

print("ohhhh, I need to convince my wife now.")
# print(f"How far is the {place.title()} from new york?") this is wrongly indented

# H/W: 4-1, 4-2

print("# Working with list of numbers, range() functions")
# range(5) -> 0, 1, 2, 3, 4
# range(2, 6) -> 2, 3, 4, 5(6-1)
# range(4, 16, 3) -> 4, 7, 10, 13
print(range(5))
print(list(range(5)))

# nums = list(range(5))
# for num in nums:
#     print(f'Each number : {num}')

for num in range(5):
    print(f'Each number : {num}')
print("================================")

for num in range(2, 6):
    print(f'Each number : {num}')
print("================================")

for num in range(4, 16, 3):
    print(f'Each number : {num}')

print("# Problem solving:")
print("# problem1: list all number between 21 and 36 that can be divided by 4.")
for num in range(24, 37, 4):
    print(f'each number: {num}')

print("# problem2: create a list of the squares of numbers between 25 and 30.")
num_squares = []
for num in range(25, 31):
    # print(f'num = {num} and square is: {num**2}')
    num_squares.append(num**2)
print("final list of squares:", num_squares)

for num in range(5, -10, -2):
    print(num)
print("*****************************")
nums = [4, 2, 9, 10]
print(f'sum of the nums: {sum(nums)}')
sum = 0
for num in nums:
    sum = sum + num
print(sum)

# H/W : 4-3 to 4-9
# Next class agenda: Working with Part of a List


