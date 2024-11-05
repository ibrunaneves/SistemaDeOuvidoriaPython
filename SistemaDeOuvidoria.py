opcao = 1
manifestacoes = []

print("========== Sistema de Ouvidoria ==========")

while opcao != 6:
    print("""
1) Listagem de manifestações
2) Criar uma nova manifestação 
3) Exibir quantidade de manifestações 
4) Pesquisar uma manifestação por código
5) Excluir uma manifestação pelo Código
6) Sair do sistema """)  
    print()
    opcao = int(input("Digite a opção desejada [1-6]: "))
    print()

    if opcao == 1:
        if len(manifestacoes) > 0:
            print("===== LISTA DE MANIFESTAÇÕES =====")
            print()
            for i in range(len(manifestacoes)):
                print(f"{i + 1} - {manifestacoes[i]}")
                print()  
            print()
        else:
            print("[ERRO] Não existem manifestações cadastradas!")

    elif opcao == 2:
        novaManifestacao = input("Digite uma nova manifestação: ")
        manifestacoes.append(novaManifestacao)
        print()
        print("Manifestação criada com sucesso!")
        print()
    
    elif opcao == 3:
        if len(manifestacoes) > 0:  
            quantidade = len(manifestacoes)
            print(f"Quantidade de manifestações: {quantidade}.")
        else:
            print("Não existem manifestações cadastradas.")
            
    elif opcao == 4:
        if len(manifestacoes) == 0:
            print("Não há nenhuma manifestação para pesquisar.")
        else:
            codigo = int(input("Digite o código da manifestação que deseja pesquisar: "))
            print()
            if 1 <= codigo <= len(manifestacoes): 
                print(f"Código: {codigo} \nManifestação: {manifestacoes[codigo - 1]}.")
                print()  
            else:
                print("[ERRO] Código inválido!")  
            
    elif opcao == 5:
        if len(manifestacoes) == 0:
            print("Não há nenhuma manifestação para excluir.")
        else:
            excluir = int(input("Digite o código da manifestação que deseja excluir: "))
            if 1 <= excluir <= len(manifestacoes):  
                manifestacoes.pop(excluir - 1)  
                print(f"A manifestação {excluir} foi excluída com sucesso!")  
            else:
                print("[ERRO] Código inválido!")  
    elif opcao != 6:
        print("[ERRO] Opção Inválida, tente novamente.")

print("Obrigado por usar o Sistema de Ouvidoria da Universidade XYZ!")
