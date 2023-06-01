from Entity.product import Product
from Container.basket import Basket


class ShopAssistance:
    @staticmethod
    def calculate_total_price(basket):
        if isinstance(basket, Basket) and basket.size != 0:
            total = 0
            for i in range(basket.size):
                product = basket.get_product(i)

                if isinstance(product, Product):
                    total += product.price

            return total
        else:
            return 0