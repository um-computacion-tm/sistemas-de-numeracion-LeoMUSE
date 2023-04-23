def octalaDecimal(Num):

    posicion = 0
    decimal = 0
    Num = Num[::-1]

    for digito in Num:
        multiplicador = 8**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    
    return (decimal)

def octalaHexadecimal(Num):

    Num = str(Num)
    Num = int(octalaDecimal(Num))

    if Num == 0:
        return "0"   
    else:
        hexadecimal = ""
        while Num > 0:
            resto = Num % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(resto - 10 + ord("A")) + hexadecimal
            Num //= 16
        
        return hexadecimal
    
if __name__ == '__main__':
    pass