# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab4 Q2


class Character():
    def __init__(self, name, AP, HP):
        self.name = name
        self.AP = AP
        self.HP = HP
    def attack(self,opp):
        opp.HP -= self.AP
    def print_info(self):
        print(self.name + ": AP = " + str(self.AP) + ", HP = " + str(self.HP))

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 20, 100)
    def attack(self, opp):
        print("Punching " + opp.name)
        return super().attack(opp)

class Beast(Character):
    def __init__(self, name):
        super().__init__(name, 25, 70)
    def attack(self, opp):
        print("Biting " + opp.name)
        return super().attack(opp)



try:
    c = Character("Dummy", 10, 200) # with HP = 200, AP = 10
except TypeError:
    print("Can't instantiate abstract class Character")
hero = Hero('Spider-Man') # with HP = 100, AP = 20
beast = Beast('Two-Headed') # with HP = 70, AP = 25

while True:
    if hero.HP <= 0:
        break
    hero.attack(beast)
    if beast.HP <= 0:
        break
    beast.attack(hero)

hero.print_info()
beast.print_info()
print((beast.name if beast.HP <= 0 else hero.name) + " is dead!")

