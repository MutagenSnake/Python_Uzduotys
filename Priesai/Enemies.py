# Mes atsakingi už priešų kūrimą kompiuteriniam žaidimui.
#
# Visi priešai turi gyvybes, maksimalų gyvybių skaičių, gali atlikti veiksmą, būti sužaloti ir būti pagydyti.
# Kai priešas pagydomas, jis turi gražinti eilutę su savo tipu ir nuo kiek iki kiek buvo pagydytas.
# Sukurkite priešą lankininkas. Jei lankininkas turi daugiau arba lygiai 20% gyvybių, jo atliekamas veiksmas gražina eilutę "Shooting an arrow".
# Jei lankininkui mažiau nei 20% gyvybių, jo atliekamas veiksmas gražina eilutę "Running away".
# Sukurkite priešą riteris. Jei riteris turi maksimalų gyvybių skaičių, jo atliekamas veiksmas gražina eilutę "Charging".
# Jei turi tarp 10% ir 100%, jo veiksmas gražina eilutę "Swinging a sword". Jei turi mažiau nei 10%, veiksmas atgydo riterį iki pilnų gyvybių.
#
# Įsitikinkite, kad priešai elgiasi pagal sąlygas naudodami "assert" sakinius.

class Enemy:
    def __init__(self, health):
        self.health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self._health = new_health
        elif new_health > 100:
            self._health = 100
        elif new_health < 0:
            self._health = 0

    def lose_health(self):
        if self.health > 0:
            self.health = self.health - 10
        else:
            return f'Dead'

    def gain_health(self):
        if self.health > 0:
            self.health = self.health + 10
        else:
            return f'Dead'

    def take_action(self):
        pass

class Bowman(Enemy):
    def take_action(self):
        if self.health == 0:
            return f'Dead'
        elif self.health < 20:
            return f'Running away'
        elif self.health >= 20:
            return f'Shooting an arrow'

class Knight(Enemy):
    def take_action(self):
        if self.health == 0:
            return f'Dead'
        elif self.health == 100:
            return f'Charging'
        elif self.health >= 10 and self.health <100:
            return f'Swinging a sword'
        elif self.health <10:
            self.health = 100
            return f'Healing'

bowman = Bowman(50)
assert (bowman.take_action() == f'Shooting an arrow')

bowman.health = 10
assert (bowman.take_action() == f'Running away')

bowman.gain_health()
assert (bowman.health == 20)

bowman.lose_health()
assert (bowman.health == 10)

knight = Knight(50)
assert (knight.take_action() == f'Swinging a sword')

knight.health = 150
assert (knight.health == 100)
assert (knight.take_action() == f'Charging')

knight.health = 5
assert (knight.take_action() == f'Healing')

knight.health = -20
assert (knight.health == 0)
assert (knight.take_action() == f'Dead')

pass
