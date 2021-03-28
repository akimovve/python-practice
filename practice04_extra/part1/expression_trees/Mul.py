from practice04_extra.part1.expression_trees.Operation import Operation


class Mul(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def count(self):
        return int(self.num1.digit) * int(self.num2.digit)
