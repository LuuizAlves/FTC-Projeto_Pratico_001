import re

try:
    def validacao_cpf(x):
        cpf_re = r'^(\d{3}\.\d{3}\.\d{3}-\d{2}\s)'
        cpf_r = re.search(cpf_re, x)

        if cpf_r:
            a = re.findall(r'(\d)', cpf_r.group())

            for i in range(11):
                a[i] = int(a[i])

            soma = a[0] * 10 + a[1] * 9 + a[2] * 8 + a[3] * 7 + a[4] * 6 + a[5] * 5 + a[6] * 4 + a[7] * 3 + a[8] * 2
            resto_cpf = soma % 11

            if resto_cpf < 2:
                valor1 = 0
            else:
                valor1 = 11 - resto_cpf

            if valor1 == a[9]:
                soma1 = a[0] * 11 + a[1] * 10 + a[2] * 9 + a[3] * 8 + a[4] * 7 + a[5] * 6 + a[6] * 5 + a[7] * 4 + a[
                    8] * 3 + a[9] * 2
                resto2_cpf = soma1 % 11

                if resto2_cpf < 2:
                    valor2 = 0
                else:
                    valor2 = 11 - resto2_cpf

                if valor2 == a[10]:
                    return True  # print("CPF VÁLIDO: " + cpf_r.group())
                else:
                    return False  # print("CPF INVÁLIDO")
            else:
                return False  # print("CPF INVÁLIDO")
        else:
            return False  # print("FORMATO INCORRETO DE CPF!")


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

            resc1 = somac1 % 11

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

                resc2 = somac2 % 11

                if resc2 < 2:
                    segundo = 0
                else:
                    segundo = 11 - resc2

                if segundo == b[13]:
                    return True  # print("CNPJ VÁLIDO: " + cnpj_r.group())
                else:
                    return False  # print("CNPJ INVÁLIDO!!")
            else:
                return False  # print("CNPJ INVÁLIDO!!")

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

                    soma = ac[0] * 10 + ac[1] * 9 + ac[2] * 8 + ac[3] * 7 + ac[4] * 6 + ac[5] * 5 + ac[6] * 4 + ac[
                        7] * 3 + ac[8] * 2
                    resto = soma % 11

                    if resto < 2:
                        valor1 = 0
                    else:
                        valor1 = 11 - resto

                    if valor1 == ac[9]:
                        soma1 = ac[0] * 11 + ac[1] * 10 + ac[2] * 9 + ac[3] * 8 + ac[4] * 7 + ac[5] * 6 + ac[6] * 5 + \
                                ac[7] * 4 + ac[8] * 3 + ac[9] * 2
                        resto2 = soma1 % 11

                        if resto2 < 2:
                            valor2 = 0
                        else:
                            valor2 = 11 - resto2

                        if valor2 == ac[10]:
                            return True  # print(" CPF DO VENDEDOR VÁLIDO:")
                        else:
                            return False  # print("CPF DO VENDEDOR INVÁLIDO")
                    else:
                        return False  # print("CPF DO VENDEDOR INVÁLIDO")
                else:
                    return False  # print("FORMATO INCORRETO DE CPF DO VENDEDOR!!")
            else:
                return False  # print("FORMATO INCORRETO DE CNPJ!!")


    def data(x):
        teste = '159.200.335-41 581.612.159-60 2012.12.12 25:00:00 [5.00] 489756322-i3j4k-666'

        data_re = r'\s[1-2][098][0189][^9][.][0][1-9][.][1-2][0-9]\s'
        data_r = re.search(data_re, x)

        if data_r:
            return True  # print("DATA VÁLIDA: " + data_r.group())
        else:
            data_r = re.search(r'\s[1-2][089][0189][^9][.][1][0-2][.][1-2][0-9]\s', x)
        if data_r:
            return True  # print("DATA VÁLIDA: " + data_r.group())
        else:
            data_r = re.search(r'\s[1-2][089][0189][^9][.][0][1-9][.][3][0-1]\s', x)
            if data_r:
                return True  # print("DATA VÁLIDA: " + data_r.group())
            else:
                data_r = re.search(r'\s[1-2][089][0189][^9][.][1][0-2][.][3][0-1]\s', x)
                if data_r:
                    return True  # print("DATA VÁLIDA: " + data_r.group())
                else:
                    data_r = re.search(r'\s[1-2][089][0189][^9][.][0][0-9][.][0][1-9]\s', x)
                    if data_r:
                        return True  # print("DATA VÁLIDA: " + data_r.group())
                    else:
                        data_r = re.search(r'\s[1-2][089][0189][^9][.][1][0-2][.][0][1-9]\s', x)
                        if data_r:
                            return True  # print("DATA VÁLIDA: " + data_r.group())
                        else:
                            return False  # print("DATA INCORRETA!")


    def hora(x):
        hora_re = r'\s[0-1][0-9]\:[0-5][0-9]\:[0-5][0-9]\s'
        hora_r = re.search(hora_re, x)

        if hora_r:
            return True  # print("HORA VÁLIDA: " + hora_r.group())
        else:
            hora_r = re.search(r'\s[2][0-3]\:[0-5][0-9]\:[0-5][0-9]\s', x)
            if hora_r:
                return True  # print("HORA VÁLIDA: " + hora_r.group())
            else:
                return False  # print("HORA INCORRETA")


    def validando_preco(x):
        preco_re = r'\[\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\]'

        preco_r = re.search(preco_re, x)

        if preco_r:
            return True  # print("VALIDO!")
        else:
            preco_r = re.search(r'\[\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\]', x)
            if preco_r:
                return True  # print("VALIDO!")
            else:
                preco_r = re.search(r'\[\d+\.\d{2}\,\d+\.\d{2}\,\d+\.\d{2}\]', x)
                if preco_r:
                    return True  # print("VALIDO!")
                else:
                    preco_r = re.search(r'\[\d+\.\d{2}\,\d+\.\d{2}\]', x)
                    if preco_r:
                        return True  # print("VALIDO!")
                    else:
                        preco_r = re.search(r'\[\d+\.\d{2}\]', x)
                        if preco_r:
                            return True  # print("VALIDO!")
                        else:
                            return False  # print("INVALIDO!!")


    def validacao_tra(x):
        tra_re1 = r'(\s\d{9}\-[a-z0-9]{5}\-[24680]{3}\-[0-1]{3})$'
        tam = re.search(r'\d{9}\-[a-z0-9]{5}\-\d{3}\-\d{3}', x)

        if tam:
            a = re.findall(r'\w|\w', tam.group())
            b = len(a)
        else:
            b = 10

        tra_r = re.search(tra_re1, x)

        if tra_r:
            g = re.findall(r'[a-z0-9]', tra_r.group())
            compara = 0

            if g[9] == g[10]:
                compara = 1
            if g[9] == g[11]:
                compara = 1
            if g[9] == g[12]:
                compara = 1
            if g[9] == g[13]:
                compara = 1
            if g[10] == g[11]:
                compara = 1
            if g[10] == g[12]:
                compara = 1
            if g[10] == g[13]:
                compara = 1
            if g[11] == g[12]:
                compara = 1
            if g[11] == g[13]:
                compara = 1
            if g[11] == g[12]:
                compara = 1

            if tra_r and compara == 0:
                return True  # print("TRANSAÇÃO APROVADA: " + tra_r.group())
            else:
                return False  # print("ERRO NO CÓDIGO DE TRASAÇÃO")
        else:
            if b == 20:
                return False  # print("ERRO NO CÓDIGO DE TRASAÇÃO")
            else:
                tra_r = re.search(r'(\s\d{9}\-[a-z0-9]{5}\-[^13579]{3})$', x)
                if tra_r:
                    g = re.findall(r'[a-z0-9]', tra_r.group())
                    compara = 0

                    if g[9] == g[10]:
                        compara = 1
                    if g[9] == g[11]:
                        compara = 1
                    if g[9] == g[12]:
                        compara = 1
                    if g[9] == g[13]:
                        compara = 1
                    if g[10] == g[11]:
                        compara = 1
                    if g[10] == g[12]:
                        compara = 1
                    if g[10] == g[13]:
                        compara = 1
                    if g[11] == g[12]:
                        compara = 1
                    if g[11] == g[13]:
                        compara = 1
                    if g[11] == g[12]:
                        compara = 1

                    if tra_r and compara == 0:
                        return True  # print("TRANSAÇÃO APROVADA: " + tra_r.group())
                    else:
                        return False  # print("ERRO NO CODIGO DE TRANSAÇÃO!")
                else:
                    return False  # print("ERRO NO CODIGO DE TRANSAÇÃO!")


    var1 = input()

    cpf = validacao_cpf(var1)
    cnpj = validacao_cnpj(var1)
    vdata = data(var1)
    vhora = hora(var1)
    pre = validando_preco(var1)
    tran = validacao_tra(var1)

    # print(cpf)
    # print(cnpj)
    # print(vdata)
    # print(vhora)
    # print(pre)
    # print(tran)

    if cpf:
        if cnpj:
            if vdata:
                if vhora:
                    if pre:
                        if tran:
                            resultado = True
                        else:
                            resultado = False
                    else:
                        resultado = False
                else:
                    resultado = False
            else:
                resultado = False
        else:
            resultado = False
    else:
        resultado = False

    print(resultado)

except EOFError:
    print(True)