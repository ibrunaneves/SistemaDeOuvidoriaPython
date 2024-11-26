from operacoesbd import *
def consultaListagem(conexao):
    consultaListagem = 'select * from ouvidoria'
    manifestacoes = listarBancoDados(conexao, consultaListagem)

    if len(manifestacoes) > 0:
        print("====== LISTA DE MANIFESTAÇÕES ======")
        for i in manifestacoes:
            print(f"\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]}\n")
    else:
        print("Não há manifestações cadastradas no momento.")
def tipoEscolhido(conexao):
    tipoEscolhido = int(input("Selecione o tipo de manifestação que deseja pesquisar: \n1) Reclamação 2) Elogio 3) Sugestão 4) Informação: "))

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
        return  

    consultaPorTipo = "select * from ouvidoria where tipo = %s"
    manifestacoesPorTipo = listarBancoDados(conexao, consultaPorTipo, (tipo,))

    if manifestacoesPorTipo:
        print(f"\nManifestações do tipo - {tipo}:")
        for i in manifestacoesPorTipo:
            print(f"\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]}\n")
    else:
        print(f"Não há manifestações do tipo '{tipo}' no momento.")

def consultaInserir(conexao):
    consultaInserir = 'insert into ouvidoria (autor, descricao, tipo) values (%s, %s, %s)'

    autorManifestacao = input("Digite seu nome: ")
    descManifestacao = input("Digite sua manifestação: ")
    tipoManifestacaoInt = int(input("Digite o tipo de manifestação: \n1) Reclamação 2) Elogio 3) Sugestão 4) Informação: "))

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
        return  

    dados = [autorManifestacao, descManifestacao, tipoManifestacao]
    insertNoBancoDados(conexao, consultaInserir, dados)
    print("Manifestação inserida com sucesso!")
def consultaQuantidade(conexao):
    consultaQuantidade = 'select count(*) from ouvidoria'
    quantidade = listarBancoDados(conexao, consultaQuantidade)

    if quantidade:
        print(f"\nAtualmente temos {quantidade[0][0]} manifestações registradas em nosso sistema.")
    else:
        print("Ainda não há manifestações em nosso sistema.")
def codigoPesquisa(conexao):
    codigoPesquisa = int(input("Digite o código da sua pesquisa: "))
    consultaListagem = 'select * from ouvidoria where codigo = %s'
    dados = [codigoPesquisa]

    ouvidoria = listarBancoDados(conexao, consultaListagem, dados)

    if len(ouvidoria) > 0:
        for i in ouvidoria:
            print(f'\nAutor: {i[1]} \nDescrição: {i[2]} \nTipo: {i[3]} \nCódigo: {i[0]} \n')
    else:
        print("Não há nenhuma manifestação com esse código.")
def codigoManifestacao(conexao):
    codigoManifestacao = int(input("Digite o código da manifestação: "))
    consultaRemocao = 'delete from ouvidoria where codigo = %s'
    dados = [codigoManifestacao]

    linhasAfetadas = excluirBancoDados(conexao, consultaRemocao, dados)

    if linhasAfetadas > 0:
        print(f"Manifestação com o código {codigoManifestacao} removida com sucesso!")
    else:
        print("Não existe nenhuma manifestação com o código informado. Tente novamente.")
