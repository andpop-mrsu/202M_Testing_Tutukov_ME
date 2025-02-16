import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):

    def test_equilateral_triangle(self):
        """Проверка равностороннего треугольника"""
        self.assertEqual(get_triangle_type(3, 3, 3), 'equilateral')

    def test_isosceles_triangle(self):
        """Проверка равнобедренного треугольника"""
        self.assertEqual(get_triangle_type(4, 4, 3), 'isosceles')

    def test_nonequilateral_triangle(self):
        """Проверка разностороннего треугольника"""
        self.assertEqual(get_triangle_type(5, 6, 7), 'nonequilateral')

    def test_zero_side(self):
        """Проверка, что нулевая сторона вызывает исключение"""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

    def test_negative_side(self):
        """Проверка, что отрицательная сторона вызывает исключение"""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 4, 5)

    def test_invalid_triangle_inequality(self):
        """Проверка неравенства треугольника"""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_non_numeric_input(self):
        """Проверка нечислового входа"""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 5, 5)

    def test_large_side(self):
        """Проверка, что слишком большая сторона вызывает исключение"""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 1)

if __name__ == "__main__":
    unittest.main()
