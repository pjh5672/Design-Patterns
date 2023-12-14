class A:
    def __init__(self) -> None:
        self.a = 10

    def get_a(self):
        return self.a
    
class B(A):
    def __init__(self) -> None:
        A.__init__(self)
        self.b = 20

    def get_b(self):
        return self.b

class C(B):
    def __init__(self) -> None:
        B.__init__(self)
        self.c = 30

    def get_c(self):
        return self.c


if __name__ == "__main__":
    c = C()
    print(c.get_c())
    print(c.get_b())
    print(c.get_a())