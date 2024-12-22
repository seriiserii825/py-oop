def catsFunctions():
    def catCreate():
        global power
        power = 100
        print("Cat created")

    def catIsActive():
        return power >= 0
    
    def catPlay():
        global power
        power -= int(input())

    def catWantPlay():
        global power
        print(f' Поиграй со мной, {power}')

    def catFeed():
        global power
        print(f' Покорми меня, {power}')
        power += int(input())

    def catSleep():
        print('Я спать!')

    catCreate()
    while catIsActive():
        catFeed()
        catWantPlay()
        catPlay()
    catSleep()
