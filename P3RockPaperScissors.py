# Chinasa "Chi-Chi" Iheanacho
choices=["R","r","P","p","S","s"]
print('Welcome to Rock Paper Scissors!')
while True:
    num_games=int(input("How many games would you like to play??"))
    if num_games % 2 ==0:
        print("Please enter an odd number.")
        continue
    else:
        print("Great! Let's play {} games!".format(num_games))
        break
print("Let's Go!!")
for game in range(num_games):
    print("\nGame {}!".format(game+1))
    while True:
        user=input("Please choose from the following:\nR-Rock\nP-Paper\nS-Scissors")
        num_gamez = 0
        if user not in choices:
            print("Invalid Entry. Please try again.")
            continue
        else:
            num_gamez=num_gamez+1
            if user == "R":
                print("The computer chose Paper. You lose.")
                break
            elif user == "r":
                print("The computer chose Paper. You lose.")
                break
            elif user == "P":
                print('The computer chose Scissors.You lose.')
                break
            elif user =="p":
                print('The computer chose Scissors.You lose.')
                break
            elif user == "S":
                print("The computer chose Rock. You lose.")
                break
            else:
                print("The computer chose Rock. You lose.")
                break
print("\nThank you for playing!")
print("The computer won {} games!".format(num_games))
print("You won 0 games!")
print("Computer won! Better luck next time!")
