# Desafio com Funções
''' 
Criar um programa que calcula a quantidade de tinta necessária parapintar uma parede.O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita
de x latas de tinta'
'''

rendimento = int(input('Qual é o rendimento da lata?'))
altura = int(input('Qual é a altura da parede'))
largura = int(input('Qual é a largura da parede'))


def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tintas')


calculo_tinta()