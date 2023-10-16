import unittest

from app import changeFromRoman

class TestChangeFromRoman(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(changeFromRoman("I"), 1)
        self.assertEqual(changeFromRoman("V"), 5)
        self.assertEqual(changeFromRoman("X"), 10)
        self.assertEqual(changeFromRoman("L"), 50)
        self.assertEqual(changeFromRoman("C"), 100)
        self.assertEqual(changeFromRoman("D"), 500)
        self.assertEqual(changeFromRoman("M"), 1000)
        self.assertEqual(changeFromRoman("VIII"), 8) 
        self.assertEqual(changeFromRoman("XXIII"), 23) 
        self.assertEqual(changeFromRoman("IX"), 9)
        self.assertEqual(changeFromRoman("XXIV"), 24) 
        self.assertEqual(changeFromRoman("III"), 3)
        self.assertEqual(changeFromRoman("Z"), "invalid")
        self.assertEqual(changeFromRoman("CIZ"), "invalid")
        self.assertEqual(changeFromRoman("VV"), "invalid")
        self.assertEqual(changeFromRoman("IIII"), "invalid")
        self.assertEqual(changeFromRoman(None), "invalid")
        
unittest.main()