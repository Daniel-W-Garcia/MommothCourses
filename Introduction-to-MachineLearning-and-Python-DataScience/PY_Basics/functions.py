x_pos = 0
current_pos = 0

def move():
    global x_pos  # global keyword needed to access variable outside function scope
    x_pos += 1

print(x_pos)
move()
print(x_pos)

def movement(by_amount): # don't have to declare value type for param
    global current_pos
    current_pos += by_amount

movement(5)
print(current_pos)

def move_default_param(by_amount = 1): # default param value assigned
    global current_pos
    current_pos += 1

move_default_param() # when called without input for param, default value is used
print(current_pos)

def move_to_end(position, end_pos):

    while position < end_pos:
        print(position)
        position += 1
    return position

new_current_position = move_to_end(0, 5)
print(new_current_position)