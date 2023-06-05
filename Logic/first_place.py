from Logic.score import Score


class FirstPlace:
    @staticmethod
    def find_max_total(total):
        totals = []
        for _ in range(len(totals)):
            a = Score.calculate_total_price(totals)
            totals.append(int(a))
        max_total = totals[0]
        for i in totals:
            if max_total < total[i]:
                max_total = totals[i]

        return max_total
