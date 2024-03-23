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

    def set_priority(self):
        return self._priority

    def get_priority(self):
        return self._priority

    def get_value(self):
        return self._value

    # dunder
    def __str__(self):
        return f"Priority:{self._priority}; Value:{self._value}"


class PQ:
    def __init__(self):
        self._entries = []

    def add(self, priority, value):
        entry = Entry(priority, value)
        self._entries.append(entry)

    def remove_min(self):
        if not self._entries:
            return false
        else:
            min_entry = min(self._entries, key=lambda entry: entry.get_priority())
            self._entries.remove(min_entry)
            return min_entry

    def set_priority(self, newPriority, value):
        for entry in self._entries:
            if entry.get_value == value:
                entry.set_priority(newPriority)
        self._entries.sort(key=lambda entry: entry.get_priority())

    def size(self):
        return len(self._entries)


if __name__ == "__main__":
    pq = PQ()

    pq.add(2, "Eat")
    pq.add(0, "Study for CS 3035")
    pq.add(3, "Sleep")
    pq.add(1, "Maintain Personal Relationships")
    pq.add(4, "Practice Good Personal Hygiene")
    pq.set_priority("Practice Good Personal Hygiene", 2)
    pq.set_priority("Eat", 4)

    #while pq.size() > 0:
        #print(pq.remove_min())

    for entry in pq._entries:
        print(entry.get_priority(), entry.get_value())



