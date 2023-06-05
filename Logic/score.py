from Entity.coin import Coin
from Containers.player import Players


class Score:
    @staticmethod
    def calculate_total_price(player):
        if isinstance(player, Players) and player.size != 0:
            total = 0
            for i in range(player.size):
                coins = player.get_coin(i)

                if isinstance(coins, Coin):
                    total += coins.price

            return total
        else:
            return 0
