class Person: # this is the class keyword. same as C#
    def __init__(self, name, health, x_pos,): # initializer is class constructor
        self.health = health
        self.name = name # I think self is similar to 'this' in C#
        self.x_pos = x_pos

    def move (self, by_amount):
        self.x_pos += by_amount

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health < 0:
            self.health = 0

    def check_if_dead(self):
        return self.health == 0