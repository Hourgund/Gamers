from Containers.player import Players
from Logic.score import Score


class Table:
    ls1 = [Score.calculate_total_price(player=12),
           Score.calculate_total_price(player=16)]
    # elements of the list
    for i in range(2):
        n = Score.calculate_total_price(player=12)
        n = Score.calculate_total_price(player=16)
        ls1.append(n)
    print(ls1)

    def find_min_total(self, ls1):
        min_total = ls1[0]
        # lowest result
        for i in range(len(ls1)):
            if ls1[i] < min_total:
                min_total = ls1[i]
            msg_min = ("The smallest result is ", min_total)
        return msg_min

    def find_max_total(self, ls1):
        max_total = ls1[0]
        # highest result
        for i in range(len(ls1)):
            if ls1[i] > max_total:
                max_total = ls1[i]
            msg_max = ("The highest result is ", max_total)
        return msg_max

# t1 = Score.calculate_total_price_first_player(player1)
# t2 = Score.calculate_total_price_first_player(player2)
# result = 0
# if (t1 > t2):
#  result = ("Player {Player1.name} won!!!
# Player {Player2.name} good luck next time!")
# elif (t2 >t1):
#  result = ("Player {Player2.name} won!!!
# Player {Player1.name} good luck next time!")
# elif:
# msg = ("Its a Draw! Friendship won!!!)
