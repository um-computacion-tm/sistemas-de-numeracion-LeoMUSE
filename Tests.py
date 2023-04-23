import unittest

from DecimalaBinario import decimalaBinario
from DecimalaOctal import decimalaOctal
from DecimalaHexadecimal import decimalaHexadecimal
from BinarioaDecimal import binarioaDecimal
from BinarioaOctal import binarioaOctal
from BinarioaHexadecimal import binarioaHexadecimal
from OctalaDecimal import octalaDecimal
from OctalaBinario import octalaBinario
from OctalaHexadecimal import octalaHexadecimal
from HexadeciamalaDecimal import hexadecimalaDecimal
from HexadecimalaBinario import hexadecimalaBinario
from HexadecimalaOctal import hexadecimalaOctal

class TestNumeracion(unittest.TestCase):

#decimal a binario
    
    def test_decimal_a_binario_1(self):
        self.assertEqual(decimalaBinario(97), "01100001")

    def test_decimal_a_binario_2(self):
        self.assertEqual(decimalaBinario(54), "00110110")

    def test_decimal_a_binario_3(self):
        self.assertEqual(decimalaBinario(1934), "0000011110001110")

#decimal a octal

    def test_decimal_a_octal_1(self):
        self.assertEqual(decimalaOctal(97), 141)

    def test_decimal_a_octal_2(self):
        self.assertEqual(decimalaOctal(54), 66)

    def test_decimal_a_octal_3(self):
        self.assertEqual(decimalaOctal(1934), 3616)

#decimal a hexadecimal

    def test_decimal_a_hexadecimal_1(self):
        self.assertEqual(decimalaHexadecimal(97), "61")

    def test_decimal_a_hexadecimal_2(self):
        self.assertEqual(decimalaHexadecimal(54), "36")

    def test_decimal_a_hexadecimal_3(self):
        self.assertEqual(decimalaHexadecimal(1934), "78E")

#binario a decimal

    def test_binario_a_decimal_1(self):
        self.assertEqual(binarioaDecimal("01100001") , 97)

    def test_binario_a_decimal_2(self):
        self.assertEqual(binarioaDecimal("00110110") , 54)

    def test_binario_a_decimal_3(self):
        self.assertEqual(binarioaDecimal("0000011110001110") , 1934)

#binario a octal

    def test_binario_a_octal_1(self):
       self.assertEqual(binarioaOctal("01100001") , 141)

    def test_binario_a_octal_2(self):
        self.assertEqual(binarioaOctal("00110110") , 66)

    def test_binario_a_octal_3(self):
        self.assertEqual(binarioaOctal("0000011110001110") , 3616)

#binario a hexadecimal

    def test_binario_a_hexadecimal_1(self):
       self.assertEqual(binarioaHexadecimal("01100001") , "61")

    def test_binario_a_hexadecimal_2(self):
        self.assertEqual(binarioaHexadecimal("00110110") , "36")

    def test_binario_a_hexadecimal_3(self):
        self.assertEqual(binarioaHexadecimal("0000011110001110") , "78E")

#octal a decimal

    def test_octal_a_decimal_1(self):
       self.assertEqual(octalaDecimal(141) , 97)

    def test_octal_a_decimal_2(self):
        self.assertEqual(octalaDecimal(66) , 54)

    def test_octal_a_decimal_3(self):
        self.assertEqual(octalaDecimal(3616) , 1934)

#octal a binario

    def test_octal_a_binario_1(self):
       self.assertEqual(octalaBinario(141) , "01100001")

    def test_octal_a_binario_2(self):
        self.assertEqual(octalaBinario(66) ,"00110110")

    def test_octal_a_binario_3(self):
        self.assertEqual(octalaBinario(3616) , "0000011110001110")

#octal a hexadecimal

    def test_octal_a_hexadecimal_1(self):
       self.assertEqual(octalaHexadecimal(141) , "61")

    def test_octal_a_hexadeciaml_2(self):
        self.assertEqual(octalaHexadecimal(66) , "36")

    def test_octal_a_hexadecimal_3(self):
        self.assertEqual(octalaHexadecimal(3616) , "78E")

#hexadecimal a decimal

    def test_hexadecimal_a_decimal_1(self):
       self.assertEqual(hexadecimalaDecimal("61") , 97)

    def test_hexadecimal_a_decimal_2(self):
        self.assertEqual(hexadecimalaDecimal("36") , 54)

    def test_hexadecimal_a_decimal_3(self):
        self.assertEqual(hexadecimalaDecimal("78E") , 1934)

#hexadecimal a binario

    def test_hexadecimal_a_binario_1(self):
       self.assertEqual(hexadecimalaBinario("61") , "01100001")

    def test_hexadecimal_a_binario_2(self):
        self.assertEqual(hexadecimalaBinario("36") , "00110110")

    def test_hexadecimal_a_binario_3(self):
        self.assertEqual(hexadecimalaBinario("78E") , "0000011110001110")

#hexadecimal a octal

    def test_hexadecimal_a_octal_1(self):
       self.assertEqual(hexadecimalaOctal("61") , 141)

    def test_hexadecimal_a_octal_2(self):
        self.assertEqual(hexadecimalaOctal("36") , 66)

    def test_hexadecimal_a_octal_3(self):
        self.assertEqual(hexadecimalaOctal("78E") , 3616)

if __name__ == '__main__':
    unittest.main()