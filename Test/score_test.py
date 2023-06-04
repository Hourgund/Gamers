import unittest
from Containers.player import Players
from Entity.coin import Coin
from Logic.score import Score


class ShopAssistanceTest(unittest.TestCase):
    def test_different_type(self):
        basket = "basket"
        expected = 0

        actual = Score.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    def test_empty_player(self):
        player = Players()
        expected = 0

        actual = Score.calculate_total_price(player)

        self.assertEqual(expected, actual)

    def test_player_with_None(self):
        player = None
        expected = 0

        actual = Score.calculate_total_price(player)

        self.assertEqual(expected, actual)

    def test_player_with_coins_positive(self):
        player = Players()
        coin1 = Coin(5)
        coin2 = Coin(10)
        coin3 = Coin(3)
        player.add(coin1)
        player.add(coin2)
        player.add(coin3)

        expected = 18

        actual = Score.calculate_total_price(player)

        self.assertEqual(expected, actual)

    def test_player_with_one_coin(self):
        coin = Coin(5)

        player = Players()
        player.add(coin)

        expected = coin.price

        actual = Score.calculate_total_price(player)

        self.assertEqual(expected, actual)

    def test_player_with_coins_negative(self):
        player = Players()
        coin1 = Coin(5)
        coin2 = Coin(10)
        coin3 = Coin(3)

        player.add(5)
        player.add(coin1)
        player.add(coin3)
        player.add(coin2)
        player.add("string")

        expected = 18

        actual = Score.calculate_total_price(player)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
