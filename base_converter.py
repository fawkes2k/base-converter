class BaseConverter:
    def __init__(self, base: int, base_digits: str):
        """
        Creates a conversion object between a positional numeral system in given base and decimal

        :param base: A base of that positional numeral system in decimal (only natural numbers allowed)
        :param base_digits: Digits used in that positional numeral system
        :return: A conversion object
        """
        if base <= 1 or base % 1 != 0:
            raise Exception(f'{base} is not a natural number or/and not greater than 1')
        if len(base_digits) != base:
            raise Exception(f'The number of digits ({len(base_digits)}) and base ({base}) do not match')
        self.base, self.digits = base, base_digits

    def decimal_to_base(self, number: int) -> str:
        """
        Converting a natural number in decimal to given positional numeral system

        :param number: A natural number in decimal
        :return: A number in given positional numeral system
        """
        from math import log
        if number < 0 or number % 1 != 0: raise Exception(f'{number} is not a natural number')
        if number == 0: return self.digits[number]
        length, final = int(log(number) / log(self.base) + 1), ''
        for power in range(length):
            character = self.digits[number // self.base**power % self.base]
            final += character
        return final[::-1]

    def base_to_decimal(self, number: str) -> int:
        """
        Converting a natural number in given positional numeral system to decimal

        :param number: A natural number in given positional numeral system
        :return: A number in decimal
        """
        for digit in number:
            if digit not in self.digits: raise Exception(f"Digit '{digit}' is not used by this numberal system")
        length, decimal = len(number), 0
        for index in range(length): decimal += self.digits.find(number[length - index - 1]) * self.base**index
        return decimal