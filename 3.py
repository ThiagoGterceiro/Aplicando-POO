#3
class socio:

    def __init__(self,tipo,valor):
       self.tipo = tipo
       self.valor = valor

    def desconto (self):
        if self.tipo == 'gold':
            return(self.valor * 0.10)

        elif self.tipo == 'platinum' :
            return (self.valor * 0.20)

        elif self.tipo == 'black' :
            return (self.valor * 0.30)

        else:
            return(self.valor)

a=socio('black',1000)
conta = a.desconto()
print(f'A sua conta saiu por: {conta} R$ ')