def binarioaDecimal(Num):

    posicion = 0
    decimal = 0
    Num = Num[::-1]

    for digito in Num:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    return decimal

def binarioaHexadecimal(Num):

    decimal = binarioaDecimal(Num)

    if decimal == 0:
        return "0"
    else:
        hexadecimal = ""
        while decimal > 0:
            resto = decimal % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(resto - 10 + ord("A")) + hexadecimal
            decimal //= 16        
    
        return str(hexadecimal)
    
if __name__ == '__main__':
    pass