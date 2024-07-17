class Polynomial():

    def __init__(self,coefficients=[0]):
        self.coefficients = coefficients[::-1]

    def __add__(self, other):
        length = max(len(self.coefficients), len(other.coefficients))
        result = [0] * length

        for i in range(length):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result[i] = coeff1 + coeff2

            result.reverse()
            return Polynomial(result)


    def __call__(self, param):
        length = len(self.coefficients)
        total = 0
        for i in range(length):
            total += self.coefficients[i] * (param**i)
        return total
    

    def __repr__(self):
        length = len(self.coefficients)
        

p1 = Polynomial([2, 0, 7, -9, 3])  # 2x^4 - 9x^3 + 7x + 3
print(p1)