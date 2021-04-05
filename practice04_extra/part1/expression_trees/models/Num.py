class Num:
    def __init__(self, digit):
        self.digit = digit

    def stack(self):
        print('PUSH ' + str(self.digit))

    def __str__(self) -> str:
        return str(self.digit)
