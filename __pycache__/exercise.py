"""print("Welcome to the KBC.")

print("Who is the national bird of India ?")

ans = input("Enter your solution : ")
if (ans == 'peacock'):
    print("Correct.")
else:
    print("Incorrect answer.")

print("Current president of India? ")
ans = input("Enter your solution : ")
if (ans == 'munmun'):
    print("Correct.")
else:
    print("Incorrect answer.")

print("T20 cricket best player in 2022")
ans = input("Enter your solution : ")
if (ans == 'Rohit sharma'):
    print("Correct.")
else:
    print("Incorrect answer.")
    """

#Next solutions.

ques = ['Who is the national bird of India ?','Current president of India?','find missing letter ph_ne']
ans = ['peacock','murmur','o']
score = 0;
for i in range(3):
    print(ques[i])
    answer = input("Enter the solution: ")
    if answer == ans[i]:
            #print("Corect")
            score += 1
    else:
        print("The soltuin is Incorrect.")
        break
match score:
    case 0 :
        print("oops!! you win nothing.")
    case 1 :
        print("well played!! you won Rs.50000")
    case 2 :
        print("Wow you win 1lakh rupees....")
    case 3 :
        print("Yeah!!well 50 lakh.")



   