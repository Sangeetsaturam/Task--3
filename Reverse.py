# Reverse a given list in Python
#     list1 = [100, 200, 300, 400, 500]
#     Expected output: [500, 400, 300, 200, 100]
def reversing_list(List):
    list.reverse()
    return list

input_list = input("Enter list:")
list  = input_list.split(",")
print("REVERSE LIST:")
for i in list:
    print(i)


print(reversing_list(list))    

#Output:
# Enter list:100, 200, 300, 400, 500
# REVERSE LIST:
# 100
#  200
#  300
#  400
#  500
# [' 500', ' 400', ' 300', ' 200', '100']