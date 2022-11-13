# scenarios
from while_loop import fuzz_buzz as fb  # this imports only one function
from while_loop import *
from functions.functions_return import *

# import while_loop , we need to mention module name with each function use
# while_loop.fuzz_buzz()
print("# execution of functions from while_loop.py")
fb() # executing fuzz_buzz() functions with alias name.
while_loop_increment()
while_loop_decrement()

print("# execution of functions from functions_returns.py")
print('Result of the function: ', build_full_name('john', 'doe'))
person2 = build_full_name('jane', 'doe')
print('Person2: ', person2)

print('----- 8-6. -----------------------------')
print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))


# h/w: 8-4, 8-5
# H/W: 8-7, 8-8
# H/W: 8-15

from functions.exercises_chp8 import *

print_models(unprinted_designs, completed_models)
