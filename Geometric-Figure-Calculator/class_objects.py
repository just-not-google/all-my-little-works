import math


class Figure:
    def __init__(self, radius=None, d_1=None, d_2=None,
                 side=None, length=None, width=None, side_a=None, side_b=None, side_c=None,
                 h_a=None, h_b=None, h_c=None, angle_a=None, angle_b=None, angle_c=None, base=None, leg=None,
                 any_interior_angle=None, semi_minor_axis=None,
                 base_a=None, base_b=None, leg_c=None, leg_d=None, semi_major_axis=None):
        self.radius = radius
        self.side = side
        self.length = length
        self.width = width
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.h_a = h_a
        self.h_b = h_b
        self.h_c = h_c
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.base = base
        self.leg = leg
        self.any_interior_angle = any_interior_angle
        self.base_a = base_a
        self.base_b = base_b
        self.leg_c = leg_c
        self.leg_d = leg_d
        self.d_1 = d_1
        self.d_2 = d_2
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis


class Circle(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def diameter(self):
        return self.radius * 2 if self.radius else None

    @property
    def circumference(self):
        return 2 * math.pi * self.radius if self.radius else None

    @property
    def area(self):
        return math.pi * self.radius ** 2 if self.radius else None

    def __str__(self):
        return (f"Окружность\n"
                f"Диаметр: {self.diameter or 'N/A'}\n"
                f"Длина окружности: {self.circumference or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Square(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def diagonal(self):
        return self.side * math.sqrt(2) if self.side else None

    @property
    def area(self):
        return self.side ** 2 if self.side else None

    @property
    def perimeter(self):
        return self.side * 4 if self.side else None

    def __str__(self):
        return (f"Квадрат\n"
                f"Диагональ: {self.diagonal or 'N/A'}\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Rectangle(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def diagonal(self):
        return math.sqrt(self.length ** 2 + self.width ** 2) if self.length and self.width else None

    @property
    def perimeter(self):
        return 2 * (self.length + self.width) if self.length and self.width else None

    @property
    def area(self):
        return self.length * self.width if self.length and self.width else None

    def __str__(self):
        return (f"Прямоугольник\n"
                f"Диагональ: {self.diagonal or 'N/A'}\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Triangle(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def perimeter(self):
        if self.side_a and self.side_b and self.side_c:
            if (self.side_a + self.side_b > self.side_c and
                self.side_b + self.side_c > self.side_a and
                self.side_a + self.side_c > self.side_b):
                return self.side_a + self.side_b + self.side_c
        return None

    @property
    def area(self):
        if self.side_a and self.side_b and self.side_c:
            if (self.side_a + self.side_b > self.side_c and
                self.side_b + self.side_c > self.side_a and
                self.side_a + self.side_c > self.side_b):
                p = self.perimeter / 2
                return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        elif self.side_a and self.h_a:
            return 0.5 * self.side_a * self.h_a
        elif self.side_b and self.h_b:
            return 0.5 * self.side_b * self.h_b
        elif self.side_c and self.h_c:
            return 0.5 * self.side_c * self.h_c
        elif self.side_a and self.side_b and self.angle_c:
            return 0.5 * self.side_a * self.side_b * math.sin(math.radians(self.angle_c))
        return None

    def __str__(self):
        return (f"Треугольник\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class IsoscelesTriangle(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def altitude(self):
        return math.sqrt(self.leg ** 2 - (self.base / 2) ** 2) if self.base and self.leg else None

    @property
    def perimeter(self):
        return self.base + 2 * self.leg if self.base and self.leg else None

    @property
    def area(self):
        return 0.5 * self.base * self.altitude if self.base and self.altitude else None

    def __str__(self):
        return (f"Равнобедренный треугольник\n"
                f"Высота: {self.altitude or 'N/A'}\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class EquilateralTriangle(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def altitude(self):
        return (self.side * math.sqrt(3)) / 2 if self.side else None

    @property
    def perimeter(self):
        return 3 * self.side if self.side else None

    @property
    def area(self):
        return (self.side ** 2 * math.sqrt(3)) / 4 if self.side else None

    def __str__(self):
        return (f"Равносторонний треугольник\n"
                f"Высота: {self.altitude or 'N/A'}\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Parallelogram(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b) if self.side_a and self.side_b else None

    @property
    def area(self):
        if self.side_a and self.h_a:
            return self.side_a * self.h_a
        elif self.side_a and self.side_b and self.angle_a:
            return self.side_a * self.side_b * math.sin(math.radians(self.angle_a))
        return None

    def __str__(self):
        return (f"Параллелограмм\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Rhombus(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def perimeter(self):
        return 4 * self.side_a if self.side_a else None

    @property
    def area(self):
        if self.d_1 and self.d_2:
            return (self.d_1 * self.d_2) / 2
        elif self.side_a and self.h_a:
            return self.side_a * self.h_a
        elif self.side_a and self.any_interior_angle:
            return self.side_a ** 2 * math.sin(math.radians(self.any_interior_angle))
        return None

    def __str__(self):
        return (f"Ромб\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Trapezium(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def perimeter(self):
        return self.base_a + self.base_b + self.leg_c + self.leg_d if self.base_a and self.base_b and self.leg_c and self.leg_d else None

    @property
    def mid_segment(self):
        return (self.base_a + self.base_b) / 2 if self.base_a and self.base_b else None

    @property
    def area(self):
        return ((self.base_a + self.base_b) / 2) * self.h_a if self.base_a and self.base_b and self.h_a else None

    def __str__(self):
        return (f"Трапеция\n"
                f"Средняя линия: {self.mid_segment or 'N/A'}\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


class Ellipse(Figure):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis if self.semi_major_axis and self.semi_minor_axis else None

    @property
    def perimeter(self):
        if self.semi_major_axis and self.semi_minor_axis:
            a, b = self.semi_major_axis, self.semi_minor_axis
            return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
        return None

    def __str__(self):
        return (f"Эллипс\n"
                f"Периметр: {self.perimeter or 'N/A'}\n"
                f"Площадь: {self.area or 'N/A'}\n")


if __name__ == "__main__":
    figure = Figure(
        radius=5,
        d_1=8,
        d_2=6,
        side=10,
        length=15,
        width=8,
        side_a=5,
        side_b=7,
        side_c=9,
        h_a=4,
        h_b=5,
        h_c=6,
        angle_a=45,
        angle_b=60,
        angle_c=75,
        base=12,
        leg=10,
        any_interior_angle=120,
        semi_minor_axis=4,
        base_a=8,
        base_b=12,
        leg_c=5,
        leg_d=5,
        semi_major_axis=6
    )

    figure_dict = figure.__dict__.copy()

    circle_1 = Circle(**figure_dict)
    square_1 = Square(**figure_dict)
    rectangle_1 = Rectangle(**figure_dict)
    triangle_1 = Triangle(**figure_dict)
    isosceles_triangle_1 = IsoscelesTriangle(**figure_dict)
    equilateral_triangle_1 = EquilateralTriangle(**figure_dict)
    parallelogram_1 = Parallelogram(**figure_dict)
    rhombus_1 = Rhombus(**figure_dict)
    trapezium_1 = Trapezium(**figure_dict)
    ellipse_1 = Ellipse(**figure_dict)

    print(circle_1)
    print(square_1)
    print(rectangle_1)
    print(triangle_1)
    print(isosceles_triangle_1)
    print(equilateral_triangle_1)
    print(parallelogram_1)
    print(rhombus_1)
    print(trapezium_1)
    print(ellipse_1)