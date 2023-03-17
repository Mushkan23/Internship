#Write a program to accept a string from the user and display characters that are 
#present at an even index number.

input = input("Enter the letter: ")
length = len(input)

for i in range(0,length,2):
    print(input[i])