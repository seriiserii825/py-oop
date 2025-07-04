from classes.cats.BattleCat import BattleCat


def catsView():
    # cat()
    # catsFunctions()
    # cat = Cat('Мурзик')
    # while cat.is_active():
    #     cat.feed()
    #     cat.want_play()
    #     cat.play()
    # cat.sleep()
    battle_cat = BattleCat("Барсик")
    while battle_cat.is_active():
        battle_cat.feed()
        battle_cat.cannonFire()
        battle_cat.want_play()
        battle_cat.play()
    battle_cat.sleep()
