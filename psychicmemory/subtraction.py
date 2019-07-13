from .operation import Operation


class Subtraction(Operation):
    def execute(self, left, right):
        return left - right
