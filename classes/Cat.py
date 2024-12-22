class Cat:
    def __init__(self, name):
        self._power = 100
        self._name = name
        print(f"Cat {self._name} created")

    def is_active(self):
        return self._power >= 0

    def play(self):
        self._power -= int(input())
        print(f' Поиграл с тобой, {self._power}')

    def want_play(self):
        print(f' Поиграй со мной, {self._power}')

    def feed(self):
        print(f' Покорми меня, {self._power}')
        self._power += int(input())

    def sleep(self):
        print(f'{self._name} идет спать!')
