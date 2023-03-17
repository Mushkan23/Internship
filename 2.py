#Write a program to iterate the first 10 numbers and in each iteration, 
#print the sum of the current and previous number.

previous = 0
for i in range(1,11):
    sum = previous + i
    print (sum)
    previous = i                  #i is an current value
