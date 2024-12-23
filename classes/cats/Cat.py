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
        print(f'[green]Поиграй со мной, 0 - 100 ({self._power}): ')

    def feed(self):
        print(f'[blue]Покорми меня, 0 - 100 ({self._power}): ')
        self._power += int(input())

    def sleep(self):
        print(f'[red]{self._name} идет спать!')
