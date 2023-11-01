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
        return f"{self.name}"
    

spear = Weapon("Spear", 25)
silver_sword = Weapon("Silver Sword", 20)
sword = Weapon("Sword", 15)
long_sword = Weapon("Long Sword", 10, 3)
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

small_man = Character("Small Man", 60, 15, 0, sword)
korlox = Character("Korlox", 200, 10, 0, axe)
tigris = Character("Tigris", 100, 20, 10, axe)
spartacus = Character("Spartacus", 100, 20, 5, spear)
lucius_verus = Character("Lucius Verus", 200, 20, 10, silver_sword)
galius = Character("Galius", 200, 30, 5, spear)
decimus = Character("Decimus", 150, 30, 15, sword)
corvus = Character("Corvus the Crusher", 250, 40, 10, axe)
quintus = Character("Quintus the Quick", 120, 50, 20, silver_sword)

commodus = Character("Commodus", 100, 15, 5, double_daggers)



maximus = Character("Maximus the Merciless", 1000, 60, 50, sword)