# Remove empty strings from the list of strings
#           list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

while "" in list1:
    list1.remove("")

print(list1)


# output:
# ['Mike', 'Emma', 'Kelly', 'Brad']