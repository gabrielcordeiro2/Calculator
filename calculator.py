print('''
 dP""b8    db    88      dP""b8 88   88 88        db    8888b.   dP"Yb  88""Yb    db
dP   `"   dPYb   88     dP   `" 88   88 88       dPYb    8I  Yb dP   Yb 88__dP   dPYb
Yb       dP__Yb  88  .o Yb      Y8   8P 88  .o  dP__Yb   8I  dY Yb   dP 88"Yb   dP__Yb
 YboodP dP""""Yb 88ood8  YboodP `YbodP' 88ood8 dP""""Yb 8888Y"   YbodP  88  Yb dP""""Yb


Esta é apenas uma versao experimental.  (1.0.0)
Que os numeros estejam com voce.''')

alternativas = [1, 2, 3, 4, 5 ,6]
r_operacao = ''

while r_operacao != alternativas:
    r_operacao = int(input('''

================================================================

Qual Operação voce deseja efetuar?

1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Potenciação
6- Raíz

'''))
# Operação de Soma:
    if r_operacao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"A resposta é: {n1+n2}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break
# Operação de Subtração:
    elif r_operacao == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"A resposta é: {n1-n2}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break       
# Operação de Multiplicação:
    elif r_operacao == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"A resposta é: {n1*n2}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break     
# Operação de Divisão:
    elif r_operacao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"A resposta é: {n1/n2}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break     
# Operação de Potenciação:
    elif r_operacao == 5:
        n1 = int(input("Digite o número base: "))
        n2 = int(input("Digite por quanto ele será elevado: "))
        print(f"A resposta é: {n1**n2}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break   
# Operação de Raíz:
    elif r_operacao == 6:
        potencia = int(input('''
Digite qual a potencia de raíz voce deseja calcular, por exemplo:
Raíz Quadrada = 2
Raíz Cúbica = 3

'''))
        raiz = int(input("Digite a base da raiz: "))
        print(f"A resposta é: {raiz**(1/potencia)}")
        continuar = input("Voce deseja realizar mais algum calculo? (S/N): ")
        if continuar.lower() == "n":
            print("Programa encerrado.")
            break
    else:
        print('''
Erro!
Por favor, digite uma operação de 1 a 6''')
        
