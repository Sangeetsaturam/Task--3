# Merge following two Python dictionaries into one
#    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#     dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
def merge(d1, d2):
    result = {**d1, **d2}
    return result


d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

d3 = merge(d1, d2)

print(d3)

# output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}