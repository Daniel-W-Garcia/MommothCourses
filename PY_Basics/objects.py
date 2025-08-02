from PY_Basics import classes
from inheritance import Enemy

player_character = classes.Person("Dan", 100, 0)
enemy_character = Enemy('Enemy', 0, 100, 10) # inherits from Person class. adds damage amount and max health attributes
print(type(player_character))
print(player_character.name)
print(player_character.health)
print(player_character.x_pos)

other_character = classes.Person("Jane", 50, 5)
print(other_character.name)
print(other_character.health)
print(other_character.x_pos)

print(f'old pos: {player_character.x_pos}') # f'string' is similar to $'string' in C#
print('Player will move 5 spaces')
player_character.move(5)
print(f'new pos: {player_character.x_pos}')


