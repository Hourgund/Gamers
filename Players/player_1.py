from Entity.coins import Coin


class Player1:
    def __init__(self, name="User1", coins=None, size=30):
        if not coins:
            self.__coins = []
        else:
            self.__coins = coins

    @property
    def size(self):
        return len(self.__coins)

    def get_coin(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__coins[index]

    def add(self, coin):
        if isinstance(coin, Coin):
            self.__coins.append(coin)

    def __str__(self):
        msg = "List of products:"

        for i in range(self.size):
            msg += f"\n{i + 1})" + str(self.__coins[i])

        return msg
