class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по его сторонам.

    Аргументы:
    a, b, c -- длины сторон треугольника

    Возвращает строку с типом треугольника: "nonequilateral", "isosceles", "equilateral".

    Исключения:
    IncorrectTriangleSides -- если стороны не могут образовать треугольник.

    Примеры:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'

    >>> get_triangle_type(4, 4, 3)
    'isosceles'

    >>> get_triangle_type(5, 6, 7)
    'nonequilateral'

    >>> get_triangle_type(0, 4, 5)  # Некорректный: одна из сторон нулевая
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Длинны сторон должны быть положительными числами.

    >>> get_triangle_type(1, 2, 3)  # Некорректный: не удовлетворяет неравенству треугольника
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны не удовлетворяют неравенству треугольника.

    >>> get_triangle_type("a", 5, 5)  # Некорректный: одна из сторон не число
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Каждая сторона должна быть числом.
    """

    # Проверка на корректность переданных аргументов
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise IncorrectTriangleSides("Каждая сторона должна быть числом.")

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Длинны сторон должны быть положительными числами.")

    # Проверка неравенства треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника.")

    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
