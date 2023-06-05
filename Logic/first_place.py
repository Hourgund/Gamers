from Util.main import main
from Containers.player import Players
from Logic.score import Score


class FirstPlace:
    @staticmethod
    def find_max_total(score, player):
        if isinstance(score, Score) and score.calculate_total_price(player) != 0:
            totals = []
            max_total = totals[2]
            # highest result
            for i in range(len(totals)):
                if totals[i] > max_total:
                    max_total = totals[i]
            return max_total

        else:
            return 0
