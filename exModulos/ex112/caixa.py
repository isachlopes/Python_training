#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidades import moeda
from utilidades import dado
preco = dado.moneyread('Digite preço: R$')
moeda.resumo(preco, 20, 10)