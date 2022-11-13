# CHAPTER 5: ELIF STATEMENTS
# else if >> elif

# if expression1:
#     code to execute when expression1 is True
#     code to execute when expression1 is True
#     code to execute when expression1 is True
#     code to execute when expression1 is True
# elif expression2:
#     code to execute when expression2 is True
# elif expression3:
#     code to execute when expression3 is True
# elif expression4:
#     code to execute when expression4 is True
# else:
#     code to execute when none of above expressions are True
# input(prompt_message) - this asks the user to input and return a string (always)

# Problem: if older than 25 print don't drink and drive, from 17-25 get DL but you will pay more to insurance,
# age is less than 0-17 then you can not get DL,

print("Hello!! Your awesome program is starting ...")
for i in range(5):
    print(f'Iteration # :{i}')
    # age = 30
    # age = input("Please enter your age: ")
    # age = int(age)
    # break
    age = int(input("Please enter your age: "))
    if 0 < age < 17:
        print('Sorry, you still young, you can not get DL, just play PlayStation.')
    elif 17 <= age < 25:
        print('Good, you are eligible to get DL, but you will pay more to Insurance')
        # break  # this will stop the for loop
        # print('after break message')   # this code is not reachable if you have break
    elif 25 <= age < 120:
        print("Great, if you have DL, please Do not Drink and Drive, Do not Smoke and Drive.")
    else:
        print("Please enter valid number for age!")

# H/w: from 5-3 to 5-7
# H/w: from 5-8 to 5-11

# Interview questions:
# Problem 1:
# if number dividable by 3 print "Fuzz", if number dividable by 5 then print "Buzz,
#       if number dividable by 3 and 5 then print "FuzzBuzz"
n = 3
if n % 3 == 0:
    print('dividable by 3')
else:
    print('this is not dividable by 3')

# Problem 2:
# how can you loot through the list of numbers and check that number 5 is in the list,
# when you find 5 then stop the loop print 'Hoooraa'
# Hint: use 'break' keyword to stop the loop
