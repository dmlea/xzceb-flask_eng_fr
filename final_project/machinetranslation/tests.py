import unittest

from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_french_to_english(self):
        if self==None:
            print('input is null')
        else:
            self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_english_to_french(self):
        if self==None:
            print('input is null')
        else:
            self.assertEqual(english_to_french('Hello'),'Bonjour')

if __name__=='__main__':
    unittest.main()

