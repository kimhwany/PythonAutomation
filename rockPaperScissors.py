import random

print('Game Rules:\n'
    + " - Rock Crushes Scissors\n"
    + " - Scissors Cuts Paper\n"
    + " - Paper Covers Rock \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice: "))

    # looping until user enters valid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please: '))

    # Extract the corresponding move from choice (integer)
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Ouput User's Choice
    print('User choice is:', choice_name)
    print('\nNow it\'s the Computer\'s Turn....')

    # Computer chooses randomly any number
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name, '\n')
    print(choice_name, 'Vs', comp_choice_name)

    # Determine Result
    if choice == comp_choice:
        print("~~~ It's a tie ~~~")
    elif ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
        print("~~~ Computer wins ~~~")
    else:
        print("~~~ YOU WIN ~~~")

    # Continue or repeat!
    print("Want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# Exit:
print("Thanks for playing")