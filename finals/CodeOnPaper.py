# Carlos Romero
import math
from abc import abstractmethod


class Cryptid:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    @abstractmethod
    def attack(self, location):
        pass

    def __eq__(self, other):
        if isinstance(other, Cryptid):
            return math.isclose(self._height, other._height) and self._name == other._name
        else:
            return False


class Yeti(Cryptid):
    def __init__(self, name, height):
        super().__init__(name, height)

    def __str__(self):
        return f"{self._name} the Yeti is {self._height} meters tall"

    def attack(self, location):
        return f"{self._name} the Yeti throws ice at the citizens of {location}"

    def __add__(self, other):
        combined_name = self._name + other.name
        combined_height = self._height + other.height
        return Yeti(combined_name, combined_height)


