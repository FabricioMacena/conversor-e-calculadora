import metods

print('¬¬' * 25)
print(f'\033[32m      Conversor de bases numéricas \n       e calculadora de binários \033[m')

opcao = int(input('\n[1] Converter da base decimal para as demais bases; \n[2] Converter das demais bases para a base decimal;\n[3] Abrir calculadora de números binários. \nQual opção deseja? '))
while opcao != 1 and opcao != 2 and opcao != 3:
    opcao = int(input('Opção inválidada. Digite novamente: '))

while opcao != 4:

    if opcao == 1:
        num = int(input('\nInsira um número decimal: '))
        base = str(input('\n[B] Decimal para Binário; \n[O] Decimal para Octal; \n[H] Decimal para Hexadecimal. \nQual opção deseja? ')).upper().strip()[0]
        while base != 'B' and base != 'O' and base != 'H':
            base = str(input('Opção inválida. Tente Novamente: ')).upper().strip()[0]
        if base == 'B':
            print(f'\nO número {num} em binário é --> \033[1;34m{metods.decimalParaBinario(num)}\033[m')
        elif base == 'O':
            print(f'\nO número {num} em Octadecimal é --> \033[1;34m{metods.decimalParaOctal(num)}\033[m')
        elif base == 'H': 
            print(f'\nO número {num} em Hexadecimal é --> \033[1;34m{metods.decimalParaHexa(num)}\033[m')
            
        opcao = int(input('\n[1] Converter da base decimal para as demais bases; \n[2] Converter das demais bases para a base decimal; \n[3] Abrir calculadora de binário \n[4] Terminar Programa\nQual opção deseja? '))

    elif opcao == 2:
        base = str(input('\n[B] Binário para Decimal; \n[O] Octal para Decimal; \n[H] Hexa para Decimal. \nInsira a base desejada: ')).upper().strip()[0]
        while base != 'B' and base != 'O' and base != 'H':
            base = str(input('Opção inválida. Tente Novamente: ')).upper().strip()[0] 
        if base == 'B':
            num = str(input('\n(Dígitos possíveis: 0 e 1) \nInsira o número Binário: '))
            print(f'\nO número {num} em decimal é --> \033[1;34m{metods.binarioParaDecimal(num)}\033[m')
        elif base == 'O':
            num = str(input('\n(Dígitos Possíveis: 0, 1, 2, 3, 4, 5, 6 e 7) \nInsira o número Octal: '))
            print(f'\nO número {num} em decimal é --> \033[1;34m{metods.octalParaDecimal(num)}\033[m')
        elif base == 'H':
            num = str(input('\n(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F) \nInsira o número Hexadecimal: ')).upper()
            print(f'\nO número {num} em decimal é --> \033[1;34m{metods.hexaParaDecimal(num)}\033[m')

        opcao = int(input('\n[1] Converter da base decimal para as demais bases; \n[2] Converter das demais bases para a base decimal; \n[3] Abrir calculadora de binário; \n[4] Terminar Programa\nQual opção deseja? '))

    elif opcao == 3:
        num = str(input('\nInsira um número binário: '))
        v1 = metods.binarioParaDecimal(num)
        num2 = str(input('Insira outro número binário: '))
        v2 = metods.binarioParaDecimal(num2)
        opcao = int(input('\n[1] Somar \n[2] Subtrair \n[3] Multiplicar \nO que deseja fazer com esses números? '))
        while opcao != 1 and opcao != 2 and opcao != 3:
            opcao = int(input('Opção inválida. Digite novamente: '))
        if opcao == 1:
            v3 = v1 + v2
            print(f'\n{num} ({v1})  +  {num2} ({v2}) --> \033[1;34m{metods.somaBinario(v1, v2)} ({v3})\033[m')
        elif opcao == 2: 
            v3 = v1 - v2
            print(f'\n{num} ({v1})  -  {num2} ({v2}) --> \033[1;34m{metods.subBinario(v1, v2)} ({v3})\033[m')
        elif opcao == 3: 
            v3 = v1 * v2
            print(f'\n{num} ({v1})  x  {num2} ({v2}) --> \033[1;34m{metods.multBinario(v1, v2)} ({v3})\033[m')   

        opcao = int(input('\n[1] Converter da base decimal para as demais bases; \n[2] Converter das demais bases para a base decimal; \n[3] Abrir calculadora de binário; \n[4] Terminar Programa\nQual opção deseja? '))
    else:
        while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            opcao = int(input('Opção inválidada. Digite novamente: '))

print('\n\033[32m'+'Obrigado, até a próxima!'+'\033[0;0m')
print('¬¬' * 25)
