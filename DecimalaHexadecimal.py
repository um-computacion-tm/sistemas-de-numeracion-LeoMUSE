def decimalaHexadecimal(Num):
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
        
        return str(hexadecimal)
    
if __name__ == '__main__':
    pass