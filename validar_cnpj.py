import re #Importação da biblioteca para utilização de métodos das expressões regulares

def validacao_cnpj(x):
    cnpj_re = r'\s(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\s'
    cpf_rec = r'(\d{3}\.\d{3}\.\d{3}-\d{2})\s'
    cnpj_r = re.search(cnpj_re, x)

    if cnpj_r:
        b = re.findall(r'(\d)', cnpj_r.group())

        for i in range(14):
            b[i] = int(b[i])

        num1 = 5
        num2 = 9
        somac1 = 0
        for i in range(12):
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

            num3 = 6
            num4 = 9
            somac2 = 0
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
                return  True #print("CNPJ VÁLIDO: " + cnpj_r.group())
            else:
                return False #print("CNPJ INVÁLIDO!!")
        else:
            return  False #print("CNPJ INVÁLIDO!!")

    else:
        cpf_c = re.findall(cpf_rec, x)
        h = len(cpf_c)

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
                        return True #print(" CPF DO VENDEDOR VÁLIDO:")
                    else:
                        return False  # print("CPF DO VENDEDOR INVÁLIDO")
                else:
                    return False #print("CPF DO VENDEDOR INVÁLIDO")
            else:
                return False  # print("FORMATO INCORRETO DE CPF DO VENDEDOR!!")
        else:
            return False #print("FORMATO INCORRETO DE CNPJ!!")