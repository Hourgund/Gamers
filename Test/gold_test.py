import unittest
from Entity.gold import Gold


class GoldTest(unittest.TestCase):
    def test_gold_default_constructor(self):
        gold = Gold()
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_weight, gold.weight)
        self.assertEqual(expected_price, gold.price)

    def test_gold_constructor_with_args(self):
        expected_weight = 15
        expected_price = 10

        gold = Gold(expected_weight, expected_price)

        self.assertEqual(expected_weight, gold.weight)
        self.assertEqual(expected_price, gold.price)

    def test_negative_weight_gold(self):
        weight = -10
        expected = 15
        gold = Gold(weight=weight)
        self.assertEqual(expected, gold.weight)

    def test_zero_weight_gold(self):
        weight = 0
        expected = 0
        gold = Gold(weight=weight)
        self.assertEqual(expected, gold.weight)

    def test_zero_price_gold(self):
        price = 0
        expected = 0
        gold = Gold(price=price)
        self.assertEqual(expected, gold.weight)

    def test_weight_property_negative_gold(self):
        gold = Gold()
        expected = gold.weight
        gold.weight = -10
        self.assertEqual(expected, gold.weight)

    def test_weight_property_positive_gold(self):
        gold = Gold()
        expected = 20
        gold.weight = 25
        self.assertEqual(expected, gold.weight)

    def test_weight_property_with_zero_gold(self):
        gold = Gold()
        expected = gold.weight
        gold.weight = 0
        self.assertEqual(expected, gold.weight)


if __name__ == "__main__":
    unittest.main()
