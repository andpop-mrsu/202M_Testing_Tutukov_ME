import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
def test_equilateral_triangle():
    """Проверка корректного создания и работы методов для равностороннего треугольника"""
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == 'equilateral'
    assert triangle.perimeter() == 9

def test_isosceles_triangle():
    """Проверка корректного создания и работы методов для равнобедренного треугольника"""
    triangle = Triangle(4, 4, 3)
    assert triangle.triangle_type() == 'isosceles'
    assert triangle.perimeter() == 11

def test_nonequilateral_triangle():
    """Проверка корректного создания и работы методов для разностороннего треугольника"""
    triangle = Triangle(5, 6, 7)
    assert triangle.triangle_type() == 'nonequilateral'
    assert triangle.perimeter() == 18

# Негативные тесты
def test_zero_side():
    """Проверка, что нулевая длина стороны приводит к выбросу исключения"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_negative_side():
    """Проверка, что отрицательная длина стороны приводит к выбросу исключения"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 4, 5)

def test_invalid_triangle_inequality():
    """Проверка нарушения неравенства треугольника"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_non_numeric_input():
    """Проверка, что нечисловой ввод приводит к выбросу исключения"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 5, 5)

def test_large_side():
    """Проверка, что слишком большая сторона приводит к выбросу исключения (нарушение треугольного неравенства)"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 1, 1)

