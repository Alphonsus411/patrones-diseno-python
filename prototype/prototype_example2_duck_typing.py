import copy

class Monster:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def attack(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class Mummy(Monster):
    def __init__(self, id, name, bandage):
        super().__init__(id, name)
        self.bandage = bandage

    def attack(self):
        print(f"Mummy {self.id} ({self.name}) attacks with {self.bandage} bandage points")


class Vampire(Monster):
    def __init__(self, id, name, bloodlust):
        super().__init__(id, name)
        self.bloodlust = bloodlust

    def attack(self):
        print(f"Vampire {self.id} ({self.name}) attacks with {self.bloodlust} bloodlust points)")


class Zombie(Monster):
    def __init__(self, id, name, health):
        super().__init__(id, name)
        self.health = health

    def attack(self):
        print(f"Zombie {self.id} ({self.name}) attacks with {self.health} health points")


zombie = Zombie("1", "Zombie 1", 100)
vampire = Vampire("2", "Vampire 1", 50)
mummy = Mummy("3", "Mummy 1", 25)

zombie.attack()
vampire.attack()
mummy.attack()

cloned_zombie = zombie.clone()
cloned_zombie.id = "4"
cloned_zombie.name = "Zombie 2"
cloned_zombie.health = 120
cloned_zombie.attack()
zombie.attack()

cloned_vampire = vampire.clone()
cloned_vampire.id = "5"
cloned_vampire.name = "Vampire 2"
cloned_vampire.bloodlust = 70
cloned_vampire.attack()
vampire.attack()

cloned_mummy = mummy.clone()
cloned_mummy.id = "6"
cloned_mummy.name = "Mummy 2"
cloned_mummy.bandage = 50
cloned_mummy.attack()
mummy.attack()