from Entity.bronze import Bronze
from Entity.silver import Silver
from Entity.gold import Gold
from Containers.player import Players
from Logic.score import Score
from Logic.first_place import FirstPlace


# from operator import attrgetter


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

    score1 = Score.calculate_price_the_price_of_score(player1)
    score2 = Score.calculate_price_the_price_of_score(player2)

    print(f"Total price of first player = {score1}")
    print(f"Total price of second player = {score2}")

    scores = (score1, score2)
    # max_total = max(totals)
    max_score = FirstPlace.find_max_score(scores)
    print(f"The biggest result is", max_score)


if __name__ == "__main__":
    main()
