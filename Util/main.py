from Entity.bronze import Bronze
from Containers.player_1 import Player1
from Logic.score import Score


def main():
    basket = Player1()

    br = Bronze(1, 10.0)

    basket.add(br)

    print(f"size = {basket.size}")

    print(basket)

    total = ShopAssistance.calculate_total_price(basket)

    print(f"Total price = {total}")


if __name__ == "__main__":
    main()