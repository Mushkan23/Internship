import database
MENU_PROMPT = '''**Coffee Bean App**

Please choose one of  the option:

1. Add a new bean
2. see all beans
3. find a beans by name
4. see which preparation is best for a bean
5. Exit
Your Selection: ''';

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) !="5":
        if user_input == 1:
            name =input("Enter the name: ")
            method = input("Enter how you prepare: ")
            rating = int(input("Enter the rating score (0-100): "))

            database.add_bean(connection, name,method,rating)

        elif user_input == 2:
            beans = database.get_all_beans(connection)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

        elif user_input == 3:
            name =input("Enter the bean name: ")
            beans = database.get_beans_by_name(connection,name)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

        elif user_input == 4:
            pass
        else:
            print('Invalid input, please try again')

menu()