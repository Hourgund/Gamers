from Entity.bronze import Bronze
from Entity.silver import Silver
from Entity.gold import Gold
from Containers.player import Players
from Logic.score import Score
from Logic.first_place import FirstPlace


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

    max_total = FirstPlace.find_max_total(total1)
    max_total = FirstPlace.find_max_total(total2)

    print(f"Total price of first player = {total1}")
    print(f"Total price of second player = {total2}")
    print(f"The biggest result is ", max_total)


if __name__ == "__main__":
    main()
