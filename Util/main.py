from Entity.bronze import Bronze
from Entity.silver import Silver
from Entity.gold import Gold
from Containers.player import Players
from Logic.score import Score
from Logic.table_of_leaders import Table


def main():
    player = Players()

    br = Bronze(1, 10.0)
    sil = Silver(5, 15.0)
    gol = Gold(10, 20.0)

    player.add(sil)
    player.add(gol)
    player.add(sil)
    player.add(gol)
    player.add(sil)
    player.add(gol)

    print(f"size = {player.size}")

    print(player)

    total = Score.calculate_total_price(player)

    print(f"Total price = {total}")

    Min_total = Table.find_min_total()

if __name__ == "__main__":
    main()
