player_pos = 0
end_pos = 5
enemy_position = 3
while player_pos < end_pos:
    print(player_pos)
    player_pos += 1
    if player_pos == enemy_position :
        print('you collided with enemy. Game over')
        break

for i in range(10):
    print(i)

inventory = ['sword', 'armor', 'shield', 'boots']
for item in inventory:
    print(item)

