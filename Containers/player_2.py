from Containers.players import Players
from Entity.coins import Coin


class Player2(Players):
    def __init__(self, name="User1", coin=None, size=30):
        super().__init__(size)

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
