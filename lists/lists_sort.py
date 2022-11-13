# Chapter 3 : Lists sort

cars = ['tesla', 'bmw', 'moskvich', 'lexus']
print("Permanent sorting - sort().")
print("List before sorting: ", cars)
cars.sort()  # sorting in ascending order
print("List after sorting: ", cars)

names = ['john', 'jane', 'mark']
print("List before sorting: ", names)
names.sort(reverse=True)  # sorting in descending order
print("List after sorting: ", names)

print("Sorting temporarily - sorted()")
car_models = ['model x', '550 xi', 'corolla', 'camry']
print("Car models before sorting: ", car_models)
sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True)

print("Car models after sorting: ", car_models)
print("sorted Car models after sorting in ascending order: ", sorted_car_models_asc)
print("sorted Car models after sorting in descending order: ", sorted_car_models_desc)

print("Reversing(permanent) the list without sorting: ")
nums = [6, 3, 9, 7, 10]
print("list before reversing: ", nums)
nums.reverse()
print("list after reversing: ", nums)

# example
# unsorted list of number 10mln nums = [.......]
# print largest and smallest number
# nums.sort()
# print('smallest number: ', nums[0])
# print('largest number: ', nums[-1])

print("# number of elements in the list with len()")
print('number of elements in the nums list: ', len(nums))
print('number of elements in the names list: ', len(names))
print('number of elements in the cars list: ', len(cars))
# H/W: 3-8, 3-9, 3-10

