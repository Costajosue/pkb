def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válidas.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else: 
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válidas.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else: 
         return n
        
n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('digite um real: ')
print(f'O valor inteiro digitando foi {n1} e o real foi {n2}')