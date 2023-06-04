from os import system
from registro import Registro

# Criando um objeto Registro
registro = Registro()

# Chamando o método Registrar
#registro.Registrar()

# Chamando o método Salvar
#df = registro.Salvar()

class Login:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def meu_metodo(self):
        l = 'user123'
        s = '1234'
        while(True):
            self.login = input('Digite o login:\n')
            self.senha = input('Digite a senha:\n')
            system('cls')
            if self.login == l and self.senha == s:
                registro.Registrar()
                
                break
            elif self.login != l or self.senha != s:
                print('Login incorreto! Tente novamente')
                system('cls')



        


