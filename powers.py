class Power:
    def __init__(
        self, name: str,
        power_type: str,
        damage: int,
        value: int
    ) -> None:
        self.name = name
        self.power_type = power_type
        self.damage = damage
        self.value = value


power_punch: Power = Power(
    name='Power Punch',
    power_type='Physical power',
    damage=4,
    value=5
    )

sound_blast: Power = Power(
    name='Sound Blast',
    power_type='Acoustic power',
    damage=10,
    value=3
    )

radiation_poisoning: Power = Power(
    name='Radiation Poisoning',
    power_type='Radiation power',
    damage=5,
    value=2
)
