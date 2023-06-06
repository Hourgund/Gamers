from Logic.score import Score


class LastPlace:
    @staticmethod
    def find_min_score(scores):
        for score in scores:
            if isinstance(score, Score):
                score.calculate_price_the_price_of_score(score)
                min_score = scores[0]
                for i in range(len(scores)):
                    if min_score > scores[i]:
                        min_score = scores[i]
                        msg_min = ("The highest result is ", min_score)
                        return msg_min
