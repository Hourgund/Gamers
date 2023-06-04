from Entity.coin import Coin


class Players:
    def __init__(self, name="No name", coins=None):
        if not coins:
            self.__coins = []
        else:
            self.__coins = coins

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins):
        if isinstance(coins, list):
            self.__coins = coins

    @property
    def size(self):
        return len(self.coins)

    def get_coin(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__coins[index]

    def add(self, coin):
        if isinstance(coin, Coin):
            self.__coins.append(coin)

    def __str__(self):
        msg = "List of coins:"

        for i in range(self.size):
            msg += f"\n{i + 1})" + str(self.__coins[i])

        return msg
