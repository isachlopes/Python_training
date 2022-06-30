from modulos.lib import *
from modulos.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):    
    criararquivo(arq)

while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resp == 1:#opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resp == 2:#CADASTRAR UMA NOVA PESSOA
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema. Até logo!...')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1)
    