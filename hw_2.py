class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}")


if __name__ == "__main__":
    figures = [
        Square(4),      # Квадрат со стороной 4 см
        Square(7),      # Квадрат со стороной 7 см
        Rectangle(5, 8),  # Прямоугольник 5х8 см
        Rectangle(6, 9),  # Прямоугольник 6х9 см
        Rectangle(3, 12)  # Прямоугольник 3х12 см
    ]

    for figure in figures:
        figure.info()
