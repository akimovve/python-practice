'''
Задача 2. Реализовать конечный автомат Мили в виде класса C32. Начальным состоянием
автомата является A. Методы возвращают числовые значения. Если вызываемый метод не реализован
для некоторого состояния, необходимо вызвать исключение RuntimeError.
'''


class C32:
    def __init__(self):
        self.state = AState(self)

    def peek(self):
        return self.state.peek()

    def trace(self):
        return self.state.trace()

    def chat(self):
        return self.state.chat()


# Главный класс конечного автомата Мили
class MileMachineState:
    def __init__(self, root):
        self.root = root

    def peek(self):
        # print('RuntimeError')
        raise RuntimeError

    def trace(self):
        # print('RuntimeError')
        raise RuntimeError

    def chat(self):
        # print('RuntimeError')
        raise RuntimeError


# Состояние A
class AState(MileMachineState):
    def peek(self):
        self.root.state = BState(self.root)
        # print(0)
        return 0


# Состояние B
class BState(MileMachineState):
    def chat(self):
        self.root.state = CState(self.root)
        # print(1)
        return 1


# Состояние C
class CState(MileMachineState):
    def peek(self):
        self.root.state = CState(self.root)
        # print(4)
        return 4

    def trace(self):
        self.root.state = FState(self.root)
        # print(3)
        return 3

    def chat(self):
        self.root.state = DState(self.root)
        print(2)
        return 2


# Состояние D
class DState(MileMachineState):
    def peek(self):
        self.root.state = EState(self.root)
        # print(5)
        return 5

    def trace(self):
        self.root.state = AState(self.root)
        # print(6)
        return 6

    def chat(self):
        self.root.state = BState(self.root)
        # print(7)
        return 7


# Состояние E
class EState(MileMachineState):
    def peek(self):
        self.root.state = FState(self.root)
        # print(8)
        return 8


# Состояние F
class FState(MileMachineState):
    pass


if __name__ == '__main__':
    o = C32()
    o.peek()
    o.chat()
    o.peek()
    o.chat()
    o.trace()
    o.trace()
    o.peek()
    o.chat()
    o.chat()
    o.peek()
    o.trace()
    o.peek()

    o = C32()
    o.peek()
    o.chat()
    o.peek()
    o.chat()
    o.trace()
    o.peek()
    o.chat()
    o.chat()
    o.chat()
    o.chat()
    o.peek()
    o.trace()
