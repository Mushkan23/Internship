#Program 1

"""import operator
import time
l1 = [4,8,12,3,2]
l2 = [1,15,32,4,3]
t1 = time.time()
a,b,c,d,e = map(operator.mul,l1,l2)
t2 = time.time()

print("The result is : ", a,b,c,d,e)
print("The total time taken  by function : %.12f " %(t2-t1))

# solving using loop

t1 = time.time()

for i  in range(5):
    print("solution : " , (l1[i] * l2[i]))
t2 = time.time()
t = ("The time taken by loop is : %.6f " %( t2 - t1 ))
"""

#Program 2 (infinite iterator)

"""import itertools
for i in itertools.count(5,5):
    if i == 55:
        break
    else:
        print(i,end = " ") """

#Program 3 product()

"""from itertools import product
print(list(product(['good','book'],repeat = 2)))
print()
print(list(product([1,5],'ab')))
print() """

#Program 4 permutations()

"""from itertools import permutations
print(list(permutations(['AB',2])))
print()
print(list(permutations('hey')))
print()  """

#Program 5 combinations()

"""from itertools import combinations
from itertools import combinations_with_replacement

print(list(combinations(["Hey",3],5)))
print()

#Program 6 accumulate()
import itertools
from itertools import accumulate
import operator
l1 = [1,3,5,2]
print(list(itertools.accumulate(l1)))
print(list(itertools.accumulate([l1],operator.mul)))"""

#Program 6 chain()

"""import itertools
l1 = [1,12,5,32]
l2 = [14,24,32,2]
l3 = [7,84,6,32]
print(list(itertools.chain(l1,l2,l3)))"""





