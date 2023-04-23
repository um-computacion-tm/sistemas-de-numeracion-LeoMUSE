def hexadecimalaDecimal(Num):

    decimal = 0
    posicion = 0

    for digito in Num[::-1]:
        valor = int(digito, 16)
        decimal += valor * (16 ** posicion)
        posicion += 1

    return decimal
   
def hexadecimalaOctal(Num):

    Num = hexadecimalaDecimal(Num)

    if Num <= 0:
        return "0"
    
    binario = str("")
    
    while Num > 0:
        resto = int(Num % 8)
        Num = int(Num / 8)
        binario = str(resto) + binario
    
    return int(binario)

if __name__ == '__main__':
    pass