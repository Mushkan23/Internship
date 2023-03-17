while True:
    try:
        num = int(input("Enter a num: "))
    except ValueError:
        print("The entered value is 42.")
        continue
    if num != 42:
        print(num)
    else:
        print("Enetered number is 42.")
        break;

