# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:

#c=1 while c !=10:

#print(c)

# c+=1

# print(‘Acabou’)

#__________________________________________________________________________________________________________________________________________#

# VAMOS USAR O WHILE QUNADO NÃO TEMOS A QUANTIADE, NO CASO O WHITE VAI ASSUMR O LUGAR DO FOR 

'''r = "s"
while r== "s":
    n = int(input('digite um valor:'))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('fim')  '''


n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um numero: '))
    if n != 0:
        if n %2 ==0:
            par += 1 
        else:
            impar += 1
print('voçe digitou {} N° PARES e {} N° impa'.format(par, impar))        




