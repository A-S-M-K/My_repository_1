#X = input("Enter Your Name: ")
#print ("Hello"+X)
import random


def generate_superhero_name(name):
  
    prefixes = ['The', 'Captain', 'Super', 'Mighty', 'Dark', 'Shadow', 'Iron', 'Turbo']
    suffixes = ['Avenger', 'Knight', 'Flash', 'Warrior', 'Phoenix', 'Vanguard', 'Fury', 'Champion']

  
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)

 
    superhero_name = f"{prefix} {name} {suffix}"
    
    return superhero_name


name = input("Enter your name: ")


hero_name = generate_superhero_name(name)
print(f"Your superhero name is: {hero_name}")
