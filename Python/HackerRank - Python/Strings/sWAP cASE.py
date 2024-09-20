def swap_case(s): # criando uma função def
    return s.swapcase()

if __name__ == '__main__':
    s = input() # input para digitar a frase.
    result = swap_case(s)
    #lt = swap_case(s)
    print(result)
        #print(result)


# EXPLICAÇÃO DA FUNÇÃO: swap_case()
# Função é usada para converter todos os caracteres maiúsculos de uma string para minúsculos 
# e todos os caracteres minúsculos para maiúsculos.Ela é especialmente útil quando se deseja 
# alternar o caso de cada caractere em uma string.