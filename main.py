import os
from hero import Hero, Villain
from powers import sound_blast, radiation_poisoning, power_punch

hero: Hero = Hero(alias='Superman', health=100)
hero.next_power(sound_blast)

villain: Villain = Villain(alias='Green Goblin', health=88, power=sound_blast)

fight: bool = True

while fight:
    os.system("cls")

    hero.attack(villain)
    villain.attack(hero)

    hero.health_bar.draw()
    villain.health_bar.draw()

    input()
    if hero.health <= 0:
        print(
            f'{hero.alias} has fallen to {villain.alias}!'
        )
        break

    if villain.health <= 0:
        print(
            f'{villain.alias} has fallen to {hero.alias}!'
        )
        break
