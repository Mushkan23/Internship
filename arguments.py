#def average(a,b,c):
   # print ("The average is : " , (a + b + c)/2)
#average(4,7,1)

#def average(a,b):
 #   print("The average is : " , a + b/2)
#average(b=1,a=2)

#arguments as a tuple
"""def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("The average is : ", sum / len(numbers))

average(4,2,6,8)"""

#arguments as a dictionary

def name(**name):
    print(type(name))
    print("The full name iis : ", name["fname"], name["lname"], name["age"])
name(fname = "mushkan",lname = "singh", age = 21)
