import unittest
import sys
sys.path.append('../')
from ppu import strings,dicts

class MyTest(unittest.TestCase):
    def test_strings(self):
        result = [1,2,3,4]
        self.assertEqual(strings.string2nums("1,2,3,4"),result)
    def test_strings_sep(self):
        result = [1,2,3,4]
        self.assertEqual(strings.string2nums("1;2;3;4",separator=';'),result)
    def test_maxdict(self):
        ques = {'a':12,'b':13,'c':15,'d':12}
        result = ['a','d']
        self.assertEqual(dicts.max_dict(ques),result)


if __name__ == '__main__':
    unittest.main()
