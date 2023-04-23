def hexadecimalaDecimal(Num):

    decimal = 0
    posicion = 0

    for digito in Num[::-1]:
        valor = int(digito, 16)
        decimal += valor * (16 ** posicion)
        posicion += 1

    return int(decimal)
   
        
if __name__ == '__main__':
    pass