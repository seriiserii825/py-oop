def cat():
    power = 100
    while power >= 0:
        print(f" Покорми меня, {power}")
        power += int(input())
        print(f"Поиграй со мной, {power}")
        power -= int(input())
    print("Я спать!")
