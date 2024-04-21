# Задание 1
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    @staticmethod
    def get_instans_count():
        return Fraction.count

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def sum(self, other):
        new_numerator = (self.numerator * other.denominator +
                         self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator / common_part,
                        new_denominator / common_part)

    def subtract(self, other):
        new_numerator = (self.numerator * other.denominator -
                         self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator / common_part,
                        new_denominator / common_part)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator / common_part,
                        new_denominator / common_part)

    def divide(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator / common_part,
                        new_denominator / common_part)

    # Специальный метод / Магический метод / Dunder method - Double underscore method
    def __str__(self):
        return f'{int(self.numerator)}/{int(self.denominator)}'


a = Fraction(14, 22)
b = Fraction(17, 34)

print(Fraction.get_instans_count())
