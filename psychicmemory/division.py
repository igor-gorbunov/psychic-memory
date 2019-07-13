from .operation import Operation


class Division(Operation):
    def execute(self, left, right):
        return left / right
