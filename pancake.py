import threading
import time
from random import random
from queue import LifoQueue


class Pancake:
    # tracks number of pancakes created
    num_pancakes = 0

    def __init__(self):
        Pancake.num_pancakes += 1
        self._num = Pancake.num_pancakes

    def __str__(self):
        return f"Total pancakes :{self._num}"


class Cook:
    def __init__(self, name, stack_of_pancakes):
        self._name = name
        self._stack_of_pancakes = stack_of_pancakes

    def cook_pancake(self):
        pancake = Pancake()
        print(f"{self._name} the cook cooks pancake #{pancake.num_pancakes}")
        return pancake

    def work(self):
        while True:
            pancake = self.cook_pancake()
            self._stack_of_pancakes.put(pancake)
            time.sleep(random() * 2)

    def __str__(self):
        return f"Cook {self._name}."


class Customer:
    def __init__(self, name, stack_of_pancakes):
        self._name = name
        self._stack_of_pancakes = stack_of_pancakes

    def eat_pancake(self, pancake):
        # ?
        return f"{self._name} the customer eats pancake #{pancake.num_pancakes}"

    def dine(self):
        while True:
            if self._stack_of_pancakes.empty():
                print("\nNo pancakes ready to eat!")
                time.sleep(random() * 2)
            else:
                pancake = self._stack_of_pancakes.get()
                self.eat_pancake(pancake)
                time.sleep(random() * 2)

    def __str__(self):
        return f"Customer {self._name}"


class PancakeHouse:
    def __init__(self):
        self._stack = LifoQueue()
        self._cooks = []
        self._customers = []

    def add_cook(self, name):
        cook = Cook(name, self._stack)
        self._cooks.append(cook)

    def add_customer(self, name):
        customer = Customer(name, self._stack)
        self._customers.append(customer)

    def begin_shifts(self):
        for cook in self._cooks:
            thread = threading.Thread(target=cook.work)
            thread.start()

    def server_customers(self):
        for customer in self._customers:
            thread = threading.Thread(target=customer.dine)
            thread.start()

    def open(self, seconds):
        self.begin_shifts()
        self.server_customers()
        time.sleep(seconds)
        print(f"Pancakes uneaten {self._stack.qsize()}")
        while not self._stack.empty():
            pancake = self._stack.get()
            print(pancake)

        exit()


# Driver
pancake_house = PancakeHouse()
pancake_house.add_cook("Luis")
pancake_house.add_cook("Alex")
pancake_house.add_customer("Moe")
pancake_house.add_customer("Earl")
pancake_house.open(60)
