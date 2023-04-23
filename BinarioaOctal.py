def binarioaDecimal(Num):

    posicion = 0
    decimal = 0
    Num = Num[::-1]

    for digito in Num:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    return decimal

def binarioaOctal(Num):
    
    decimal = binarioaDecimal(Num)
    octal = ""
   
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal = decimal // 8

    return int(octal)

if __name__ == '__main__':
    pass