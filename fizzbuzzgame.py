class FizzBuzzGame:
    def play(self, number):
        if self.is_fizzbuzzable(number):
            return "FizzBuzz"

        if self.is_fizzable(number):
            return "Fizz"

        if self.is_buzzable(number):
            return "Buzz"

        return number

    def is_fizzbuzzable(self, number):
        return self.is_fizzable(number) and self.is_buzzable(number)

    def is_buzzable(self, number):
        return self.is_divisable_by_5(number)

    def is_fizzable(self, number):
        return self.is_divisable_by_3(number)

    def is_divisable_by_5(self, number):
        return number % 5 == 0

    def is_divisable_by_3(self, number):
        return number % 3 == 0
