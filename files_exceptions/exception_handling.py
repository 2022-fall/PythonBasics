# Python uses special objects called exceptions to manage errors that arise
# during a program’s execution.
import yaml

try:
    # usual code to execute
    print('executing a code in try block')
    # print(5/0)

    filepath1 = '../data/credentials.yml'

    # functions/steps
    with open(filepath1, "r") as stream:
        credentials = yaml.safe_load(stream)

    print("** try block execution completed :) ****")
except ZeroDivisionError as err:
    # executes only when ZeroDivisionError happens
    print("You can not divide by 0!!!!!!!!!!!")
    print('printing the standard error:', err)
except FileNotFoundError:
    # executes only when FileNotFoundError happens
    print("ops, no file no code execution")
except Exception as err:
    print('printing the standard error:', err)
finally:  # you dont have to use this block
    # this block will be executed regardless exceptions happens or not
    print("clean up and close the browser.")

# print('executing a code in try block')
# print(5 / 0)
# print("** try block execution completed :) ****")

print("Execution completed !!!")

# H/W : 10-8