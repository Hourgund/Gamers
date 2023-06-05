from Entity.bronze import Bronze
from Entity.silver import Silver
from Entity.gold import Gold
from Containers.player import Players
from Logic.score import Score
from Logic.table_of_leaders import Table


def main():
    player = Players()
    player1 = Players()
    player2 = Players()

    br = Bronze(1, 10.0)
    sil = Silver(5, 15.0)
    gol = Gold(10, 20.0)

    player.add(br)
    player.add(sil)
    player.add(gol)

    player1.add(sil)
    player1.add(gol)
    player1.add(gol)

    player2.add(sil)
    player2.add(gol)
    player2.add(sil)
    player2.add(gol)

    print(f"size = {player1.size}")
    print(f"size = {player2.size}")

    print(player)

    total1 = Score.calculate_total_price(player1)
    total2 = Score.calculate_total_price(player2)

    print(f"Total price = {total1}")
    print(f"Total price = {total2}")

    totals = [total1, total2]

    Minimum_total = Table.find_min_total(totals)
    Maximum_total = Table.find_max_total(totals)

    print(f"The biggest resoult is ", Maximum_total)
    print(f"The smallest resoult is ", Minimum_total)


if __name__ == "__main__":
    main()
