from .operation import Operation


class Multiplication(Operation):
    def execute(self, left, right):
        return left * right
