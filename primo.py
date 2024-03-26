import unittest

def is_primo(value):
    for div in range(2, value):
        if value % div == 0:
            return False 
    else:
        return True 
        

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_21(self):
        result = is_primo(21)
        self.assertEqual(result, False)

unittest.main()