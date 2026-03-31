def adicionar_contato (contatos, nome_contato, email_contato, telefone_contato):
    contato = {"contato": nome_contato, "email": email_contato, "telefone": telefone_contato}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi salvo!")
    return

def visualizar_contatos (contatos):
    print("\n Sua lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. Nome: {nome_contato} \n Telefone: {telefone_contato} \n Email: {email_contato}\n")


def atualizar_contatos (contatos, indice_contato, escolha_novo):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(contatos):
        if escolha_novo == "1":
            novo_nome = input ("Digite o novo nome do contato: ")
            contatos[indice_contato_ajustado] ["contato"] = novo_nome
            print(f"Nome do contato atualizado para {novo_nome}")
        elif escolha_novo == "2":
            novo_email = input ("Digite o novo email do contato: ")
            contatos[indice_contato_ajustado] ["email"] = novo_email
            print(f"Email do contato atualizado para {novo_email}")
        elif escolha_novo == "3":
            novo_telefone = input ("Digite o novo telefone do contato: ")
            contatos [indice_contato_ajustado] ["telefone"] = novo_telefone
            print(f"Telefone do contato atualizado para {novo_telefone}")
    else:
        print("Índice de tarefa inválido.")
    return

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
        atualizar_contatos(contatos, indice_contato, escolha_novo)
        


    elif escolha == "7":
        break

