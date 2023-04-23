def hexadecimalaDecimal(Num):

    decimal = 0
    posicion = 0

    for digito in Num[::-1]:
        valor = int(digito, 16)
        decimal += valor * (16 ** posicion)
        posicion += 1

    return decimal

def hexadecimalaBinario(Num):

    Num = hexadecimalaDecimal(Num)

    if Num <= 0:
        return "0"
    
    binario = str("")
    
    while Num > 0:
        resto = int(Num % 2)
        Num = int(Num / 2)
        binario = str(resto) + binario
    
    while len(binario) % 8 != 0:
        binario = "0" + binario

    return binario

if __name__ == '__main__': 
    pass