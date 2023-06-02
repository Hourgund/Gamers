class Coin:
    def __init__(self, price=0, diameter=1):
        self.__price = price if isinstance(price, (int, float)) and price > 0 else 0
        self.__diameter = diameter if diameter > 0 else 100

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter > 0:
            self.__diameter = diameter