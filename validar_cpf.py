import re

def validacao_cpf(x):
    cpf_re = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    print(cpf_re)
    cpf_r = re.search(cpf_re, x)
    print(cpf_r)

    if cpf_r:
        a = re.findall(r'(\d|\d)', cpf_r.group())
        print(a)

        for i in range(11):
            a[i] = int(a[i])
        print(a)

        soma = a[0]*10+a[1]*9+a[2]*8+a[3]*7+a[4]*6+a[5]*5+a[6]*4+a[7]*3+a[8]*2
        resto_cpf = soma%11

        if resto_cpf < 2:
            valor1 = 0
        else:
            valor1 = 11 - resto_cpf

        if valor1 == a[9]:
            soma1 = a[0]*11+a[1]*10+a[2]*9+a[3]*8+a[4]*7+a[5]*6+a[6]*5+a[7]*4+a[8]*3+a[9]*2
            resto2_cpf = soma1%11

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