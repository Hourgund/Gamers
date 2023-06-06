from Logic.score import Score


class FirstPlace:
    @staticmethod
    def find_max_score(scores):
        for score in scores:
            if isinstance(score, Score):
                score.calculate_price_the_price_of_score(score)
                max_score = scores[0]
                for i in range(len(scores)):
                    if max_score < scores[i]:
                        max_score = scores[i]
                        msg_max = ("The highest result is ", max_score)
                        return msg_max

#    def find_max_total(total):
#        totals = []
#        for _ in range(len(totals)):
#            a = Score.calculate_total_price(totals)
#           totals.append(int(a))
#        max_total = totals[0]
#        for i in totals:
#            if max_total < total[i]:
#                max_total = totals[i]
#
#        return max_total
