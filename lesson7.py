# number1
a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 1\n{matrix_2}\n{'*' * 20}")

# number2

from abc import ABC, abstractmethod
class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5
class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)

coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

# number3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['😎' * rows for _ in range(self.nums // rows)]) + '\n' + '🤖' * (self.nums % rows)
    def __str__(self):
        return f"{self.nums}"
    def __add__(self, other):
        print('Sum of cells is: ')
        return Cell(self.nums - other.nums)
    def __sub__(self, other):
        print("Substraction of cell is:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "ячеек в первой клетке меньше, чем во второй, вычитание невозможно!"
    def __mul__(self, other):
        print("Multiply of cell is:")
        return Cell(self.nums * other.nums)
    def __floordiv__(self, other):
        print("Truediv of cell is:")
        return Cell(self.nums // other.nums)
cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))