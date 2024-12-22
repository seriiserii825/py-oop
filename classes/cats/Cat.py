from rich import print
class Cat:
    def __init__(self, name):
        self._power = 100
        self._name = name
        print(f"[green]Cat {self._name} created")

    def is_active(self):
        return self._power >= 0

    def play(self):
        self._power -= int(input())
        print(f'[blue] Поиграл с тобой, {self._power}')

    def want_play(self):
        print(f'[green]Поиграй со мной, {self._power}, 0 - 100: ')

    def feed(self):
        print(f'[blue]Покорми меня, {self._power}, 0 - 100: ')
        self._power += int(input())

    def sleep(self):
        print(f'[red]{self._name} идет спать!')
