def escolha_1():
    x = 5
    y = 10
    soma = x + y
    print("Resultado da soma é:", soma)

def escolha_2():
    nome = input("escreva o seu nome: ")
    idade  = int(input("Escreva a sua idade: "))
    media =  float(input("Escreva a sua média: "))
    print(f"Olá {nome}, você tem {idade} anos e sua média é {media}.")

def menu():
    while True:
        print("="* 30)
        print("Menu básico")
        print("="* 30)
        print("1 - Opção 1")
        print("2 - Opção 2")
        print("0 - Sair")
        print("="* 30)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            escolha_1()
        elif escolha == '2':
            escolha_2()
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        