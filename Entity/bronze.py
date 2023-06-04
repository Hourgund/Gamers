from Entity.coin import Coin


class Bronze(Coin):
    def __init__(self, price=1, weight=1):
        super().__init__(price, weight)


    def __str__(self):
        return (f"Bronze coin: weight = {self.weight},"
                f" Price = {self.price} point")
