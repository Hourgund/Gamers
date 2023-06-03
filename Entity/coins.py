class Coin:
    def __init__(self, price=0, weight=1):
        self.__price = price if isinstance(price, (int, float)) and price > 0 else 0
        self.__weight = weight if weight > 0 else 100

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def diameter(self, weight):
        if weight > 0:
            self.__weight = weight