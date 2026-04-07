import os 

def adicionar_contato (contatos, nome_contato, email_contato, telefone_contato):
    contato = {"contato": nome_contato, "email": email_contato, "telefone": telefone_contato, "favorito": False}
    contatos.append(contato)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"O contato {nome_contato} foi salvo!")
    return

def visualizar_contatos (contatos):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n Sua lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆ " if contato ["favorito"] else ""
        print(f"{indice}. {status} Nome: {contato.get("contato")} \n   Email: {contato.get("email")} \n   Telefone:{contato.get("telefone")}\n")

def atualizar_contatos (contatos, indice_contato, escolha_novo):
    indice_contato_ajustado = int(indice_contato) - 1

    if indice_contato_ajustado <0 and indice_contato_ajustado > len(contatos):
        print("Índice de contato inválido.")
        return
    
    contato_indice= contatos[indice_contato_ajustado] 
    if escolha_novo == "1":
        novo_nome = input ("Digite o novo nome do contato: ")
        contato_indice ["contato"] = novo_nome
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Nome do contato atualizado para {novo_nome}")
    elif escolha_novo == "2":
        novo_email = input ("Digite o novo email do contato: ")
        contato_indice ["email"] = novo_email
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Email do contato atualizado para {novo_email}")
    elif escolha_novo == "3":
        novo_telefone = input ("Digite o novo telefone do contato: ")
        contato_indice ["telefone"] = novo_telefone
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Telefone do contato atualizado para {novo_telefone}")

    print (contatos)
    return

def favoritar_desfavoritar (contatos, indice_contato):
    indice_contato_ajustado = int (indice_contato) - 1

    if indice_contato_ajustado <0 and indice_contato_ajustado > len (contatos):
        print("Índice de contato inválido.")
    else:
        if contatos[indice_contato_ajustado] ["favorito"] == False:
            contatos[indice_contato_ajustado] ["favorito"] = True
            print(f"Contato {nome_contato} foi favoritado!")
        else:
            contatos[indice_contato_ajustado] ["favorito"] = False
    return
    
def visualizar_favoritos (contatos):
    print("\n Sua lista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆ " if contato ["favorito"] else ""
        if contato ["favorito"] == True:
            print (f"{indice}. {status} Nome: {contato.get("contato")} \n   Email: {contato.get("email")} \n   Telefone {contato.get("telefone")}\n")
    
        

def deletar_contato (contatos, indice_contato):
    indice_contato_ajustado = int (indice_contato) - 1

    if indice_contato_ajustado <0 and indice_contato_ajustado > len(contatos):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Índice de contato inválido.")
        return
    
    else:
        del contatos[indice_contato_ajustado]

        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Contato deletado com sucesso!")

contatos = []


while True:
    print("Agenda pessoal")
    print("\n 1) Adicionar novo contato")
    print(" 2) Ver sua lista de contatos")
    print(" 3) Editar informações de um contato")
    print(" 4) Marcar ou tirar um contato como favorito")
    print(" 5) Ver contatos favoritos")
    print(" 6) Apagar um contato")
    print(" 7) Sair\n")

    escolha= input("Escolha um número: ")

    if escolha == "1":
        nome_contato = input("Nome do contato: ")
        email_contato = input("Email do contato: ")
        telefone_contato = input ("Telefone do contato: ")
        adicionar_contato (contatos, nome_contato, email_contato, telefone_contato)
    
    elif escolha == "2":
        visualizar_contatos(contatos)

    elif escolha == "3":
        visualizar_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        print (" 1. Mudar o nome do contato\n 2. Mudar o email do contato\n 3. Mudar o telefone do contato")
        escolha_novo = input("Digite o número do que deseja alterar nesse contato: ")
        if escolha_novo <0 and escolha_novo > "3":
            print ("Número inválido")
        else:
            atualizar_contatos(contatos, indice_contato, escolha_novo)
        
    elif escolha == "4":
        #Favoritar contato/desfavoritar um contato
        visualizar_contatos(contatos)
        indice_contato = input("Qual contato deseja favoritar/desfavoritar: ")
        favoritar_desfavoritar(contatos, indice_contato)
    
    elif escolha == "5":
        visualizar_favoritos(contatos)

    elif escolha == "6":
        visualizar_contatos(contatos)
        indice_contato = input ("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)


    elif escolha == "7":
        break

