
import unittest
import sudoku


class TestSudoku(unittest.TestCase):

    def test_item_family(self):
        '''
        Test .__getitem__() and .__setitem__() to see if:
        1. item subscription is supported
        2. item assignment (and thereby item mutation) is supported
        '''

        eg = [  
            ['1', '.', '3', '.'],
            ['.', '2', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '4']
        ]
        eg = sudoku.Sudoku(eg, elements = {'1', '2', '3', '4'})

        # 1. item subscription
        result_select = (eg[(1, 1)] == '2')
        expected_result_select = True

        # 2. item assignment to the empty entry
        eg[(0, 1)] = '4'
        result_assign = list(eg.show[0]) == ['1', '4', '3', '.']
        expected_result_assign = True

        result = {
            'getitem_subscript': result_select, 
            'setitem_assign': result_assign
        }
        expected_result = {
            'getitem_subscript': expected_result_select, 
            'setitem_assign': expected_result_assign
        }

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main(exit = False)
