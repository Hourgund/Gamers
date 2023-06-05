from Containers.player import Players
from Logic.score import Score


class FirstPlace:
    @staticmethod
    def find_max_total(total1):
        totals = []
        max_total = 0
        # highest result
        for i in range(len(totals)):
            total1 = totals[i]
            if totals[i] > max_total:
                max_total = totals[i]

        return max_total
