import re #Importação da biblioteca para utilização de métodos das expressões regulares

def validacao_cpf(x):
    cpf_re = r'\d{3}\.\d{3}\.\d{3}-\d{2}' #Expressão regular que vai encontrar o formato correto de CPF
    cpf_r = re.search(cpf_re, x) #Procura o CPF através da expressão criada e armazena na variável cpf_r

    #Verifica se o formato do CPF é valido, se não é retornado informando o erro e o resultado FALSE
    if cpf_r:
        a = re.findall(r'(\d|\d)', cpf_r.group()) #Cria uma lista através do método .findal() e armazena na variável a

        for i in range(11): #Transforma a lista de string em uma lista de inteiros para ser possivel realizar os cálculos
            a[i] = int(a[i])

        #Cálculo realizado para obter o valor do primeiro digito verificador, que vai especificar se o CPF é válido
        soma = a[0]*10+a[1]*9+a[2]*8+a[3]*7+a[4]*6+a[5]*5+a[6]*4+a[7]*3+a[8]*2
        resto_cpf = soma%11

        #Verifica o valor do primeiro digito verificador - Se menor que 2, recebe 0 : Se maior ou igual, recebe 11 - resto_cpf
        if resto_cpf < 2:
            valor1 = 0
        else:
            valor1 = 11 - resto_cpf

        #Verifica se o primeiro digíto está de acordo com o CPF que foi encontrado, senão o CPF é inválido
        if valor1 == a[9]:

            #Cálculo realizado para obter o valor do segundo digito verificador, que vai especificar se o CPF é válido
            soma1 = a[0]*11+a[1]*10+a[2]*9+a[3]*8+a[4]*7+a[5]*6+a[6]*5+a[7]*4+a[8]*3+a[9]*2
            resto2_cpf = soma1%11

            #Verifica o valor do segundo digito verificador - Se menor que 2, recebe 0 : Se maior ou igual, recebe 11 - resto_cpf
            if resto2_cpf < 2:
                valor2 = 0
            else:
                valor2 = 11 - resto2_cpf

            if valor2 == a[10]:
                print("CPF VÁLIDO: " + cpf_r.group())
                return True
            else:
                print("CPF INVÁLIDO")
                return False
        else:
            print("CPF INVÁLIDO")
            return False
    else:
        print("FORMATO INCORRETO DE CPF!")
        return False 

valor_entrada = input()
resultado = validacao_cpf(valor_entrada)
print(resultado)