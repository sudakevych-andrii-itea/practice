class Dot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Dot(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Dot(self.x / other.x, self.y / other.y, self.z / other.z)

    def __neg__(self):
        return Dot(-self.x, -self.y, -self.z)


if __name__ == '__main__':
    dot1 = Dot(1, 2, 3)
    dot2 = Dot(1, 2, 3)
    print(dot1 + dot2)
    print(dot1 - dot2)
    print(dot1 * dot2)
    print(dot1 / dot2)
