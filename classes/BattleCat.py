import random
from rich import print
from classes.Cat import Cat
from classes.Target import Target


class BattleCat(Cat):
    def __init__(self, name):
        super().__init__(name)
        self._power = 200
        print(f"[green]BattleCat {self._name} with {self._power} created")
    
    def cannonFire(self):
        target = Target(random.randint(1, 10))
        coordinate = input('Enter coordinate as integer from 1 to 10: ')
        if not coordinate.isdigit():
            print('[red]Invalid coordinate')
            return
        else:
            coordinate = int(coordinate)
        print(f'[blue]Fire on {target}')
        self._power -= 1
        print(f'[green]Power: {self._power}')
        print(f'[blue]Coordinate: {coordinate}')
        print(f'[yellow]Target coordinate: {target}')
        if target._x == coordinate:
            print('[green]Target destroyed')
        else:
            print('[red]Missed')

