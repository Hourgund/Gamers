from Entity.coins import Coin
from Containers.player_1 import Player1
from Containers.player_2 import Player2


class Score:
    @staticmethod
    def calculate_total_price_first_player(player_1):
        if isinstance(player_1, Player1) and player_1.size != 0:
            first_total = 0
            for i in range(player_1.size):
                coins = player_1.get_coin(i)

                if isinstance(coins, Coin):
                    first_total += coins.price

            return first_total
        else:
            return 0

    def calculate_total_price_second_player(player_2):
        if isinstance(player_2, Player2) and player_2.size != 0:
            second_total = 0
            for i in range(player_2.size):
                coins = player_2.get_coin(i)

                if isinstance(coins, Coin):
                    second_total += coins.price

            return second_total
        else:
            return 0
