# This is comment line , ctrl + /

print("Hello World!")
# print(a) - you will get NameError when you try to use variable before defining
# variable - storage while code runs, varname = value
# note: name should be
# 1. should not start with numbers
# 2. starts with lower case letter
a = 45  # number, integer (data type)
b = 6.87  # number, float, double (data type)
name = 'john doe'  # text , i.e. string (data type)
msg = "hello, this is my first coding practice!!!!"  # string

print(a)
print(b)
print(name)
print(msg)

a = 90
print(a)

a = 1000
print(a)
print(a, b, name, msg)
print('I am printing the variables', a, b, name, msg)
# PEP8 - python best practices (in coding) guidelines
print('summing the a and b', a + b)
# print(a + name)
print(name + ': ' + msg)

# 10/9/2022
a = a + 1
#  a += 1
a = a - 1
#  a -= 1
print(a)

# length_of_persons_name - snake case
# print(c) you will get NameError since this is not defined yet
print("####### useful functions for strings ############")
print("# title(), upper(), lower(), isLower(), isUpper(), isdigit()")
print('name before title', name)
print('name with title:', name.title())
print('name after title', name)
print('using is lower: ', name.islower())
print("# concatenation ")
print("my message: " + name + ', ' + msg)
print("my message: " + name.title() + ', ' + msg.upper())
# whitespace characters : \t, \n, '     '
print("Special characters : \\t \\n")
print("my message:\t\t\t" + name.title() + ',\n\n\n\t\t\t\t' + msg.upper())
print("Message to everyone:\n\t\t\tplease have fun!!".upper())
# SyntaxError, NameError, ..
# strip(), rstrip(), lstrip() , works with string values
locatn = '              \thawai\n\t'
print(locatn)
print('my wedding venue: ' + locatn.strip().upper() + ' islands')
# print('my wedding venue: ' + a.strip().upper()+' islands')
print("##### working with numbers #####################")
num1 = 3
num2 = 8
print("addition: :", num1 + num2)
print("subtraction: ", num1 - num2)
print("multiplication: ", num1 * num2)
print("division: ", num1 / num2)
print("exponent: ", num1 ** 2)
print("floor division: ", 30 // num1)  # how many num1(3) in 30
print("modulo: ", 20 % num1)  # 20 = 3*b + 2

# find odd numbers 20-50 -> 21 (21=2*10 + 1), 23 (23=2*11 + 1)
# if n%2 return 1 the n is odd number (pseudocode)
# if n%2 return 0 the n is even number (pseudocode)
print("### str(expression) , converts expression to a string")
print("addition: :" + str(num1 + num2))
print("### int(expression) , converts expression to a integer, if possible")
num3 = '456'  # this is a string data type
num4 = 45.7566  # this is a float data type, int(num4) will get only int part of it
print('addition with num3: ', num1 + int(num3))
print('converted to int:', int(num4))
status = True  # this is a boolean value (True/False)
newstat = False

# Summary:
# variable (naming), values string, int, float, double, boolean(True, False), Primitive data type
# string : concatenate, upper(), title(), lower(), str(), '\t', '\n'
# numbers: int, float/double, int(), +, -, *, /, **, //, %
