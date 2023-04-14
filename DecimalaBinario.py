def decimalaBinario(Num):
    if Num <= 0:
        return "0"
    
    binario = str("")
    
    while Num > 0:
    
        residuo = int(Num % 2)
        Num = int(Num / 2)
        binario = str(residuo) + binario
    
    while len(binario) % 8 != 0:
        binario = "0" + binario

    return binario

    if __name__ == '__main__':
        pass