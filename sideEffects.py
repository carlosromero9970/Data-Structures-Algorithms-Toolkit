class test:
    def __init__(self):
        self._value = 5

    def sideEffectWithNoReferentialTransparency(self):
        self._value += 1

    def sideEffectWithReferentialTransparency(self, first, last):
        self._value += 1
        return first + last

    def NoSideEffectWithNoReferentialTransparency(self):
        print("hello")

    def NoSideEffectsWithNoReferntialTransparency(self, first, last):
        return first + last

