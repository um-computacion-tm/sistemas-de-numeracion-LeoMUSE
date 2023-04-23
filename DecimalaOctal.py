def decimalaOctal(Num):
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