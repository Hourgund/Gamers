import unittest
from Containers.player import Players
from Entity.coin import Coin


class PlayersTest(unittest.TestCase):
    def test_player_default_constructor(self):
        player = Players()
        expected_name = "No name"
        expected_coins = None

        self.assertEqual(expected_name, player.name)
        self.assertEqual(expected_coins, player.coins)

    def test_player_constructor_with_args(self):
        expected_name = "Alex"
        expected_coins = [Coin.price, Coin.weight]

        player = Players(expected_name, expected_coins)

        self.assertEqual(expected_name, player.name)
        self.assertEqual(expected_coins, player.coins)

    def test_int_name_player(self):
        name = 14
        expected = "No nmae"
        player = Players(name=name)
        self.assertEqual(expected, player.name)

    def test_no_name_player(self):
        name = ""
        expected = "No name"
        player = Players(name=name)
        self.assertEqual(expected, player.name)

    def test_zero_coins_player(self):
        coins = None
        expected = None
        player = Players(coins=coins)
        self.assertEqual(expected, player.coins)

    def test_name_property_int_name(self):
        player = Players()
        expected = player.name
        player.name = 20
        self.assertEqual(expected, player.name)

    def test_name_property_player(self):
        player = Players()
        expected = "Alex"
        player.name = "Alex"
        self.assertEqual(expected, player.name)

    def test_property_with_no_name_bronze(self):
        player = Players()
        expected = player.name
        player.name = ""
        self.assertEqual(expected, player.name)


if __name__ == "__main__":
    unittest.main()