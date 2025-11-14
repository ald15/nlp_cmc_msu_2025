class Polynomial():
    def __init__(self, *args):
        self.coefs = list(args)

    def __call__(self, x):
        return sum([self.coefs[i] * x**i for i in range(len(self.coefs))])
    
    def __setitem__(self, s, c):
        self.coefs[s] = c 


polynom = Polynomial(2, 3, 1, 4, 5)
polynom[0] = 10
polynom[1::2] = [-1, -2]
print(polynom.coefs)