# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
#     list1 = [10, 20, 30, 40]
#     list2 = [100, 200, 300, 400]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for l1, l2 in zip(list1, list2[::-1]):
    print(l1, l2)

# output:
# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
#     list1 = [10, 20, 30, 40]
#     list2 = [100, 200, 300, 400]
