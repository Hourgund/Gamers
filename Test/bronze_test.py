import unittest
from Entity.bronze import Bronze


class BronzeTest(unittest.TestCase):
    def test_bronze_default_constructor(self):
        bronze = Bronze()
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_weight, bronze.weight)
        self.assertEqual(expected_price, bronze.price)

    def test_bronze_constructor_with_args(self):
        expected_weight = 10
        expected_price = 5

        bronze = Bronze(expected_weight, expected_price)

        self.assertEqual(expected_weight, bronze.weight)
        self.assertEqual(expected_price, bronze.price)

    def test_negative_weight_bronze(self):
        weight = -10
        expected = 10
        bronze = Bronze(weight=weight)
        self.assertEqual(expected, bronze.weight)

    def test_zero_weight_bronze(self):
        weight = 0
        expected = 0
        bronze = Bronze(weight=weight)
        self.assertEqual(expected, bronze.weight)

    def test_zero_price_bronze(self):
        price = 0
        expected = 0
        bronze = Bronze(price=price)
        self.assertEqual(expected, bronze.bronze)

    def test_weight_property_negative_bronze(self):
        bronze = Bronze()
        expected = bronze.weight

        bronze.weight = -20

        self.assertEqual(expected, bronze.weight)

    def test_weight_property_positive_bronze(self):
        bronze = Bronze()
        expected = 200
        bronze.weight = 10
        self.assertEqual(expected, bronze.weight)

    def test_weight_property_with_zero_bronze(self):
        bronze = Bronze()
        expected = bronze.weight
        bronze.weight = 0
        self.assertEqual(expected, bronze.weight)


if __name__ == "__main__":
    unittest.main()