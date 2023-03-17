'''arr1 = ([1,12,41,20])
print(arr1[1])
print(arr1[3])
arr1.insert(2,32)
print(arr1)
arr1.remove(20)
print(arr1)
print(arr1.index(32))
arr1[3]=11
print(arr1)'''

arr = [[1,5,6,32],[4,45,8,31],[74,54,2,61]]
for i in arr:
    for r in i:
        print(r, end=' ')
    print()

arr.insert(2,[21,0,4,32])
print(arr)
del arr[1][2]
print(arr)
