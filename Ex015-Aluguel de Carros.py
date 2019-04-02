'''
Exercício Python 015: Escreva um programa que pergunte a quantidade
de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
'''


km_percorrido = float(input('Digite a quantidade de Km percorridos: '))
dias_alugado = int(input('Digite a quantidade de dias do aluguel: '))

preco_km = km_percorrido * 0.15
preco_dia = dias_alugado * 60
total = preco_km + preco_dia

print()

print(f'Preço a pagar pelos dias: {preco_dia}\n')
print(f'Preço a pagar pelos km rodados: {preco_km}\n')
print(f'Total a ser pago: {total}')



