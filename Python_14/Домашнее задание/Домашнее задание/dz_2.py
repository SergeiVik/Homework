# Задача 2
class CurrencyConversion:
    count = 0

    def __init__(self):
        CurrencyConversion.count += 1

    @staticmethod
    def currency_celsius(celsius):
        CurrencyConversion.count += 1
        return 1.8 * celsius + 32

    @staticmethod
    def currency_fahrengeit(fahrengeit):
        CurrencyConversion.count += 1
        return (fahrengeit - 32) * (5 / 9)

    @staticmethod
    def get_count_currency():
        return CurrencyConversion.count


print(CurrencyConversion.currency_celsius(25))
print(CurrencyConversion.currency_fahrengeit(77))
print(CurrencyConversion.get_count_currency())
