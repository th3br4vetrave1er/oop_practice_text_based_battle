from powers import power_punch, sound_blast, radiation_poisoning
from health_bar import Healthbar


# creating hero blueprint
class Gifted:
    def __init__(self, alias: str, health: int):
        self.alias = alias
        self.health = health
        self.health_max = health

        self.power = power_punch

    def attack(self, target) -> None:
        target.health -= self.power.damage
        # to avoid going hp below 0 we use max()
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f'{self.alias} dealt {self.power.damage} damage to {target.alias} '
            f'with {self.power.name}'
        )


class Villain(Gifted):
    def __init__(self, alias: str, health: int, power: str) -> None:
        super().__init__(alias=alias, health=health)
        self.power = power
        self.health_bar = Healthbar(self, color='red')


class Hero(Gifted):
    def __init__(self, alias: str, health: int) -> None:
        super().__init__(alias=alias, health=health)

        self.basic_power = self.power
        self.health_bar = Healthbar(self, color='green')

    def next_power(self, power) -> None:
        self.power = power
        print(
            f'{self.alias} want to use {self.power.name}!'
        )

    def previous_power(self) -> None:
        print(
            f'{self.alias} switched to  {self.power.name}'
        )
        self.power = self.basic_power
