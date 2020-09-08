import unittest
from main import calculo


class Test(unittest.TestCase):
    def test_calculo(self):
        RESULT=calculo()
        self.assertEqual("par", RESULT)
