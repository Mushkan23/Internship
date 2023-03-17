import collections
dict1 = {'name':'mon','day':'wednesday','contact': 5848596}
dict2 = {'name':'mon','day':'wednesday','contact': 5848596}
m = collections.ChainMap(dict1,dict2)
print(m.maps)
print('Keys = {}',format(list(m.keys())))
print('Value = {}',format(list(m.values())))
print()