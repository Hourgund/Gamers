from Entity.bronze import Bronze
from Entity.silver import Silver
from Entity.gold import Gold
from Containers.player_1 import Player1
from Logic.score import Score


def main():
    basket = Player1()

    br = Bronze(1, 10.0)
    sil = Silver(5, 15.0)
    gol = Gold(10, 20.0)

    basket.add(sil)
    basket.add(gol)
    basket.add(sil)
    basket.add(gol)
    basket.add(sil)
    basket.add(gol)

    print(f"size = {basket.size}")

    print(basket)

 #   total = Score.calculate_total_price(basket)

 #   print(f"Total price = {total}")


if __name__ == "__main__":
    main()
