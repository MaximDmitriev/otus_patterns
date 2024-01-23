import unittest
from main import solve

class SolveTest(unittest.TestCase):
    '''Тесты для функции solve'''

    def test_a_equals_zero(self):
        '''При a == 0 функция возвращает ошибку'''

        self.assertRaises(ValueError, lambda: solve(0, 1, 1))

    def test_types(self):
        '''При коэфициентах NaN или +/-Inf возвращает ошибку'''

        self.assertRaises(TypeError, lambda: solve(float('nan'), 1, 1))    

    def test_no_roots(self):
        '''При дискриминанте меньше 0 возвращает пустой массив'''

        result = solve(1, 0, 1)
        self.assertEqual(len(result), 0)

    def test_equals_roots(self):
        '''При дискриминанте равном 0 корни одинаковые'''

        result = solve(1, 2, 1)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], result[1])  

    def test_different_roots(self):
        '''При дискриминанте больше 0 корни разные'''

        result = solve(1, 0, -1)
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result[0], result[1])      


if __name__ == '__main__':
    unittest.main()

