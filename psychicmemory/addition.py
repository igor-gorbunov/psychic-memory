from .operation import Operation


class Addition(Operation):
    def execute(self, left, right):
        return left + right
