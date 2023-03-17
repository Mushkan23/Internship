rock = 0
paper = 1
scissor = 2

player1 = int(input("Enter a value : "))
player2 = int(input("Enter the value: "))

if (player1 == rock or player2 == paper):
    print("Player1 is winner")
 
elif (player1 == paper or player2 == scissor):
    print("Player2 is losser.")
elif (player1 == scissor or player2 == rock):
    print("player2 is winner.")


while True:
    print("Enter quit to quit or play more game.")
    cmd = input("Please enter your command for further... : ")

    if cmd == "quit":
        break;
    else:
        print("error")
"""
start = 0

match start:
    case 0 :
        print ("")
"""