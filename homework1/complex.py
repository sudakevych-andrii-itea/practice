class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}j'
        else:
            return f'{self.real} - {abs(self.imag)}j'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real + self.imag * other.imag * -1,
                             self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        numerator_real = self.real * other.real + self.imag * -other.imag * -1
        numerator_imag = self.real * -other.imag + self.imag * other.real
        denominator = other.real * other.real + other.imag * other.imag
        return ComplexNumber(round(numerator_real / denominator, 2), round(numerator_imag / denominator, 2))
