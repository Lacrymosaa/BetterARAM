import json
import random

class CharacterGetter:
    def __init__(self):
        with open('roles.json', 'r') as characters:
            self.data = json.load(characters)

    def get_character(self, classe):
        pool = self.data.get(classe, [])
        return random.choice(pool)
    
# def sortear_personagens():
#     getter = CharacterGetter()

#     team1 = [getter.get_character('Tank'),
#              getter.get_character('Fighter'),
#              getter.get_character('Support'),
#              getter.get_character('Carry'),
#              getter.get_character('Mage')]

#     team2 = [getter.get_character('Tank'),
#              getter.get_character('Fighter'),
#              getter.get_character('Support'),
#              getter.get_character('Carry'),
#              getter.get_character('Mage')]

