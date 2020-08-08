import unittest
import math
import libreria_complejos as complejos

class Test_complejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(complejos.sumar_complejos([1,2], [3,4]), [4,6])
    def test_producto(self):
        self.assertEqual(complejos.producto_complejos([-3,-1], [1,-2]),[-5, 5])
    def test_resta(self):
        self.assertEqual(complejos.resta_complejos([5,3], [2,9]), [3,-6])
    def test_division(self):
        self.assertEqual(complejos.division_complejos([0,3],[-1,-1]),[-1.5,-1.5])
        self.assertEqual(complejos.division_complejos([5,4],[0,0]), None)
    def test_modulo(self):
        self.assertEqual(complejos.modulo_complejo([4,-3]),5)
        self.assertEqual(complejos.modulo_complejo([2,-1]),2.2361)
    def test_conjugado(self):
        self.assertEqual(complejos.conjugado([10,20]),[10,-20])
        self.assertEqual(complejos.conjugado([7,0]),[7,0])
        self.assertEqual(complejos.conjugado([3,-21]),[3,21])

    def test_cartesiano_a_polar(self):
        self.assertEqual(complejos.cartesiano_a_polar([0,3]),[3.0,1.5708])
        self.assertEqual(complejos.cartesiano_a_polar([1,-math.sqrt(3)]),[2.0,-1.0472])
    
    def test_fase(self):
        self.assertEqual(complejos.fase_complejo([5,3]),0.5404)
        
        
if __name__ == "__main__":
    unittest.main()
