import random
def scissorsView():
    playerchoice = input("Choose rock(1), paper(2), or scissors(3): ")
    playerchoice = int(playerchoice)

    if playerchoice < 1 or playerchoice > 3:
        print("😢 Invalid choice")
        return

    computerchoice = random.randint(1, 3)
    computerchoice = int(computerchoice)

    print("Player choice: ", playerchoice)
    print("Computer choice: ", computerchoice)

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

