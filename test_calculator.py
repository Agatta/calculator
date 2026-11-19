"""Testy jednostkowe klasy Calculator."""
import runpy

import pytest

from calculator import Calculator


@pytest.mark.parametrize("op1, op2, expected", [
    (2, 5, 7),
    (-3, 3, 0),
    (-2, -4, -6),
    (0, 0, 0),
    (0.1, 0.2, 0.3),
])
def test_sum(op1, op2, expected):
    """Suma dla liczb dodatnich, ujemnych, zera i ułamków."""
    assert Calculator(op1, op2).sum() == pytest.approx(expected)


@pytest.mark.parametrize("op1, op2, expected", [
    (10, 4, 6),
    (4, 10, -6),
    (-2, -4, 2),
    (0, 0, 0),
    (0.3, 0.1, 0.2),
])
def test_subtract(op1, op2, expected):
    """Różnica, w tym wynik ujemny."""
    assert Calculator(op1, op2).subtract() == pytest.approx(expected)


@pytest.mark.parametrize("op1, op2, expected", [
    (10, 4, 40),
    (-3, 3, -9),
    (-2, -4, 8),
    (5, 0, 0),
    (1.5, 2, 3),
])
def test_multiply(op1, op2, expected):
    """Iloczyn, w tym mnożenie przez zero."""
    assert Calculator(op1, op2).multiply() == pytest.approx(expected)


@pytest.mark.parametrize("op1, op2, expected", [
    (10, 4, 2.5),
    (-9, 3, -3),
    (-8, -2, 4),
    (0, 5, 0),
    (1, 3, 0.3333333),
])
def test_divide(op1, op2, expected):
    """Iloraz, w tym wynik niecałkowity."""
    assert Calculator(op1, op2).divide() == pytest.approx(expected)


@pytest.mark.parametrize("op1", [0, 5, -5, 0.5])
def test_divide_by_zero_raises(op1):
    """Dzielenie przez zero zgłasza czytelny wyjątek."""
    with pytest.raises(ZeroDivisionError, match="Nie można dzielić przez zero"):
        Calculator(op1, 0).divide()


def test_operands_are_private():
    """Operandy nie są dostępne z zewnątrz klasy (pola prywatne z UML)."""
    calc = Calculator(1, 2)
    # Celowo odwołujemy się do nieistniejących/prywatnych pól.
    # pylint: disable=no-member,protected-access
    with pytest.raises(AttributeError):
        _ = calc.op1
    with pytest.raises(AttributeError):
        _ = calc.op2
    with pytest.raises(AttributeError):
        _ = calc.__op1


def test_operations_do_not_modify_operands():
    """Wywołanie działań nie zmienia stanu obiektu."""
    calc = Calculator(10, 4)
    calc.sum()
    calc.subtract()
    calc.multiply()
    calc.divide()
    assert calc.sum() == 14


def test_examples_run_without_errors(capsys):
    """Przykłady wywołania z calculator.py działają i obsługują dzielenie przez zero."""
    runpy.run_module("calculator", run_name="__main__")
    output = capsys.readouterr().out
    assert "10 + 4 = 14" in output
    assert "10 / 4 = 2.5" in output
    assert "10 / 0 -> błąd: Nie można dzielić przez zero" in output
