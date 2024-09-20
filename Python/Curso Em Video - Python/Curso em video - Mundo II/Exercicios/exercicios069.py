tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar ?')).strip().upper()[0]
        if resp == 'N':
            break
print(f'Total de pessoas com maus de 18 anos: {tot18}')
print(f'Ao todo temos {totH} de homens cadastrados no sistema.')  
print(f'E temos {totM20} mulheres com menos de 18 anos...')     