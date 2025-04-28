def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0



def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)



def feast(beast, dish):
    beast_first_and_last = beast[0] + beast[-1]
    dish_first_and_last = dish[0] + dish[-1]
    return beast_first_and_last == dish_first_and_last



def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"



def points(games):
    return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, game.split(':')) for game in games))