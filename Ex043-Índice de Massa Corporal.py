'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)   # ou (altura * altura)

print('Com um peso de {} e uma altura de {} você tem um IMC de {:.2f}'.format(peso,altura,imc))

if imc < 18.5:
    print('Você está abaixo do peso !')

elif imc <= 25:
    print('Você está no peso ideal !')

elif imc <= 30:
    print('Você está com sobre peso !')

elif imc <= 40:
    print('Você esta com Obesidade !')

elif imc > 40:
    print('Procure um medico urgente!!! Você esta com Obesidade Morbida !')
