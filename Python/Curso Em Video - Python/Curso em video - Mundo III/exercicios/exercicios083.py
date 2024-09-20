# Exercício Python 083: 
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: '))
pinha = []
for simb in expr:
    if simb == '(':
        pinha.append('(')
    elif simb == ')':
        if len(pinha) > 0:
            pinha.pop()
    else:
        pinha.append(')')
        break
if len(pinha) == 0:
    print('VAlida!')
else:
    print('Invalida!')