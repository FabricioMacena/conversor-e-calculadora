def decimalParaBinario(num):
    binario = ''
    while num != 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2
    return binario
        
def decimalParaOctal(num):
    octal = ''
    while num != 0:
        resto = num % 8
        octal = str(resto) + octal
        num = num // 8
    return octal

def decimalParaHexa(num):
    hexa = ''
    while num != 0:
        resto = num % 16
        if resto == 10:
            resto = 'A'
        elif resto == 11:
            resto = 'B'
        elif resto == 12:
            resto = 'C'
        elif resto == 13:
            resto = 'D'
        elif resto == 14:
            resto = 'E'
        elif resto == 15:
            resto = 'F'
        hexa = str(resto) + hexa
        num = num // 16
    return hexa

def binarioParaDecimal(num):
    cont = 0
    decimal = 0
    totalAlga = len((num))
    for c in range(totalAlga -1, -1, -1):
        digito = num[cont]
        resultado = int(digito) * (2 ** c)
        decimal = resultado + decimal
        cont = cont + 1
    return decimal
        
def octalParaDecimal(num):
    cont = 0
    decimal = 0
    totalAlga = len((num))
    for c in range(totalAlga -1, -1, -1):
        digito = num[cont]
        resultado = int(digito) * (8 ** c)
        decimal = resultado + decimal
        cont = cont + 1
    return decimal

def hexaParaDecimal(num):
    cont = 0
    decimal = 0
    totalAlga = len((num))
    for c in range(totalAlga -1, -1, -1):
        digito = num[cont]
        if digito == 'A':
            digito = 10
        elif digito == 'B':
            digito = 11
        elif digito == 'C':
            digito = 12
        elif digito == 'D':
            digito = 13
        elif digito == 'E':
            digito = 14
        elif digito == 'F':
            digito = 15
        resultado = int(digito) * (16 ** c)
        decimal = resultado + decimal
        cont = cont + 1
    return decimal

def somaBinario(v1, v2):
    v3 = v1 + v2
    v3 = decimalParaBinario(v3)
    return v3


def subBinario(v1, v2):
    v3 = v1 - v2
    v3 = decimalParaBinario(v3)
    return v3  

def multBinario(v1, v2):
    v3 = v1 * v2
    v3 = decimalParaBinario(v3)
    return v3
