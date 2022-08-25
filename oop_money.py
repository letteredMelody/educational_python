class Money:
    def __init__(self, initial_sum):
        self.sum = initial_sum

    def __add__(self, other):
        return Money(self.sum + other.sum)

    def __sub__(self, other):
        return Money(self.sum - other.sum)

    def __lt__(self, other):
        return self.sum < other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __eq__(self, other):
        return self.sum == other.sum

class Dollar(Money):
    def __init__(self, initial_sum):
        super().__init__(initial_sum * 71.2)
    def rubles(self):
        return self.sum

class Ruble(Money):
    def dollars(self):
        return self.sum / 71.2

money_1 = Dollar(10)
money_2 = Ruble(10)
print(money_1 > money_2)
