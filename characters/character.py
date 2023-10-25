class Weapon:
    """A weapon."""
    name = "Unknown Weapon"
    damage = 10
    defense = 0

    def __init__(self, name, damage, defense = 0):
        self.name = name
        self.damage = damage
        self.defense = defense

    def __str__(self):
        return f"{self.name} (DMG: {self.damage}, DEF: {self.defense})"
    


silver_sword = Weapon("Silver Sword", 20)
sword = Weapon("Sword", 10, 10)
long_sword = Weapon("Long Sword", 15, 5)
axe = Weapon("Axe", 20)
fist = Weapon("Unarmed", 1)
double_daggers = Weapon("Dagger", 15)

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
    def critical_attack(self, enemy):
        damage = 2 * (self.strength + self.weapon.damage) - (enemy.shield + enemy.weapon.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} with their {self.weapon.name} for {damage} damage")
    def attack(self, enemy):
        damage = (self.strength + self.weapon.damage) - (enemy.shield + enemy.weapon.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} with their {self.weapon.name} for {damage} damage")

small_man = Character("Small Man", 60, 20, 0)
korlox = Character("Korlox", 200, 10,0, axe)
tigris = Character("Tigris", 100, 20, 10, axe)
gladiator = Character("Gladiator", 100, 20, 0, axe)
commodus = Character("Commodus", 100, 10, 0, double_daggers)
