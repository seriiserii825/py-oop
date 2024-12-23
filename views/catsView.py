from classes.cats.BattleCat import BattleCat
from classes.cats.Cat import Cat
from classes.cats.Target import Target
from modules.cats_functions import catsFunctions
from modules.simple_cats import cat


def catsView():
    # cat()
    # catsFunctions()
    # cat = Cat('Мурзик')
    # while cat.is_active():
    #     cat.feed()
    #     cat.want_play()
    #     cat.play()
    # cat.sleep()
    battle_cat = BattleCat('Барсик')
    while battle_cat.is_active():
        battle_cat.feed()
        battle_cat.cannonFire()
        battle_cat.want_play()
        battle_cat.play()
    battle_cat.sleep()
