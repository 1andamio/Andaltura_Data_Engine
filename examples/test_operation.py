from primer.query.operations.base import Operation


class Dummy(Operation):

    def apply(self, dataset):
        return dataset


op = Dummy()

print(type(op).__name__)
print(isinstance(op, Operation))