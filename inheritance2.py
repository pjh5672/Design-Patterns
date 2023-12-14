class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7


class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9


class BadWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)


class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9


class GoodWay(PlusNineCorrect, TimesSevenCorrect):
    def __init__(self, value):
        super().__init__(value)


class GoodWay2(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)



if __name__ == "__main__":
    foo1 = BadWay(5)
    print(f"Expected : (5 * 7) + 9 = 44, but got {foo1.value}")

    foo2 = GoodWay(5)
    print(f"Expected : (5 * 7) + 9 = 44, got {foo2.value}")

    foo3 = GoodWay2(5)
    print(f"Expected : (5 + 9) * 7 = 98, got {foo3.value}")
