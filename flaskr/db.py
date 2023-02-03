import json,os
import random

class dataClass:
    def __init__(self):
        self.selection = list(range(1, 152))
        self.sample = random.sample(self.selection, 2)
        self.winner = None

    def reset(self):
        self.selection = list(range(1, 152))
        return self.selection

    def resample(self):

        if len(self.selection) == 1:
            return

        else:   
            self.sample = random.sample(self.selection, 2)
            return

    def elim(self, value):
        self.selection.remove(value)
        return

    def tourney(self, choice):
        if choice == "Left":
            self.elim(self.sample[1])
            self.resample()
        elif choice == "Right":
            self.elim(self.sample[0])
            self.resample()

    def finals(self, choice):
        if choice == "Left":
            self.winner = self.sample[0]
        elif choice == "Right":
            self.winner = self.sample[1]
        



def get_rand_img():
    return os.path.join("images", str(f"{random.randint(1,150):03}") + '.png')

def get_img(num):
    return os.path.join("images", str(f"{num:03}") + '.png')

def get_db():
    with open("flaskr/static/data/pokemon.json", encoding="utf8") as f:
        return json.load(f)