'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
- ACUTANGULO: todos os lados menores que 90°
'''

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b+c and b < a+c and c < a+b:
    print('É um triangulo')

    if a == b == c: # ou a == b and b == c:
        print('Triângulo Equilatero')

    elif  a != b != c != a:  #ou a != b and b != c and c != a:
        print('Triângulo escaleno')

    elif a < 90 and b < 90 and c < 90:
        print('Triângulo acutângulo')

    elif a == b or b == c or a == c:
        print('Triângulo Isosceles')

else:
    print('Não é um triangulo')

