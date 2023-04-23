def octalaDecimal(Num):

    Num = str(Num)
    posicion = 0
    decimal = 0
    Num = Num[::-1]

    for digito in Num:
        multiplicador = 8**posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    return int(decimal)
        
if __name__ == '__main__':
    pass