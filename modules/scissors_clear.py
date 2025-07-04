import random
import sys

from rich import print


def scissorsClear():
    playerchoice = input("Choose rock(1), paper(2), or scissors(3): ")
    try:
        playerchoice = int(playerchoice)
    except ValueError:
        sys.exit("Invalid type, please enter a number")

    if playerchoice < 1 or playerchoice > 3:
        sys.exit("Invalid choice")

    computerchoice = random.randint(1, 3)
    computerchoice = int(computerchoice)

    print("Player choice: ", playerchoice)
    print("Computer choice: ", computerchoice)

    if playerchoice == computerchoice:
        print("[blue]It's a tie!")
    elif playerchoice == 1 and computerchoice == 3:
        print("[green]Player wins!")
    elif playerchoice == 2 and computerchoice == 1:
        print("[green]Player wins!")
    elif playerchoice == 3 and computerchoice == 2:
        print("[green]Player wins!")
    else:
        print("[red]Computer wins!")
