#!/usr/bin/env checkio --domain=py run army-battles

# https://py.checkio.org/mission/army-battles/

# 
# END_DESC

# Taken from mission The Warriors

class Warrior:
    health = 50
    damage = 5
    def __init__(self):
        self.is_alive = True
    
    #Check if the health drops below 1
    def check_health(self):
        if self.health > 0:
            self.is_alive = True
        else:
            self.is_alive = False
            
    #Attacks the other unit
    def attack(self, other):
        #makes sure you cant attack while dead
        if self.is_alive == True:
            other.health = other.health - self.damage
            other.check_health()
        
class Knight(Warrior):
    damage = 7

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attack(unit_2)
        unit_2.attack(unit_1)
    print("unit1!", unit_1.is_alive, "unit2!" , unit_2.is_alive)
 
    return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")