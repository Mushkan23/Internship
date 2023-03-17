# Given two integer numbers return their product only if the product is equal to or lower than 1000, 
#else return their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
ans = num1 * num2
if (ans <= 1000):
    print (ans)
else:
    print(num1 + num2)

