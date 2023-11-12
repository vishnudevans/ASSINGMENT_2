# list with EVEN and ODD numbers
list = [1,2,3,4,5,6,7,8,9,10]

# print original list
print("Original list:")
print(list)

# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
for i in list:
    if i % 2 == 0:
        list.remove(i)

# print list after removing EVEN elements
print("List after removing EVEN numbers:")
print(list)
