'''
nome
idade
telefone
email
formação
resumo
'''
import pandas as pd
from os import system

class Registro:
    def __init__(self, nome, idade, telefone, email, formacao, resumo):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.formacao = formacao
        self.resumo = resumo

    def Registrar(self):
        serie_nome = pd.Series([])
        serie_idade = pd.Series([])
        serie_telefone = pd.Series([])
        serie_email = pd.Series([])
        serie_formacao = pd.Series([])
        serie_resumo = pd.Series([])

        while True:
            print('Digite 0 no campo nome para encerrar essa sessão')
            self.nome = input('Digite o nome:\n')
            if self.nome == '0':
                break
            system('cls')
            print('')
            self.idade = input('Digite a idade:\n')
            print('')
            self.telefone = input('Digite o telefone:\n')
            print('')
            self.email = input('Digite o email:\n')
            print('')
            self.formacao = input('Digite a formação:\n')
            print('')
            self.resumo = input('Digite o resumo:\n')
            system('cls')

            serie_nome = serie_nome.append(pd.Series([self.nome]))
            serie_idade = serie_idade.append(pd.Series([self.idade]))
            serie_telefone = serie_telefone.append(pd.Series([self.telefone]))
            serie_email = serie_email.append(pd.Series([self.email]))
            serie_formacao = serie_formacao.append(pd.Series([self.formacao]))
            serie_resumo = serie_resumo.append(pd.Series([self.resumo]))

        df = pd.DataFrame({
            'Nome': serie_nome,
            'Idade': serie_idade,
            'Telefone': serie_telefone,
            'Email': serie_email,
            'Formação': serie_formacao,
            'Resumo': serie_resumo
        })

        return df

