# Parse the following JSON to get all the values of a key ‘name’ within an array
# [
# {
# "id":1,
# "name":"name1",
# "color":[
# "red",
# "green"
# ]
# },
# { 
# "id":2,
# "name":"name2",
# "color":[
# "pink",
# "yellow"
# ]
# }
# ]

import json

path = input("Enter the Path : ")

try:
    file = open(path,"r")
    info = file.read()

    value = []
    value = json.loads(info)

    List = [item.get('name') for item in value]
    print(List)

except:
    print("File open failure")

# output:
# Enter the Path : H:\Task-3\history.py
# File open failure