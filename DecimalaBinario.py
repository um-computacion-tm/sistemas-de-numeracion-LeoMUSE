def decimalaBinario(Num):
    if Num <= 0:
        return "0"
    
    binario = str("")
    
    while Num > 0:
        resto = int(Num % 2)
        Num = int(Num / 2)
        binario = str(resto) + binario
    
    while len(binario) % 8 != 0:
        binario = "0" + binario

    return str(binario)

    if __name__ == '__main__':
        pass