nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))
estuda = input("Você estuda Python? S/N? ")

anos = 18 - idade

if idade < 18:
    print(f"Sinto muito! Entrada permitida somente para pessoas com 18 anos ou mais! Volte daqui {anos} anos!")

else: 
    print('''
    [1] Entrada Padrão - R$ 35,00 reais
    [2] Entrada VIP - R$ 60,00 reais''')

    entrada = int(input("Qual entrada você gostaria de adquirir? "))

    if estuda == 'S' and entrada == 1:
        print(f"Legal! Você ganhou 50% de desconto, sua Entrada Padrão será no valor de R$ {35*0.5} reais.")

    elif estuda == 'S' and entrada == 2: 
        print(f"Legal! Você ganhou 50% de desconto, sua Entrada VIP será no valor de R$ {60*0.5} reais.")

    else: 
        if entrada == 1:
            print(f"Legal! Sua Entrada Padrão será no valor de R$ 35,00 reais.")

        else: 
            print(f"Legal! Sua Entrada VIP será no valor de R$ 60,00 reais.")


