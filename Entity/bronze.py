from Entity.coins import Coin


class Bronze(Coin):
    def __init__(self, price=1, diameter=1):
        super().__init__(price, diameter)

        self.__diameter = diameter if diameter > 0 else 100

    def __str__(self):
        return (f"Bronze: Diameter = {self.diameter},"
                f" Price = {self.price} point")
