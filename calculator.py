class Calculator:
    def __init__(self, op1: float, op2: float):
        # "-" w UML oznacza atrybut prywatny -> w Pythonie podwójne podkreślenie
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        return self.__op1 * self.__op2

    def divide(self) -> float:
        if self.__op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")
        return self.__op1 / self.__op2

