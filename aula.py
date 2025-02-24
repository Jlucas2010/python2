
def criar_ficheiro():
    nome = input("Intrudusa um nome para o ficheiro: ")
    with open(nome, "w") as file:
        file.write("")
    print("Ficheiro criado.")
    print(f"O nome do ficheiro é {nome}.")

def escrita():
    nome = input("Nome do ficheiro a escrever: ")
    frase = input("Intrudosa a frase: ")
    with open(f"{nome}", "a") as file:
        file.write(f"\n{frase}")

def ler():
    nome = input("Nome do ficheiro a ler: ")
    with open(f"{nome}", "r") as file:
        leitora = file.readlines()
        for l in leitora:
            print(l)

def escolha():
    print("")
    print("Digite 1 para criar ficheiro.")
    print("Digite 2 para escrever em um ficheiro.")
    print("Digite 3 para ler um ficheiro.")
    escolha = input("O que deseja fazer ? : ")
    print("")
    if escolha == "1":
        criar_ficheiro()
    elif escolha == "2":
        escrita()
    elif escolha == "3":
        ler()

while True:
    escolha()


