class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass

class Triangle:
    def __init__(self, a, b, c):
        """Конструктор, принимающий длины сторон треугольника.

        Выбрасывает IncorrectTriangleSides, если переданные длины не могут сформировать треугольник.
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            raise IncorrectTriangleSides("Каждая сторона должна быть числом.")

        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Длинны сторон должны быть положительными числами.")

        if not (a + b > c and a + c > b and b + c > a):
            raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника.")

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        """Возвращает тип треугольника как строку: 'nonequilateral', 'isosceles' или 'equilateral'."""
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        """Вычисляет и возвращает периметр треугольника."""
        return self.a + self.b + self.c

if __name__ == "__main__":
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.triangle_type())
        print(triangle.perimeter())
    except IncorrectTriangleSides as e:
        print(f"Ошибка: {e}")
