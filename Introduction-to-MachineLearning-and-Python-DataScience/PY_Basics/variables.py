player_name = 'dan' # py is snake_case
num_lives = 4 # var types are inferred
is_game_over = False # bool False is 0 and True is any value not equal to 0

print(player_name)
print(num_lives)
print(is_game_over)

print(type(player_name)) # type keyword used to give type of printed variable
print(type(num_lives))
print(type(is_game_over))

str_num_lives = str(num_lives) # casting from int to str
print(str_num_lives)
print(type(str_num_lives))