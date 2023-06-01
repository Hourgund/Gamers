from Points.coins import Coin


class Orange(Coin):
    def __init__(self, price=):
        super().__init__(price)

        self.__diameter = diameter if diameter > 0 else 100
        self.__vitamin = vitamin if vitamin >= 0 else 1000


    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter > 0:
            self.__diameter = diameter

    @property
    def vitamin(self):
        return self.__vitamin

    @vitamin.setter
    def vitamin(self, vitamin):
        if vitamin >= 0:
            self.__vitamin = vitamin

    def __str__(self):
        return (f"Orange: Diameter = {self.__diameter},"
                f" Vitamin C = {self.__vitamin},"
                f" Price = ${self.price}")