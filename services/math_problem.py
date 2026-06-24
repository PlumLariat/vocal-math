from random import randint

from constants import Difficulty, Type

class MathProblem:
    def __init__(self, level: Difficulty, type: Type) -> None:
        self.operand1 = 0
        self.operand2 = 0
        self.answer = 0
        if level == Difficulty.EASY:
            self._min_digits = 1
            self._max_digits = 3
        elif level == Difficulty.MEDIUM:
            self._min_digits = 4
            self._max_digits = 6
        elif level == Difficulty.HARD:
            self._min_digits = 7
            self._max_digits = 9

    def get_operand1(self) -> int:
        return self.operand1
    
    def get_operand2(self) -> int:
        return self.operand2

    def get_answer(self) -> int:
        return self.answer
    
    def _init_easy(self, type:Type) -> tuple[int, int, int]:
        num1 = randint(1, 999)
        num2 = randint(1, 999)
        answer = 0

        if type == Type.ADDITION:
            answer = num1 + num2
        if type == Type.SUBTRACTION:
            answer = num1 - num2
        if type == Type.MULTIPLICATION:
            answer = num1 * num2
        if type == Type.DIVISION:
            answer = num1 // num2

        return num1, num2, answer


