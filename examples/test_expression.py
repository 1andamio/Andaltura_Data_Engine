from primer.query.expression import Expression


class IsEven(Expression[int]):

    def evaluate(self, value: int) -> bool:
        return value % 2 == 0


class GreaterThanFive(Expression[int]):

    def evaluate(self, value: int) -> bool:
        return value > 5


expr = IsEven() & GreaterThanFive()

for i in range(10):
    if expr(i):
        print(i)