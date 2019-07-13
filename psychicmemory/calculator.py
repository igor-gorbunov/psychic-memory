from . import operation


class Calculator:
    def __init__(self):
        pass

    def proceed_queue(self, commands):
        stack = []
        for item in commands:
            if isinstance(item, operation.Operation):
                right = stack.pop()
                left = stack.pop()
                result = item.execute(left, right)
                stack.append(result)
            else:
                stack.append(item)
        return stack.pop()
