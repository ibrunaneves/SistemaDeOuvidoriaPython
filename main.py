from operacoesbd import *
from Ouvidoriadef import *

opcao = 1
endSGBD = 'localhost'
usuarioSGBD = 'root'
senhaSGBD = '12345'
schemaSGBD = 'ouvidoria_xyz'
conexao = criarConexao(endSGBD, usuarioSGBD, senhaSGBD, schemaSGBD)

print("====== Ouvidoria - Universidade XYZ ======")

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
        consultaListagem(conexao)
    elif opcao == 2:
        tipoEscolhido(conexao)
    elif opcao == 3:
        consultaInserir(conexao)
    elif opcao == 4:
        consultaQuantidade(conexao)
    elif opcao == 5:
        codigoPesquisa(conexao)
    elif opcao == 6:
        codigoManifestacao(conexao)
    elif opcao != 7:
        print('Opção inválida.')

print("\n====== Obrigado por usar o programa da Ouvidoria. Até a próxima! ======")

encerrarConexao(conexao)