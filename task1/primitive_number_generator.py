from dataclasses import dataclass
import random
from math import sqrt


@dataclass
class NumberGenerator:
    length: int

    def __generate_bits(self):
        """This function is to generate bits sequence as List[str], where int can be 0 or 1"""
        self.bits_sequence = [str(random.randint(0, 1)) for _ in range(self.length // 2 - 1)]
        self.bits_sequence = ['1'] + self.bits_sequence

    def generate_number(self) -> int:
        """Function return number from generated bits sequence"""
        self.__generate_bits()
        _bits_sequence = "".join(self.bits_sequence)
        return int(_bits_sequence, 2)

    def __call__(self):
        """When call class generate number"""
        self.generate_number()

    def __str__(self):
        return f'{self.bits_sequence}'


@dataclass
class FermatTester:
    """This class is realisation of Fermat's test for numbers (check if they primitive):
    https://en.wikipedia.org/wiki/Fermat%27s_little_theorem \n
    k: int
        this parameter shows how much we should test to be sure that number is primitive"""
    number: int
    k: int

    def check_condition(self, a: int) -> bool:
        """
        The checking conditions is a ** (T - 1) mod T = 1 \n
        Args:
            a: number that less than checking number (i.e. self.number)

        Returns:
            True when condition is correct, else False
        """
        if pow(a, self.number - 1, self.number) == 1:
            return True
        else:
            return False


@dataclass
class PrimeNumberGenerator(NumberGenerator, FermatTester):

    def get_primitive_number(self):
        self.number = self.generate_number()
        cnt = 0
        while cnt < self.k:
            random_num = random.randint(2, int(sqrt(self.number)))

            if self.check_condition(random_num):
                cnt += 1
            else:
                self.number = self.generate_number()

        return self.number

    def __call__(self):
        return self.get_primitive_number()


if __name__ == '__main__':
    png = PrimeNumberGenerator(length=64, number=0, k=10)
    print(png())
