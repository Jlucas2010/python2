import re

print("Sistema de cadastro de usuarios")

emailIntrodusido = input("Introdusa o seu email.")
senhaIntodusido = input("Introdusa a sua senha.")
nome = input("Introdusa o seu Nome.")
listaUsuarios = [["j@alam.com", "j", "j"]]


def Valido(emailIntrodusido):
    V = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', emailIntrodusido)
    if V == None:
        print("Email invalido.")
    return V


def emails(emailIntrodusido):
    Temp = []
    for x in listaUsuarios:
        for y in listaUsuarios:
            if y == emailIntrodusido:
                print("Email já cadastrado, Introdusa outro")
            else:
                Temp.append(emailIntrodusido)
                Temp.append(senhaIntodusido)
                Temp.append(nome)
                listaUsuarios.append(Temp)
                print("Email cadastrado.")
                return listaUsuarios


Valido(emailIntrodusido)
if V != None:
    emails(emailIntrodusido)
