# Chapter 10: Files and Exceptions

# with open('filepath') as aliasNameForTheFile:
#     line1 = aliasNameForTheFile.readline()
#     line2 = aliasNameForTheFile.readline()
#     line3 = aliasNameForTheFile.readline()
#
#     all_lines = aliasNameForTheFile.readlines(), list of values
#
#     file_content = aliasNameForTheFile.read()
#
#     # aliasNameForTheFile.close() , no need to close when you read a file starting 'with'
#
filepath1 = '../data/products.txt'
filepath2 = '../data/sample.txt'
filepath = 'c:/dev/basics/data/products.txt'

print("************ READ file *****************")
with open(filepath) as prod_list:
    contents = prod_list.read()
    print("Contents of the file:\n", contents)

with open(filepath, 'r') as prod_list:
    print("now we are trying to loop through the contents")
    all_lines = prod_list.readlines()
    print(all_lines)
print('printing the line5:', all_lines[4])

for line in all_lines:
    print(line)

print("************ WRITE file appending new content *****************")
with open(filepath, 'a') as prod_list:
    prod_list.write('playstation 5\n')
    prod_list.write('Learning Python book\n')
    prod_list.write('First head to Selenium book\n')
    # check the file content

# print("************ WRITE file deleting the old content *****************")
# with open(filepath, 'w') as prod_list:
#     prod_list.write('spiderman jacket\n')
#     prod_list.write('batman mask\n')
#     prod_list.write('smart tv samsung 70"\n')
#     # check the file content

# H/W : 10-3, 10-4, 10-5
