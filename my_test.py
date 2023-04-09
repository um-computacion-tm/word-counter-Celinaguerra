import unittest

from cont_palabras import contpalabras

class TestPalabras(unittest.TestCase):

    def test1(self):
        rdo = contpalabras("hola")
        self.assertEqual(rdo,{"hola":1})
    
    def test2 (self):
        rdo=contpalabras("buenas tardes")
        self.assertEqual(
            rdo,
            {
                "buenas":1,
                "tardes":1,
            }
        )

    def test3 (self):
        rdo=contpalabras("buenas buenas")
        self.assertEqual(
            rdo,
            {
                "buenas":2
            }
        )

    def test4 (self):
        rdo=contpalabras("hola hola lero lero")
        self.assertEqual(
            rdo,
            {
                "hola":2,
                "lero":2,
            }
        )

if __name__ == "__main__":
    unittest.main()