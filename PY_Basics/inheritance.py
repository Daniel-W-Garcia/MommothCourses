from PY_Basics.classes import Person


class Enemy(Person): #this is the way py does inheritance
    def __init__(self, name, x_pos, health, damage_amount):
        super().__init__(name, x_pos, health)
        self.max_health = health
        self.damage_amount = damage_amount