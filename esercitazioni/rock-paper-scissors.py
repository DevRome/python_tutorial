# sasso carta forbice
import random 

options = ("rock", "paper", "scissors")


is_running = True
while is_running:

    player = None
    computer = random.choice(options)

    # finché la scelta del player non coincide con le options a disposizione: 
    while player not in options:
        player = input("Enter a choice: rock, paper, scissors: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors": print("You win!")
    elif player == "paper" and computer == "rock": print("You win!")
    elif player == "scissors" and computer == "paper": print("You win!")
    else: print("You loose!")

    if input("Play again? (y / n): ").lower() == "n":
        break

print("Thanks for playing")
