import math


class SimpleSequenceCalc:

    @staticmethod
    def sqrt_from_avg_of_sequence(seq: list) -> float:

        #if 0 in seq:
            #raise ZeroDivisionError
        #if (math.prod(seq) or sum(seq)) < 0:
            #raise ValueError

        return math.sqrt(sum(seq)/math.prod(seq))

print(SimpleSequenceCalc.sqrt_from_avg_of_sequence([-7,1]))