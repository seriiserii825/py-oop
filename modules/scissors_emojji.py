import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def scissorsEmojji():
    playerchoice = input("🫠 Choose rock(1), paper(2), or scissors(3): ")
    try:
        playerchoice = int(playerchoice)
    except ValueError:
        sys.exit("👺 Invalid type, please enter a number")

    if playerchoice < 1 or playerchoice > 3:
        sys.exit("🧨 Invalid choice")

    computerchoice = random.randint(1, 3)
    computerchoice = int(computerchoice)

    print("Player choice: ", RPS(playerchoice).name)
    print("Computer choice: ", RPS(computerchoice).name)

    if playerchoice == computerchoice:
        print("🟰 It's a tie!")
    elif playerchoice == 1 and computerchoice == 3:
        print("🎉 Player wins!")
    elif playerchoice == 2 and computerchoice == 1:
        print("🎉 Player wins!")
    elif playerchoice == 3 and computerchoice == 2:
        print("🎉 Player wins!")
    else:
        print("👺 Computer wins!")
