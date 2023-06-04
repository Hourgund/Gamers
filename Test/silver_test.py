import unittest
from Entity.silver import Silver


class SilverTest(unittest.TestCase):
    def test_silver_default_constructor(self):
        silver = Silver()
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_weight, silver.weight)
        self.assertEqual(expected_price, silver.price)

    def test_silver_constructor_with_args(self):
        expected_weight = 15
        expected_price = 10

        silver = Silver(expected_weight, expected_price)

        self.assertEqual(expected_weight, silver.weight)
        self.assertEqual(expected_price, silver.price)

    def test_negative_weight_silver(self):
        weight = -10
        expected = 15
        silver = Silver(weight=weight)
        self.assertEqual(expected, silver.weight)

    def test_zero_weight_silver(self):
        weight = 0
        expected = 0
        silver = Silver(weight=weight)
        self.assertEqual(expected, silver.weight)

    def test_zero_price_silver(self):
        price = 0
        expected = 0
        silver = Silver(price=price)
        self.assertEqual(expected, silver.price)

    def test_weight_property_negative_silver(self):
        silver = Silver()
        expected = silver.weight
        silver.weight = -10
        self.assertEqual(expected, silver.weight)

    def test_weight_property_positive_silver(self):
        silver = Silver()
        expected = 200
        silver.weight = 10
        self.assertEqual(expected, silver.weight)

    def test_weight_property_with_zero_silver(self):
        silver = Silver()
        expected = silver.weight
        silver.weight = 0
        self.assertEqual(expected, silver.weight)


if __name__ == "__main__":
    unittest.main()
