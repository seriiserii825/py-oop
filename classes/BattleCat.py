from classes.Cat import Cat
from classes.Target import Target


class BattleCat(Cat):
    def __init__(self, name):
        super().__init__(name)
        self._power = 200
        print(f"BattleCat {self._name} with {self._power} created")
    
    def cannonFire(self, target: Target, coordinate: int):
        print(f'Fire on {target}')
        self._power -= 1
        print(f'Power: {self._power}')
        print(f'Coordinate: {coordinate}')
        print(f'Target coordinate: {target}')
        if target._x == coordinate:
            print('Target destroyed')
        else:
            print('Missed')

