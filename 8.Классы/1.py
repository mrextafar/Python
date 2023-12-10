class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        sum_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        sum_denominator = self.denominator * other.denominator

        gcd = self.gcd2(sum_numerator, sum_denominator)

        return Fraction(sum_numerator // gcd, sum_denominator // gcd)

    def __sub__(self, other):
        difference_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        difference_denominator = self.denominator * other.denominator

        gcd = self.gcd2(difference_numerator, difference_denominator)

        return Fraction(difference_numerator // gcd, difference_denominator // gcd)

    def __mul__(self, other):
        product_numerator = self.numerator * other.numerator
        product_denominator = self.denominator * other.denominator

        gcd = self.gcd2(product_numerator, product_denominator)

        return Fraction(product_numerator // gcd, product_denominator // gcd)

    def __truediv__(self, other):
        quotient_numerator = self.numerator * other.denominator
        quotient_denominator = self.denominator * other.numerator

        gcd = self.gcd2(quotient_numerator, quotient_denominator)

        return Fraction(quotient_numerator // gcd, quotient_denominator // gcd)

    def gcd2(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        return Fraction(self.numerator // self.gcd(), self.denominator // self.gcd())


if __name__ == "__main__":
    a = Fraction(1, 4)
    b = Fraction(1, 8)

    print(a + b)
    # Выведет: 3/8

    print(a - b)
    # Выведет: 1/8

    print(a * b)
    # Выведет: 1/8

    print(a / b)
    # Выведет: 2/3
