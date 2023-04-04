import unittest
def contpalabras(palabra):
    numpalabras = len(palabra.split())
    return {palabra:numpalabras}



class TestPalabras(unittest.TestCase):

    def test1(self):
        rdo = contpalabras("hola")
        self.assertEqual(rdo,{"hola":1})
    
    def test2 (self):
        rdo=contpalabras("buenas tardes")
        self.assertEqual(rdo,{"buenas tardes":2})

    def test3 (self):
        rdo=contpalabras("habia una vez un lobo muy pequeño")
        self.assertEqual(rdo,{"habia una vez un lobo muy pequeño":7})

    def test4 (self):
        rdo=contpalabras("buenas buenas, como va todo?")
        self.assertEqual(rdo,{"buenas buenas, como va todo?":5})


if __name__=="__main__":
    unittest.main()