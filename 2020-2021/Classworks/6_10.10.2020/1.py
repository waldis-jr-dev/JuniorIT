class Number:
    def __init__(self, digit):
        self.digit = digit

    def addition(self, num):
        return Number(self.digit + num)

    def subtraction(self, num):
        return Number(self.digit - num)

    def multiplication(self, num):
        return Number(self.digit * num)

    def division(self, num):
        return Number(self.digit / num) if num != 0 else Number(self.digit)


a = Number(5)
b = a.division(0)
print(b.digit)
