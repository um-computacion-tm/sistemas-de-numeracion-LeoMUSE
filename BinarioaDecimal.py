def binarioaDecimal(Num):

    posicion = 0

    decimal = 0

    Num = Num[::-1]

    for digito in Num:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    return decimal
        
if __name__ == '__main__':
    pass