#1
class calculadora:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def somar(self):
        return(self.a + self.b)

    def subtrair(self):
        return(self.a-self.b)

    def multiplicar(self):
        return(self.a*self.b)

    def dividir (self):
        return(self.a/self.b)

c= calculadora(5,7)
print(c.somar())
print(c.subtrair())
print(c.multiplicar())
print(c.dividir())

