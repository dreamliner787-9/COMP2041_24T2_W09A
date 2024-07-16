#!/usr/bin/env python3

pokemons = {"charizard": "fire", "bulbasaur": "grass", "squirtle": "water"}

def nice_print_dict(pokemons):
    for key, value in pokemons.items():
        print(f"[{key}] => {value}")

if __name__ == "__main__":
    nice_print_dict(pokemons)