def octalaDecimal(Num):

    posicion = 0
    decimal = 0
    Num = Num[::-1]

    for digito in Num:
        multiplicador = 8**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    
    return int(decimal)

def octalaBinario(Num):

    Num = str(Num)
    Num = int(octalaDecimal(Num))

    if Num <= 0:
        return "0"
    binario = ""

    while Num > 0:
        resto = int(Num % 2)
        Num = int(Num / 2)
        binario = str(resto) + binario

    while len(binario) % 8 != 0:
        binario = "0" + binario

    return binario

if __name__ == '__main__':
    pass