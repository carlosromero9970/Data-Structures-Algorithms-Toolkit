"""
Carlos Romero

CS 3035-05(13119)

Exercise: Implement a Priority Queue in Python

Due on the 26th of March
"""


class Entry:
    def __init__(self, priority, value):
        self._priority = priority
        self._value = value

    # setter
    def set_priority(self):
        return self._priority

    # setter
    def get_value(self):
        return self._value

    # dunder
    def __str__(self):
        return f"Priority:{self._priority}; Value:{self._value}"


class PQ(Entry):
    def __init__(self, priority, value):
        super(PQ, self).__init__(priority, value)
        entries = [Entry(priority, value)]  # list literal

    def remove_min(self, entries):
        pass


if __name__ == "__main__":

    food = Entry(4, "EAT")
    print(food.__str__())
