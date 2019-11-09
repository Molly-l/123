import unittest
from test001 import test1, test2, test3, test4


class TestNew(unittest.TestCase):
    '''这是一个用于测试的类'''

    def test_ceshi_0(self):
        '''测试开始1'''
        ce_shi = test1(4)
        self.assertEqual(ce_shi, 16)

    def test_ceshi_1(self):
        '''测试2'''
        ce_shi2 = test2('yin', 8000)
        self.assertNotEqual(ce_shi2, 'yin800000')

    def test_ceshi_2(self):
        '''测试3'''
        ce_shi3 = test3(2)

        self.assertTrue(ce_shi3)

    def asd_ceshi_3(self):
        '''测试4'''
        ce_shi4 = test3(2.3)

        self.assertTrue(ce_shi4)

    def test_ceshi_4(self):
        '''测试5'''
        ce_shi5 = test4('name')
        self.assertIn(ce_shi5, [1, 2, 3])

    def test_ceshi_5(self):
        '''测试6'''
        ce_shi6 = test4(123)
        self.assertNotIn(ce_shi6, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
