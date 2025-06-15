key_press = 'r'

if key_press == 'r': # colon used as end of the conditional statement
    print('You pressed the right arrow key.') # indentation used. no brackets
elif key_press == 'l':
    print('You pressed the left arrow key.')
else: # else is optional but it covers every other case not in an in or elif statement
    print('You pressed a different key.')

num_value = 1
is_positive = 'pos num' if num_value > 0 else 'not pos num' #tunerary operator assigns a value to a var based on a conditional
