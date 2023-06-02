from Entity.coins import Coin


class Orange(Coin):
    def __init__(self, price=1, diameter=1):
        super().__init__(price, diameter)

    def __str__(self):
        return (f"Orange: Diameter = {self.diameter},"
                f" Price = ${self.price}")