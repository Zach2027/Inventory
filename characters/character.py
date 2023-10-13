class Weapon:
    """A weapon."""
    name = "Unknown Weapon"
    damage = 10

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

sword = Weapon("Sword", 10)
axe = Weapon("Axe", 20)
fist = Weapon("Unarmed", 1)

class Character:
    """A player or enemy gladiator."""
    name = "Unknown Gladiator"
    health = 100
    strength = 10
    shield = 5
    weapon = fist

    def __init__(self, name, health, strength, shield, weapon = fist):
        self.name = name
        self.health = health
        self.strength = strength
        self.shield = shield
        self.weapon = weapon

    def __repr__(self):
        return f'{self.name}\nHP: {self.health}\nSTR: {self.strength}\nShield: {self.shield}'
    
    def attack(self, enemy):
        damage = (self.strength + self.weapon.damage) - enemy.shield
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} with their {self.weapon.name} for {damage} damage")
korlox = Character("Korlox", 200, 10, 0, sword)
tigris = Character("Tigris", 100, 20, 10, axe)
gladiator = Character("Gladiator", 200, 20, 0, axe)

# def main():
#     print(tigris)
#     print(gladiator)
#     tigris.attack(gladiator)
#     print(gladiator)

# main()