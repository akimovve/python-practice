from practice04_extra.part1.expression_trees.models.Operation import Operation


class Add(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit) + int(self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('ADD')

    def __str__(self) -> str:
        return '({} + {})'.format(self.num1, self.num2)
