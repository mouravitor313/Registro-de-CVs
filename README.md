# Registro de CVs

Este projeto consiste em um sistema simples para registrar informações de currículos (CVs) utilizando Python e Pandas. Ele permite coletar dados como nome, idade, telefone, email, formação e resumo de um candidato e armazená-los em um DataFrame.

## Arquivos do projeto

### Arquivo 1: main.py

O arquivo `main.py` contém a classe `Main`, que é a classe principal do projeto.

### Arquivo 2: registro.py

O arquivo `registro.py` contém a classe `Registro`, responsável por coletar as informações dos currículos. Ela possui um método chamado `Registrar()` que solicita ao usuário os dados do currículo e os armazena em um DataFrame do Pandas.

### Arquivo 3: registrocv.py

O arquivo `registrocv.py` contém a classe `Login`, que simula um sistema de login básico. Ela solicita ao usuário um login e senha e, se as credenciais forem corretas, chama o método `Registrar()` da classe `Registro` para coletar as informações do currículo.

## Como usar

1. Certifique-se de ter o Python e o Pandas instalados no seu ambiente.

2. Execute o arquivo `registrocv.py`.

3. Será solicitado um login e senha. Utilize as seguintes credenciais:
   - Login: user123
   - Senha: 1234

4. Após fazer o login com sucesso, você poderá registrar os dados do currículo. Siga as instruções fornecidas pelo programa.

5. Para encerrar a sessão, digite "0" no campo do nome.

6. O programa armazenará os dados do currículo em um DataFrame e, ao finalizar, exibirá o DataFrame na saída.

Esse é um projeto simples, mas pode ser expandido para incluir mais funcionalidades, como salvar os currículos em um arquivo ou realizar análises adicionais dos dados coletados.

Sinta-se à vontade para contribuir, fazer melhorias ou adaptar o projeto de acordo com suas necessidades.

Divirta-se!
