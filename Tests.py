import unittest

from BinarioaDecimal import binarioaDecimal
from DecimalaBinario import decimalaBinario

class TestNumeracion(unittest.TestCase):

#binario a decimal

    def testbinarioadecimal_1(self):
        self.assertEqual(binarioaDecimal("01011100") , 92)

    def testbinarioadecimal_2(self):
        self.assertEqual(binarioaDecimal("100010") , 34)

    def testbinarioadecimal_3(self):
        self.assertEqual(binarioaDecimal("11110001110") , 1934)

#decimal a binario
    
    def testdecimalabinario_1(self):
        self.assertEqual(decimalaBinario(97), "01100001")

    def testdecimalabinario_2(self):
        self.assertEqual(decimalaBinario(54), "00110110")

    def testdecimalabinario_3(self):
        self.assertEqual(decimalaBinario(1934), "0000011110001110")

if __name__ == '__main__':
    unittest.main()