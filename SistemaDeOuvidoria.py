from operacoesbd import *  

endSGBD = 'localhost'
usuarioSGBD = 'root'
senhaSGBD = '12345'
schemaSGBD = 'ouvidoria_xyz'

conexao = criarConexao(endSGBD, usuarioSGBD, senhaSGBD, schemaSGBD)
print("====== Ouvidoria - Universidade XYZ ======")

opcao = 1
while opcao != 7:
    print('''
 MENU:
 1) Listagem das manifestações
 2) Listagem de manifestações por tipo
 3) Criar uma nova manifestação
 4) Exibir quantidade de manifestações
 5) Pesquisar uma manifestação por código
 6) Excluir uma manifestação pelo código
 7) Sair do sistema
 ''')

    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        consultaListagem = 'select * from ouvidoria'
        manifestacoes = listarBancoDados(conexao, consultaListagem)

        if len(manifestacoes) > 0:
            print("====== LISTA DE MANIFESTAÇÕES ======")
            for i in manifestacoes:
                print(f"\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]}\n")
        else:
            print("Não há manifestações cadastradas no momento.")
    
    elif opcao == 2:
        tipoEscolhido = int(input("Selecione o tipo de manifestação que deseja pesquisar: \n1) Reclamação 2) Elogio 3) Sugestão 4) Informação: "))

        # Associa a entrada numérica ao tipo correspondente.
        if tipoEscolhido == 1:
            tipo = 'Reclamação'
        elif tipoEscolhido == 2:
            tipo = 'Elogio'
        elif tipoEscolhido == 3:
            tipo = 'Sugestão'
        elif tipoEscolhido == 4:
            tipo = 'Informação'
        else:
            print("Opção inválida. Tente novamente.")
            continue  

        consultaPorTipo = "select * from ouvidoria where tipo = %s"
        manifestacoesPorTipo = listarBancoDados(conexao, consultaPorTipo, (tipo,))

        if manifestacoesPorTipo:
            print(f"\nManifestações do tipo - {tipo}:")
            for i in manifestacoesPorTipo:
                print(f"\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]}\n")
        else:
            print(f"Não há manifestações do tipo '{tipo}' no momento.")
    
    elif opcao == 3:
        consultaInserir = 'insert into ouvidoria (autor, descricao, tipo) values (%s, %s, %s)'

        autorManifestacao = input("Digite seu nome: ")
        descManifestacao = input("Digite sua manifestação: ")
        tipoManifestacaoInt = int(input("Digite o tipo de manifestação: \n1) Reclamação 2) Elogio 3) Sugestão 4) Informação: "))

        # Mapeia o tipo de manifestação conforme a entrada numérica.
        if tipoManifestacaoInt == 1:
            tipoManifestacao = "Reclamação"
        elif tipoManifestacaoInt == 2:
            tipoManifestacao = "Elogio"
        elif tipoManifestacaoInt == 3:
            tipoManifestacao = "Sugestão"
        elif tipoManifestacaoInt == 4:
            tipoManifestacao = "Informação"
        else:
            print("Opção inválida. Tente novamente.")
            continue  

        dados = [autorManifestacao, descManifestacao, tipoManifestacao]
        insertNoBancoDados(conexao, consultaInserir, dados)
        print("Manifestação inserida com sucesso!")
    
    elif opcao == 4:
        consultaQuantidade = 'select count(*) from ouvidoria'
        quantidade = listarBancoDados(conexao, consultaQuantidade)

        if quantidade:
            print(f"\nAtualmente temos {quantidade[0][0]} manifestações registradas em nosso sistema.")
        else:
            print("Ainda não há manifestações em nosso sistema.")
    
    elif opcao == 5:
        codigoPesquisa = int(input("Digite o código da sua pesquisa: "))
        consultaListagem = 'select * from ouvidoria where codigo = %s'
        dados = [codigoPesquisa]

        ouvidoria = listarBancoDados(conexao, consultaListagem, dados)

        if len(ouvidoria) > 0:
            for i in ouvidoria:
                print(f'\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]} \n')
        else:
            print("Não há nenhuma manifestação com esse código.")
    
    elif opcao == 6:
        codigoManifestacao = int(input("Digite o código da manifestação: "))
        consultaRemocao = 'delete from ouvidoria where codigo = %s'
        dados = [codigoManifestacao]

        linhasAfetadas = excluirBancoDados(conexao, consultaRemocao, dados)

        if linhasAfetadas > 0:
            print(f"Manifestação com o código {codigoManifestacao} removida com sucesso!")
        else:
            print("Não existe nenhuma manifestação com o código informado. Tente novamente.")
    
    elif opcao != 7:
        print('Opção inválida.')
        
print("\n====== Obrigado por usar o programa da Ouvidoria. Até a próxima! ======")

encerrarConexao(conexao)
