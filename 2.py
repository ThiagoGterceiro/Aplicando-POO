#2
class login:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha


    def acesso (self):
        if self.nome == 'thiago' and self.senha == '1234' :
            return ('Autorizado')
        else:
            return ('Negado')

thiago= login('thiago','1234')
print(f'O acesso de {thiago.nome} está : \n {thiago.acesso()}')
