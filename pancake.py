import time
from random import random


class Pancake:
    # tracks number of pancakes created
    num_of_pancakes = 0

    def __init__(self):
        Pancake.num_of_pancakes += 1

    def __str__(self):
        return f"Number of Pancakes: {self.number_of_pancakes}"


class Cook:
    def __init__(self, name):
        self._name = name
        self._pancake_stack = []

    def cook_pancake(self):
        pancake = Pancake()
        print(f"{self._name} the cook cooks pancake #{pancake.num_of_pancakes}")
        return pancake

    def work(self):
        while True:
            pancake = self.cook_pancake()
            self._pancake_stack.append(pancake)
            time.sleep(random() * 2)
