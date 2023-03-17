#print(pow(2,4))

#list = (12,84,1,32,26,20)
#print(sorted(list,reverse=True))

#num = (1,5,2,1)
#print(sum(num))

"""def num():
    return 5+7
res = num
print(callable(res))"""

"""tup = (4,12,3,2)
for i in reversed(tup):
    print (i, end =' ')"""

arr = [1,23,51,2,31]

def myfunc(x):
    if x > 18:
        return True
    else:
        return False
res = filter(myfunc,arr)
for x in res:
    print(x)
