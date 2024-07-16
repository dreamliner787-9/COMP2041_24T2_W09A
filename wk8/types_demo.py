#!/usr/bin/env python3

# ===> List <===
# create a list
fav_langs = ["C", "Python", "Java"]

# accessing a specific element
print(fav_langs[1]) # Print "Python", lists are zero-indexed

# print list
print(fav_langs)

# append item
fav_langs.append("C++")
print(fav_langs) # Prints: ['C', 'Python', 'Java', 'C++']

# insert before a specific element
fav_langs.insert(1, "C#") 
print(fav_langs) # Prints: ['C', 'C#', 'Python', 'Java', 'C++']

# delete an element at a specific index
del fav_langs[3]
print(fav_langs) # Prints: ['C', 'C#', 'Python', 'C++']

# quick 1 dimension initialisation
initial_item = 0
desired_length = 5
new_list = [initial_item] * desired_length
print(new_list)

# quick 2 dimension initialisation
desired_height = 4
desired_width = 2
new_list = [[initial_item] * desired_width] * desired_height
print(new_list)



# ===> Tuple (an immutable list) <===
fav_langs = ("C", "Python", "Java") # note the round vs square brackets
print(fav_langs)

# fav_langs.append("C++") # does not run

# accessing a specific element
print(fav_langs[1]) # Prints Python



# ===> Dictionary (a hashmap) <===
# create an empty dictionary
empty_dict = dict()

# create dictionary with some pre-filled data
pokemons = {"bulbasaur": "grass", "squirtle": "water"}

# insert a key-value pair
key = "charizard"
value = "fire"
pokemons[key] = value
# pokemon["charizard"] = "fire" # same thing

# access a specific key-value pair
print(pokemons["bulbasaur"]) # Print "grass"

# checking whether a key exist
print("mimikyu" in pokemons) # Print False
print("charizard" in pokemons) # Print True

# print the contents
print(pokemons)

# get all keys, which is a list
print(pokemons.keys())

# get all values, which is also list
print(pokemons.values())

# delete a key-value pair
del pokemons["squirtle"]
print(pokemons)



# ===> Set (an unordered collection of unique elements) <===
# empty set
fav_numbers = set()

# insert an element
fav_numbers.add(42)
fav_numbers.add(60)
fav_numbers.add(76)

# checking whether an element exists
print(2041 in fav_numbers) # False
print(42 in fav_numbers) # True

# delete an element
fav_numbers.remove(60)
print(fav_numbers) # {42, 76}
