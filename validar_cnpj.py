import re #Importação da biblioteca para utilização de métodos das expressões regulares

def validacao_cnpj(x):
    cnpj_re = r'\s(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\s'  #Expressão regular que vai encontrar o formarto de CNPJ na entrada
    cpf_rec = r'(\d{3}\.\d{3}\.\d{3}-\d{2})\s'  #Expressão regular que vai encontrar o formarto de CPF na entrada
    cnpj_r = re.search(cnpj_re, x) ##Procura o CNPJ através da expressão criada e armazena na variável cnpj_r

    #Se foi encontrada o CNPJ então é feita a validação, senão o formato que foi encontrado é de CPF e também realiza a validação
    if cnpj_r:
        b = re.findall(r'(\d)', cnpj_r.group()) #Transforma a expressão encontrada em uma lista de strings através do metódo .findall()

        for i in range(14):     #Converte a lista de strings em uma lista de inteiros para possibilitar os calcúlos
            b[i] = int(b[i])

        num1,num2,somac1 = 5,9,0
        
        for i in range(12): #Realiza os calcúlos necessários para a validação do CNPJ
            if i <= 3:
                x1 = b[i] * num1
                somac1 += x1
                num1 -= 1
            if i > 3:
                y1 = b[i] * num2
                somac1 += y1
                num2 -= 1

        resc1 = somac1%11

        if resc1 < 2:
            primeiro = 0
        else:
            primeiro = 11 - resc1

        if primeiro == b[12]:
            num3,num4,somac2 = 6,9,0

            for i in range(13):
                if i <= 4:
                    x = b[i] * num3
                    somac2 += x
                    num3 -= 1
                if i > 4:
                    y = b[i] * num4
                    somac2 += y
                    num4 -= 1

            resc2 = somac2% 11

            if resc2 < 2:
                segundo = 0
            else:
                segundo = 11 - resc2

            if segundo == b[13]:
                print("CNPJ VÁLIDO: " + cnpj_r.group())
                return  True
            else:
                print("CNPJ INVÁLIDO!!")
                return False 
        else:
            print("CNPJ INVÁLIDO!!")
            return  False
    else:
        cpf_c = re.findall(cpf_rec, x)  #Procura o CPF através da expressão criada e armazena na variável cpf_c
        h = len(cpf_c)  #Verifica a quantidade de CPF que foi encontrada na nota e armazena em 'h'

        #Se houver mais de um CPF encontrado é feita a validação somente no segundo
        if h > 1:
            cpf2_re = r'\s(\d{3}\.\d{3}\.\d{3}-\d{2})\s'
            cpfc2 = re.search(cpf2_re, x)

            if cpfc2:
                cpfc1 = cpf_c[1]
                ac = re.findall(r'(\d|\d)', cpfc1)

                for i in range(11):
                    ac[i] = int(ac[i])

                soma = ac[0]*10+ac[1]*9+ac[2]*8+ac[3]*7+ac[4]*6+ac[5]*5+ac[6]*4+ac[7]*3+ac[8]*2
                resto = soma%11

                if resto < 2:
                    valor1 = 0
                else:
                    valor1 = 11 - resto

                if valor1 == ac[9]:
                    soma1 = ac[0]*11+ac[1]*10+ac[2]*9+ac[3]*8+ac[4]*7+ac[5]*6+ac[6]*5+ac[7]*4+ac[8]*3+ac[9]*2
                    resto2 = soma1%11

                    if resto2 < 2:
                        valor2 = 0
                    else:
                        valor2 = 11 - resto2

                    if valor2 == ac[10]:
                        print(" CPF DO VENDEDOR VÁLIDO:")
                        return True
                    else:
                        print("CPF DO VENDEDOR INVÁLIDO")
                        return False  
                else:
                    print("CPF DO VENDEDOR INVÁLIDO")
                    return False
            else:
                print("FORMATO INCORRETO DE CPF DO VENDEDOR!!")
                return False
        else:
            print("FORMATO INCORRETO DE CNPJ!!")
            return False

valor_entrada = input()
resultado = validacao_cnpj(valor_entrada)
print(resultado)