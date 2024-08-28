import math
from time import sleep
import time

print('-=- Sistema de Empréstimo Bancário -=-')

valorcasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Informe o total de anos para pagar: '))
mes = valorcasa / (anos * 12)
casa = salario * 0.30

print('\nCalculando solicitação...')
time.sleep(3)

if mes <= casa:
    print(f'\nEmpréstimo Aprovado!Z\nO valor da parcela será de R${mes:.2f}')

else:
    print('\nEmpréstimo Negado!\n O valor do solicitado excede a margem necessária.')
