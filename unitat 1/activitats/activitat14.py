from math import pi, sqrt
from abc import ABC, abstractmethod


class Figura():
    def __init__(self) -> None:
        pass

    @abstractmethod
    def area() -> int:
        pass

    @abstractmethod
    def perimetre() -> int:
        pass

    def __str__(self) -> str:
        return "Sóc un {} d'àrea {} i perímetre {}".format(self.__class__.__name__, self.area(), self.perimetre())


class Cercle(Figura):

    def __init__(self, radi=0) -> None:
        super().__init__()
        self.__radi = radi

    @property
    def radi(self):
        return self.__radi

    @radi.setter
    def radi(self, radi):
        self.__radi = radi

    def perimetre(self) -> int:
        return 2 * pi * self.__radi

    def area(self) -> int:
        return pi * self.__radi ** 2


class Triangle(Figura):

    def __init__(self, costat=0) -> None:
        super().__init__()
        self.__costat = costat

    @property
    def costat(self):
        return self.__costat

    @costat.setter
    def costat(self, costat):
        self.__costat = costat

    def perimetre(self) -> int:
        return 3 * self.__costat

    def area(self) -> int:
        altura = sqrt(self.__costat ** 2 - (self.__costat/2) ** 2)
        return (self.__costat * altura)/2


class Rectangle(Figura):

    def __init__(self, base=0, altura=0) -> None:
        super().__init__()
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def perimetre(self) -> int:
        return 2 * self.__base + 2 * self.__altura

    def area(self) -> int:
        return self.__base * self.__altura


class Quadrat(Rectangle):

    def __init__(self, costat=0) -> None:
        super().__init__(costat, costat)

    @property
    def costat(self):
        return self.base

    @costat.setter
    def costat(self, costat):
        self.altura = costat
        self.base = costat


if __name__ == "__main__":
    c1 = Cercle()
    print(c1)
    c1.radi = 15
    print(c1)

    t1 = Triangle()
    print(t1)
    t1.costat = 3
    print(t1)

    r1 = Rectangle(2, 3)
    print(r1)

    q1 = Quadrat(2)
    print(q1)

    q1.costat = 5
    print(q1)
