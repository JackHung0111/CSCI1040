# 1155108381
# Quiz Q3


class Series:
    def __init__(self, n):
        self.n = n
    def compute(self):
        pass

class GeometricSeries(Series):
    def __init__(self, a, r, n):
        super().__init__(n)
        self.a = a
        self.r = r
    def compute(self):
        super().compute()
        sum = 0
        for i in range(self.n):
            sum += self.a * (self.r ** i)
        return sum
