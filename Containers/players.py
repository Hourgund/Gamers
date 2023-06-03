from Entity.coins import Coin


class Players:
    def __init__(self, name="User1", coins=None, size=30):
        if not coins:
            self.__coins = []
        else:
            self.__coins = coins

    @property
    def size(self):
        return len(self.__coins)


