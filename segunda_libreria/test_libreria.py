import unittest
import math
import libreria_complejos_version_2 as complejos

class Test_complejos(unittest.TestCase):

    def test_suma_vectores(self):
        self.assertEqual(complejos.suma_vectores_complejos([8+3j,-1-4j,-9j],[8-3j,2+5j,3]),[16,1+1j,3-9j])
    def test_inverso_aditivo(self):
        self.assertEqual(complejos.inverso_aditivo_vector_complejo([-5+2j,3,-1j]),[5-2j,-3,1j])
    def test_producto_escalar(self):
        self.assertEqual(complejos.multiplicacion_escalar_vector(-1+1j,[-2+5j,-1-1j,2-9j]),[-3-7j,2,7+11j])
    def test_suma_matrices(self):
        self.assertEqual(complejos.adicion_matrices_complejas([[-8-3j,-6-4j,-4j],[-1+8j,6-10j,8-5j],[4,8+5j,-7-9j]],[[-7-2j,-4-2j,7+7j],[5+9j,3j,6-5j],[1+5j,-6-6j,5+8j]]),[[(-15-5j), (-10-6j), (7+3j)], [(4+17j), (6-7j), (14-10j)], [(5+5j), (2-1j), (-2-1j)]])
    def test_inverso_aditivo_matriz(self):
        self.assertEqual(complejos.inverso_aditivo_matriz_compleja([[7+3j,-9-4j],[-1+7j,-7-9j]]),[[-7-3j,9+4j],[1-7j,7+9j]])
    def test_producto_escalar_matriz_compleja(self):
        self.assertEqual(complejos.multiplicacion_escalar_matriz_compleja(-2+3j,[[3-2j,4-10j],[8-4j,-2-8j]]),[[13j,22+32j],[-4+32j,28+10j]])
    def test_transpuesta_matriz(self):
        self.assertEqual(complejos.transpuesta_matriz_compleja([[5+9j,8+2j],[-7-5j,-3-7j],[-1-4j,7-8j]]),[[5+9j,-7-5j,-1-4j],[8+2j,-3-7j,7-8j]])
    def test_conjugada_matriz(self):
        self.assertEqual(complejos.conjugada_matriz_compleja([[-6+1j,2-6j],[3+8j,3]]),[[-6-1j,2+6j],[3-8j,3]])
    def test_producto_matrices(self):
        #self.assertEqual(complejos.producto_matrices_complejas([[2+1j,3,1-1j],[0,-2j,7-3j],[3,0,1-2j]],[[-1j,1],[0,1j]]), None)
        self.assertEqual(complejos.producto_matrices_complejas([[-6+2j,6j,7+2j],[6+9j,7+7j,-6-6j],[5+8j,-6+8j,6+9j]],[[9-6j,-3-4j,5-2j],[3+6j,-1-5j,-5j],[9+9j,8-4j,-8-4j]]),[[(-33+153j), (120+0j), (-44-22j)], [(87+0j), (-26-117j), (107+70j)], [165j, (147+26j), (69-36j)]])
    def test_adjunta_matriz(self):
        self.assertEqual(complejos.adjunta_matriz_compleja([[7+7j,3+8j,8+4j],[5,8-6j,-10-1j]]),[[7-7j,5],[3-8j,8+6j],[8-4j,-10+1j]])

    def test_accion_matriz(self):
        self.assertEqual(complejos.accion_matriz_vector([[-1+5j,1-7j,-6+3j],[-3-9j,2-5j,1-10j],[-6+5j,6-5j,3-2j]],[1-3j,4+3j,-3+1j]),[54-32j,17j,41+30j])
    def test_producto_interno_vectores(self):
        self.assertEqual(complejos.producto_interno_vectores([2-1j,-8-5j,-2-6j],[6-3j,5-1j,-6-2j]),4+1j)
    
    
if __name__ == "__main__":
    unittest.main()
