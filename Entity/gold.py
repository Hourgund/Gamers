from Entity.coins import Coin


class Gold(Coin):
    def __init__(self, price=1, weight=1):
        super().__init__(price, weight)

    def __str__(self):
        return (f"Golden coin: weight = {self.weight},"
                f" Price = {self.price} point")