import unittest

from psychicmemory import calculator, addition, subtraction, multiplication, division


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_addition(self):
        plus = addition.Addition()

        commands = (0, 0, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = (0, 1, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = (1, 0, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = (1, 1, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 2)

        commands = (2000, 8000, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 10000)

        commands = (8000, 2000, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 10000)

        commands = (1, 2, 3, 4, 5, plus, plus, plus, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 15)

        commands = (1, 2, plus, 3, plus, 4, plus, 5, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 15)

    def test_subtraction(self):
        minus = subtraction.Subtraction()

        commands = [0, 0, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [1, 0, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = [0, 1, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -1)

        commands = [1, 1, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [10, 3, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 7)

        commands = [3, 10, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -7)

        commands = [2000, 8000, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -6000)

        commands = [8000, 2000, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 6000)

        commands = [1, 2, minus, 3, minus, 4, minus, 5, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -13)

        commands = [1, 2, 3, 4, 5, minus, minus, minus, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 3)

        commands = [1, 2, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -1)

        commands = [5, 4, minus, 3, minus, 2, minus, 1, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), -5)

        commands = [15, 4, 3, 2, 1, minus, minus, minus, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 13)

        commands = [15, 4, minus, 3, minus, 2, minus, 1, minus]
        self.assertEqual(self.calculator.proceed_queue(commands), 5)

    def test_multiplication(self):
        multiply = multiplication.Multiplication()

        commands = [0, 0, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [0, 1, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [1, 0, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [1, 1, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = [2000, 8000, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 16000000)

        commands = [8000, 2000, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 16000000)

        commands = [1, 2, 3, 4, 5, multiply, multiply, multiply, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 120)

        commands = [1, 2, multiply, 3, multiply, 4, multiply, 5, multiply]
        self.assertEqual(self.calculator.proceed_queue(commands), 120)

    def test_division(self):
        divide = division.Division()

        commands = [0, 1, divide]
        self.assertEqual(self.calculator.proceed_queue(commands), 0)

        commands = [1, 1, divide]
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = [100, 1, divide]
        self.assertEqual(self.calculator.proceed_queue(commands), 100)

        commands = [100, 100, divide]
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

        commands = [1000, 10, divide, 10, divide, 10, divide]
        self.assertEqual(self.calculator.proceed_queue(commands), 1)

    def test_mixed(self):
        plus = addition.Addition()
        minus = subtraction.Subtraction()
        multiply = multiplication.Multiplication()
        divide = division.Division()

        commands = (4, 5, 7, 2, plus, minus, multiply)
        self.assertEqual(self.calculator.proceed_queue(commands), -16)

        commands = (3, 4, plus, 2, multiply, 7, divide)
        self.assertEqual(self.calculator.proceed_queue(commands), 2)

        commands = (5, 7, plus, 6, 2, minus, multiply)
        self.assertEqual(self.calculator.proceed_queue(commands), 48)

        commands = (4, 2, 3, 5, 1, minus, plus, multiply, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 18)

        commands = (4, 2, plus, 3, 5, 1, minus, multiply, plus)
        self.assertEqual(self.calculator.proceed_queue(commands), 18)


if __name__ == "__main__":
    unittest.main()
