"""Prosty kalkulator zgodny z diagramem UML z laboratorium."""


class Calculator:
    """Kalkulator wykonujący podstawowe działania na dwóch operandach.

    Operandy są polami prywatnymi ("-" w UML), w Pythonie realizowanymi
    przez podwójne podkreślenie (name mangling).
    """

    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """Zwraca sumę operandów."""
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """Zwraca różnicę operandów (op1 - op2)."""
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """Zwraca iloczyn operandów."""
        return self.__op1 * self.__op2

    def divide(self) -> float:
        """Zwraca iloraz operandów (op1 / op2).

        Raises:
            ZeroDivisionError: gdy op2 jest równe 0.
        """
        if self.__op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")
        return self.__op1 / self.__op2


if __name__ == "__main__":
    # Przykłady wywołania
    calc = Calculator(10, 4)
    print("10 + 4 =", calc.sum())
    print("10 - 4 =", calc.subtract())
    print("10 * 4 =", calc.multiply())
    print("10 / 4 =", calc.divide())

    # Przypadek szczególny: dzielenie przez zero
    try:
        Calculator(10, 0).divide()
    except ZeroDivisionError as error:
        print("10 / 0 -> błąd:", error)
