    
try:
    a = int(input('Nemeraodr: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voçe digitou.')
except ZeroDivisionError:
    print('não é possivel dividir um numero por zero! ')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados! ')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r: 1f}')
finally:
    print(f'Volte sempre! Muito obrigado!')    