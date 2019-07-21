
import unittest
import candidate
import questions
import sudoku


# START: testing Candidate ###############################################

class TestCandidate(unittest.TestCase):

    def test_dict(self):
        '''
        Test if the following attributes of type dict are supported:
        1. .copy(); but not a shallow one but a deep one
        2. .items() (and thereby .values())
        3. .keys()
        4. .pop()
        5. .update()
        '''

        eg = candidate.Candidate(
            {
                (0, 1): {'4'}, 
                (0, 3): {'2'}, 
                (1, 0): {'4', '3'}, 
                (1, 2): {'4', '1'}, 
                (1, 3): {'1'}, 
                (2, 0): {'2', '4', '3'}, 
                (2, 1): {'4', '3', '1'}, 
                (2, 2): {'2', '1'}, 
                (2, 3): {'2', '3', '1'}, 
                (3, 0): {'2', '3'}, 
                (3, 1): {'3', '1'}, 
                (3, 2): {'2', '1'}
            }, 
            n = 2
        )

        # 1. .copy(), but not a shallow one but a deep one
        eg_cp = eg.copy()
        result_copy1 = id(eg) != id(eg_cp)
        result_copy2 = id(eg[(0, 1)]) != id(eg_cp[(0, 1)])
        result_copy = (result_copy1, result_copy2)
        expected_result_copy = (True, True)

        # 2. .items()
        eg_items = eg.items()
        result_items_type = str(type(eg_items))
        expected_items_type = "<class 'dict_items'>"
        result_items_lst = list(eg_items)
        result_items_lst.sort()
        expected_items_lst = [
            ((0, 1), {'4'}),
            ((0, 3), {'2'}), 
            ((1, 0), {'4', '3'}), 
            ((1, 2), {'4', '1'}), 
            ((1, 3), {'1'}), 
            ((2, 0), {'2', '4', '3'}), 
            ((2, 1), {'4', '3', '1'}), 
            ((2, 2), {'2', '1'}), 
            ((2, 3), {'2', '3', '1'}), 
            ((3, 0), {'2', '3'}), 
            ((3, 1), {'3', '1'}), 
            ((3, 2), {'2', '1'})
        ]
        result_items1 = (result_items_type == expected_items_type)
        result_items2 = (result_items_lst == expected_items_lst)
        result_items = (result_items1, result_items2)
        expected_result_items = (True, True)

        # 3. .keys()
        eg_keys = eg.keys()
        result_keys_type = str(type(eg_keys))
        expected_keys_type = "<class 'dict_keys'>"
        result_keys_lst = list(eg_keys)
        result_keys_lst.sort()
        expected_keys_lst = [
            (0, 1), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), 
            (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2)
        ]
        result_keys1 = (result_keys_type == expected_keys_type)
        result_keys2 = (result_keys_lst == expected_keys_lst)
        result_keys = (result_keys1, result_keys2)
        expected_result_keys = (True, True)

        # 4. .pop()
        eg.pop((0, 1))
        eg.pop((0, 3))
        eg.pop((1, 0))
        eg.pop((1, 3))
        result_pop = (eg == candidate.Candidate(
            {
                (1, 2): {'4', '1'},
                (2, 0): {'2', '4', '3'}, 
                (2, 1): {'4', '3', '1'}, 
                (2, 2): {'2', '1'}, 
                (2, 3): {'2', '3', '1'}, 
                (3, 0): {'2', '3'}, 
                (3, 1): {'3', '1'}, 
                (3, 2): {'2', '1'}
            }, 
            n = 2
        ))
        expected_result_pop = True

        # 5. .update()
        # 5.1. .update() through Candidate
        eg.update(candidate.Candidate(
            {(0, 3): {'2'}, (1, 0): {'3', '4'}},
            n = 2
        ))
        result_update1 = (eg == candidate.Candidate(
            {
                (0, 3): {'2'},
                (1, 0): {'3', '4'},
                (1, 2): {'4', '1'},
                (2, 0): {'2', '4', '3'}, 
                (2, 1): {'4', '3', '1'}, 
                (2, 2): {'2', '1'}, 
                (2, 3): {'2', '3', '1'}, 
                (3, 0): {'2', '3'}, 
                (3, 1): {'3', '1'}, 
                (3, 2): {'2', '1'}
            }, 
            n = 2
        ))
        expected_update1 = True

        # 5.2. .update() through dict
        eg.update({(0, 1): {'4'}, (1, 3): {'1'}})
        result_update2 = (eg == eg_cp)
        expected_update2 = True

        result_update = (result_update1, result_update2)
        expected_result_update = (expected_update1, expected_update2)

        result = {
            '.copy': result_copy, '.items': result_items, 
            '.keys': result_keys, '.pop': result_pop,
            '.update': result_update
        }
        expected_result = {
            '.copy': expected_result_copy, '.items': expected_result_items, 
            '.keys': expected_result_keys, '.pop': expected_result_pop,
            '.update': expected_result_update
        }
        self.assertEqual(result, expected_result)


    def test_dict_update_error(self):
        '''
        Test if .update() raises ValueError if other is of type Candidate 
        and self.n != other.n.
        '''

        eg = candidate.Candidate({(0, 1): {'4'}}, n = 2)
        updating_eg = candidate.Candidate({(8, 8): {'9'}}, n = 3)
        with self.assertRaises(ValueError): eg.update(updating_eg)


    def test_eq(self):
        '''
        Test .__eq__() to check if:
        1. two identical Candidates are evaluated as equivalent.
        2. two Candidates that have different keys but identical values 
           are evaulated as not equivalent.
        3. two Candidates that have identical keys but different values 
           are evaluated as not equivalent.
        4. two Candidates that have at least one entry with different
           key and value are evaluated as not equivalent.
        5. two Candidates that have the same keys and values but different
           n are evaluated as not equivalent.
        '''

        eg = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})

        # Case 1: same
        eg1 = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})

        # Case 2: different key same value
        eg2 = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 3): {6, 9}})

        # Case 3: same key different value
        eg3 = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 8}})

        # Case 4: different key different value
        eg4 = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 3): {6, 9}})

        # Case 5: same key same value, but different n
        eg5 = candidate.Candidate(
            {(0, 1): {1, 2, 4}, (0, 3): {6, 9}}, 
            n = 4
        )

        result = [eg == eg1, eg != eg2, eg != eg3, eg != eg4, eg != eg5]
        expected_result = [True, True, True, True, True]
        self.assertEqual(result, expected_result)


    def test_group(self):
        '''
        Test .group(by) to see if:
        1. grouping works for the case of n = 2
        2. grouping by submatrix works for n = 3
        3. grouping by submatrix works for n = 4
        4. grouping works even if candidates are not available in a
        certain group
        '''

        eg2 = candidate.Candidate(
            {
                (0, 1): {'4'}, 
                (0, 3): {'2'}, 
                (1, 0): {'4', '3'}, 
                (1, 2): {'4', '1'}, 
                (1, 3): {'1'}, 
                (2, 0): {'2', '4', '3'}, 
                (2, 1): {'4', '3', '1'}, 
                (2, 2): {'2', '1'}, 
                (2, 3): {'2', '3', '1'}, 
                (3, 0): {'2', '3'}, 
                (3, 1): {'3', '1'}, 
                (3, 2): {'2', '1'}
            }, 
            n = 2
        )
        eg3 = candidate.Candidate(
            {
                (0, 0): {'4', '9', '7', '5', '1'}, 
                (0, 1): {'5', '4'}, 
                (0, 2): {'9', '1', '7'}, 
                (0, 3): {'8', '6'}, 
                (0, 5): {'3', '8'}, 
                (0, 6): {'1', '3', '5'}, 
                (0, 7): {'5', '7', '3'}, 
                (0, 8): {'1', '3', '5'}, 
                (1, 2): {'2'}, 
                (1, 6): {'5'}, 
                (2, 0): {'2', '1', '7'}, 
                (2, 2): {'2', '1', '7'}, 
                (2, 4): {'3'}, 
                (2, 7): {'2', '7', '3'}, 
                (3, 0): {'2', '6'}, 
                (3, 2): {'2', '8', '6'}, 
                (3, 4): {'5', '7', '8', '6'}, 
                (3, 6): {'5', '8', '6'}, 
                (3, 7): {'5', '8', '6'}, 
                (4, 0): {'3', '6'}, 
                (4, 2): {'3', '8', '6'}, 
                (4, 4): {'5', '8', '6'}, 
                (4, 6): {'9', '8', '5', '3', '6'}, 
                (4, 7): {'5', '3', '8', '6'}, 
                (5, 0): {'3', '6', '4'}, 
                (5, 3): {'8', '6'}, 
                (5, 4): {'8', '6'}, 
                (5, 5): {'9', '8'}, 
                (5, 8): {'9', '3'}, 
                (6, 0): {'9', '1', '5', '3', '6', '2'}, 
                (6, 1): {'2', '8', '5'}, 
                (6, 3): {'2', '8'}, 
                (6, 4): {'3', '8'}, 
                (6, 5): {'3', '8'}, 
                (6, 7): {'8', '5', '3', '6', '2'}, 
                (6, 8): {'9', '2', '5', '3', '1'}, 
                (7, 0): {'9', '2', '3', '6', '1'}, 
                (7, 1): {'2', '8'}, 
                (7, 2): {'9', '1', '8', '3', '6', '2'}, 
                (7, 4): {'3', '8', '4'}, 
                (7, 6): {'9', '8', '3', '6', '1'}, 
                (7, 7): {'4', '8', '3', '6', '2'}, 
                (7, 8): {'9', '1', '3', '2'}, 
                (8, 0): {'5', '7', '3', '2'}, 
                (8, 1): {'2', '8', '5'}, 
                (8, 2): {'2', '7', '8', '3'}, 
                (8, 6): {'5', '3', '8'}, 
                (8, 7): {'4', '8', '5', '3', '2'}, 
                (8, 8): {'2', '3', '5'}
            }
        )
        eg4 = candidate.Candidate(
            {
                (0, 3): {'3', '9', '4', 'D', '5', 'A'},
                (0, 4): {'8', '9', 'B', '4', 'C', '5', '2', 'A'},
                (0, 5): {'8', '9', 'B', '4', 'C', '5', '2', 'A'},
                (0, 6): {'B', '4', 'C', '5'},
                (0, 7): {'9', '8', 'B', '2'},
                (0, 8): {'2', '4'},
                (0, 9): {'9', '8', '4', '2'},
                (0, 10): {'9', '2', '4'},
                (0, 11): {'9'},
                (0, 12): {'3', 'B', '9', '4'},
                (1, 0): {'5', '9', '4', '7', '2', 'E'},
                (1, 1): {'5', 'C', '7', '2', 'E', 'G'},
                (1, 2): {'2', '9', 'B', 'C', '7', '5', 'E', 'G'},
                (1, 3): {'9', '4', '7', '5', 'G'},
                (1, 4): {'1', '9', 'B', '4', '7', 'C', '5', '6', '2'},
                (1, 5): {'9', 'B', '4', '7', 'C', '5', '6', '2'},
                (1, 6): {'1', 'B', '4', '7', 'C', '5'},
                (1, 7): {'9', 'B', '7', '6', '2'},
                (1, 8): {'6', '2', 'E', '4'},
                (1, 9): {'9', '4', '6', '2', 'E'},
                (1, 15): {'6', 'B', '1'},
                (2, 0): {'8', '9', '4', 'D', '7', '2', 'A'},
                (2, 1): {'8', '3', 'D', '7', '2'},
                (2, 2): {'3', '9', '7', '2', 'A'},
                (2, 3): {'3', '9', '4', 'D', '7', 'A'},
                (2, 4): {'8', '1', '9', '4', 'F', '7', '6', '2', 'A'},
                (2, 5): {'8', '9', '4', 'F', '7', '6', '2', 'A'},
                (2, 6): {'4', 'F', '1', '7'},
                (2, 12): {'3', '9', '4', '6'},
                (2, 13): {'3', 'D'},
                (2, 14): {'1', '9', '4', 'D', '6'},
                (2, 15): {'6', '1', 'D'},
                (3, 0): {'8', '9', '4', '7', '5', 'E'},
                (3, 1): {'8', 'E', '5', '7'},
                (3, 2): {'9', 'B', '7', '5', 'E'},
                (3, 3): {'9', '5', '4', '7'},
                (3, 4): {'8', '9', 'B', '4', 'F', '7', '6', '5'},
                (3, 10): {'9', 'F', '4'},
                (3, 11): {'9', 'F', '7'},
                (3, 12): {'9', 'B', '4', '6'},
                (3, 13): {'B', '5'},
                (4, 3): {'4', 'F', 'D', '7', '6'},
                (4, 4): {'4', 'F', '7', '2', 'E'},
                (4, 5): {'4', 'F', '7', '2', 'E'},
                (4, 6): {'F', 'E', '4', '7'},
                (4, 7): {'2', '7'},
                (4, 8): {'F', '4', 'D'},
                (4, 9): {'4', 'A'},
                (4, 10): {'F', '4', 'A'},
                (4, 11): {'F', 'C', 'A'},
                (5, 1): {'5', 'G', 'D', '7'},
                (5, 2): {'5', 'G', '7'},
                (5, 3): {'4', '7', 'D', '5', 'G'},
                (5, 4): {'8', '1', '3', '4', '7', '5', 'G'},
                (5, 5): {'8', '4', '5', '7'},
                (5, 6): {'1', '4', '7', '5', 'G'},
                (5, 7): {'3', '8', '7'},
                (5, 8): {'4', '1', 'D', 'G'},
                (5, 9): {'9', '4'},
                (5, 15): {'D', 'C'},
                (6, 0): {'6', '4', 'D', '5'},
                (6, 1): {'F', 'G', 'D', '5'},
                (6, 2): {'6', 'G', '5'},
                (6, 4): {'1', '3', '4', 'F', '5', 'E', 'G'},
                (6, 5): {'F', 'E', '4', '5'},
                (6, 12): {'3', '6'},
                (6, 13): {'3', 'D'},
                (6, 14): {'6', 'D'},
                (6, 15): {'6', 'E', 'D'},
                (7, 0): {'2', '7'},
                (7, 4): {'8', 'B', 'F', '7', '2', 'G'},
                (7, 10): {'9', 'F', 'G'},
                (7, 11): {'9', 'F'},
                (7, 12): {'9', '8'},
                (7, 13): {'8'},
                (7, 14): {'9', '7'},
                (8, 4): {'9', 'C', 'D', '5', '6', '2', 'A'},
                (8, 5): {'9', 'C', '5', '6', '2', 'A'},
                (8, 6): {'C', 'D', '5'},
                (8, 7): {'9', '2', '6'},
                (8, 8): {'2', 'G'},
                (8, 9): {'9', '2', 'A'},
                (8, 10): {'9', '2', 'G', 'A'},
                (8, 11): {'9', 'A'},
                (9, 1): {'1', '5', '3', '7', '2', 'E', 'G'},
                (9, 2): {'2', '3', '9', '7', '6', '5', 'E', 'G', 'A'},
                (9, 3): {'1', '3', '9', '7', '6', '5', 'G', 'A'},
                (9, 4): {'2', '9', 'B', '7', '6', '5', 'E', 'A'},
                (9, 5): {'2', '9', 'B', '7', '6', '5', 'E', 'A'},
                (9, 6): {'B', 'E', '7', '5'},
                (9, 7): {'9', 'B', '7', '6', '2'},
                (9, 8): {'1', 'F', '2', 'E', 'G'},
                (9, 9): {'9', 'B', '2', 'E', 'A'},
                (9, 10): {'1', '9', 'F', '2', 'G', 'A'},
                (9, 14): {'6', '5'},
                (9, 15): {'6', 'B', 'F', 'A'},
                (10, 0): {'9', '7', '5', '2', 'E', 'A'},
                (10, 1): {'5', 'E', '2', '7'},
                (10, 2): {'9', '7', '5', '2', 'E', 'A'},
                (10, 3): {'9', '5', 'A', '7'},
                (10, 4): {'2', '9', 'B', 'C', '7', '5', 'E', 'A'},
                (10, 6): {'B', 'C', '7', '5', 'E'},
                (10, 12): {'8', 'B', 'C'},
                (10, 13): {'8', 'B', 'C', '5', 'A'},
                (10, 14): {'5'},
                (10, 15): {'B', 'F', 'C', 'A'},
                (11, 0): {'6', 'E', 'D', 'A'},
                (11, 1): {'E', '1', 'D', 'G'},
                (11, 2): {'6', 'E', 'G', 'A'},
                (11, 3): {'1', 'D', '6', 'G', 'A'},
                (11, 4): {'B', '4', 'D', '6', 'E', 'A'},
                (11, 11): {'B', '1', 'A'},
                (11, 12): {'6', 'B', 'G'},
                (11, 13): {'B', 'G', 'A'},
                (12, 4): {'8', '3', 'C', '7', '6', 'E'},
                (12, 5): {'8', 'C', '7', '6', 'E'},
                (12, 6): {'E', 'C', '7'},
                (12, 7): {'3', '8', '6', '7'},
                (12, 8): {'6', '1'},
                (12, 9): {'6', 'A'},
                (12, 10): {'3', '1', 'A'},
                (12, 11): {'1', 'A'},
                (13, 0): {'9', '8', 'A', '5'},
                (13, 1): {'8', '1', '3', 'F', 'C', '5'},
                (13, 2): {'3', '9', 'C', '5', 'A'},
                (13, 3): {'1', '3', '9', 'F', '5', 'A'},
                (13, 4): {'8', '3', '9', 'B', 'F', 'C', 'G'},
                (13, 5): {'8', '9', 'B', 'F', 'C'},
                (13, 6): {'B', 'F', 'G', 'C'},
                (13, 8): {'2', '1'},
                (13, 9): {'B', '2', 'A'},
                (13, 14): {'1'},
                (13, 15): {'B', '1', 'C', 'A'},
                (14, 0): {'9', 'A', '6'},
                (14, 1): {'3', 'F', '1'},
                (14, 2): {'3', '9', 'A', '6'},
                (14, 3): {'1', '3', '9', 'F', '6', 'A'},
                (14, 4): {'3', 'B', '9', 'F', 'D', '6'},
                (14, 5): {'9', 'B', 'F', '6'},
                (14, 13): {'B', 'D', 'A'},
                (14, 14): {'4', '1', 'D'},
                (14, 15): {'B', '1', 'D', 'A'},
                (15, 0): {'6', '5', 'E', '7'},
                (15, 1): {'5', 'E', 'C', '7'},
                (15, 2): {'7', 'C', '5', '6', 'E'},
                (15, 4): {'B', 'C', 'D', '7', '6', 'E', 'G'},
                (15, 5): {'B', 'C', '7', '6', 'E'},
                (15, 10): {'4'},
                (15, 11): {'B', '5'},
                (15, 12): {'B', '4', 'C', 'G'},
                (15, 13): {'B', 'C', 'G', 'D'}
            },
            n = 4
        )

        # 1. grouping
        result_row = (eg2.group(by = 'row') == {
            0: candidate.Candidate(
                {
                    (0, 1): {'4'}, 
                    (0, 3): {'2'}
                }, 
                n = 2
            ), 
            1: candidate.Candidate(
                {
                    (1, 0): {'3', '4'}, 
                    (1, 2): {'4', '1'}, 
                    (1, 3): {'1'}
                },
                n = 2
            ),
            2: candidate.Candidate(
                {
                    (2, 0): {'3', '2', '4'}, 
                    (2, 1): {'3', '4', '1'}, 
                    (2, 2): {'2', '1'}, 
                    (2, 3): {'3', '2', '1'}
                },
                n = 2
            ), 
            3: candidate.Candidate(
                {
                    (3, 0): {'3', '2'}, 
                    (3, 1): {'3', '1'}, 
                    (3, 2): {'2', '1'}
                },
                n = 2
            )
        })
        result_col = (eg2.group(by = 'col') == {
            0: candidate.Candidate(
                {
                    (1, 0): {'3', '4'}, 
                    (2, 0): {'3', '2', '4'}, 
                    (3, 0): {'3', '2'}
                },
                n = 2
            ), 
            1: candidate.Candidate(
                {
                    (0, 1): {'4'}, 
                    (2, 1): {'3', '4', '1'}, 
                    (3, 1): {'3', '1'}
                },
                n = 2
            ), 
            2: candidate.Candidate(
                {
                    (1, 2): {'4', '1'}, 
                    (2, 2): {'2', '1'}, 
                    (3, 2): {'2', '1'}
                },
                n = 2
            ), 
            3: candidate.Candidate(
                {
                    (0, 3): {'2'}, 
                    (1, 3): {'1'}, 
                    (2, 3): {'3', '2', '1'}
                },
                n = 2
            )
        })
        result_submatrix2 = (eg2.group(by = 'submatrix') == {
            1: candidate.Candidate(
                {
                    (0, 1): {'4'}, 
                    (1, 0): {'3', '4'}
                },
                n = 2
            ), 
            2: candidate.Candidate(
                {
                    (0, 3): {'2'}, 
                    (1, 2): {'4', '1'}, 
                    (1, 3): {'1'}
                },
                n = 2
            ), 
            3: candidate.Candidate(
                {
                    (2, 0): {'3', '2', '4'}, 
                    (2, 1): {'3', '4', '1'}, 
                    (3, 0): {'3', '2'}, 
                    (3, 1): {'3', '1'}
                },
                n = 2
            ), 
            4: candidate.Candidate(
                {
                    (2, 2): {'2', '1'}, 
                    (2, 3): {'3', '2', '1'}, 
                    (3, 2): {'2', '1'}
                },
                n = 2
            )
        })

        # 2. grouping by submatrix works for n = 3
        result_submatrix3 = (eg3.group(by = 'submatrix') == {
            1: candidate.Candidate({
                (0, 0): {'7', '4', '1', '9', '5'}, 
                (0, 1): {'4', '5'}, 
                (0, 2): {'9', '1', '7'}, 
                (1, 2): {'2'}, 
                (2, 0): {'1', '2', '7'}, 
                (2, 2): {'1', '2', '7'}
            }), 
            2: candidate.Candidate({
                (0, 3): {'8', '6'}, 
                (0, 5): {'8', '3'}, 
                (2, 4): {'3'}
            }), 
            3: candidate.Candidate({
                (0, 6): {'1', '3', '5'}, 
                (0, 7): {'3', '5', '7'}, 
                (0, 8): {'1', '3', '5'}, 
                (1, 6): {'5'}, 
                (2, 7): {'2', '3', '7'}
            }), 
            4: candidate.Candidate({
                (3, 0): {'2', '6'}, 
                (3, 2): {'8', '2', '6'}, 
                (4, 0): {'6', '3'}, 
                (4, 2): {'6', '8', '3'}, 
                (5, 0): {'4', '6', '3'}
            }), 
            5: candidate.Candidate({
                (3, 4): {'8', '6', '5', '7'}, 
                (4, 4): {'8', '6', '5'}, 
                (5, 3): {'8', '6'}, 
                (5, 4): {'8', '6'}, 
                (5, 5): {'9', '8'}
            }), 
            6: candidate.Candidate({
                (3, 6): {'8', '6', '5'}, 
                (3, 7): {'8', '6', '5'}, 
                (4, 6): {'3', '9', '8', '6', '5'}, 
                (4, 7): {'6', '8', '3', '5'}, 
                (5, 8): {'9', '3'}
            }), 
            7: candidate.Candidate({
                (6, 0): {'3', '1', '2', '9', '6', '5'}, 
                (6, 1): {'8', '2', '5'}, 
                (7, 0): {'3', '1', '2', '9', '6'}, 
                (7, 1): {'8', '2'}, 
                (7, 2): {'3', '1', '2', '9', '8', '6'}, 
                (8, 0): {'2', '3', '5', '7'}, 
                (8, 1): {'8', '2', '5'}, 
                (8, 2): {'8', '2', '3', '7'}
            }), 
            8: candidate.Candidate({
                (6, 3): {'8', '2'}, 
                (6, 4): {'8', '3'}, 
                (6, 5): {'8', '3'}, 
                (7, 4): {'4', '8', '3'}
            }), 
            9: candidate.Candidate({
                (6, 7): {'3', '2', '8', '6', '5'}, 
                (6, 8): {'3', '1', '2', '9', '5'}, 
                (7, 6): {'3', '1', '9', '8', '6'}, 
                (7, 7): {'3', '4', '2', '8', '6'}, 
                (7, 8): {'9', '1', '2', '3'}, 
                (8, 6): {'8', '3', '5'}, 
                (8, 7): {'3', '4', '2', '8', '5'}, 
                (8, 8): {'2', '3', '5'}
            })
        })

        # 3. grouping by submatrix works for n = 4
        result_submatrix4 = (eg4.group(by = 'submatrix') == {
            1: candidate.Candidate(
                {
                    (0, 3): {'3', '9', '4', 'D', '5', 'A'}, 
                    (1, 0): {'5', '9', '4', '7', '2', 'E'}, 
                    (1, 1): {'5', 'C', '7', '2', 'E', 'G'}, 
                    (1, 2): {'2', '9', 'B', 'C', '7', '5', 'E', 'G'}, 
                    (1, 3): {'9', '4', '7', '5', 'G'}, 
                    (2, 0): {'8', '9', '4', 'D', '7', '2', 'A'}, 
                    (2, 1): {'8', '3', 'D', '7', '2'}, 
                    (2, 2): {'3', '9', '7', '2', 'A'}, 
                    (2, 3): {'3', '9', '4', 'D', '7', 'A'}, 
                    (3, 0): {'8', '9', '4', '7', '5', 'E'}, 
                    (3, 1): {'8', 'E', '5', '7'}, 
                    (3, 2): {'9', 'B', '7', '5', 'E'}, 
                    (3, 3): {'9', '5', '4', '7'}
                },
                n = 4
            ), 
            2: candidate.Candidate(
                {
                    (0, 4): {'8', '9', 'B', '4', 'C', '5', '2', 'A'}, 
                    (0, 5): {'8', '9', 'B', '4', 'C', '5', '2', 'A'}, 
                    (0, 6): {'B', '4', 'C', '5'}, 
                    (0, 7): {'9', '8', 'B', '2'}, 
                    (1, 4): {'1', '9', 'B', '4', '7', 'C', '5', '6', '2'},
                    (1, 5): {'9', 'B', '4', '7', 'C', '5', '6', '2'}, 
                    (1, 6): {'1', 'B', '4', '7', 'C', '5'}, 
                    (1, 7): {'9', 'B', '7', '6', '2'}, 
                    (2, 4): {'8', '1', '9', '4', 'F', '7', '6', '2', 'A'}, 
                    (2, 5): {'8', '9', '4', 'F', '7', '6', '2', 'A'}, 
                    (2, 6): {'4', 'F', '1', '7'}, 
                    (3, 4): {'8', '9', 'B', '4', 'F', '7', '6', '5'}
                },
                n = 4
            ), 
            3: candidate.Candidate(
                {
                    (0, 8): {'2', '4'}, 
                    (0, 9): {'9', '8', '4', '2'}, 
                    (0, 10): {'9', '2', '4'}, 
                    (0, 11): {'9'}, 
                    (1, 8): {'6', '2', 'E', '4'}, 
                    (1, 9): {'9', '4', '6', '2', 'E'}, 
                    (3, 10): {'9', 'F', '4'}, 
                    (3, 11): {'9', 'F', '7'}
                },
                n = 4
            ), 
            4: candidate.Candidate(
                {
                    (0, 12): {'3', 'B', '9', '4'}, 
                    (1, 15): {'6', 'B', '1'}, 
                    (2, 12): {'3', '9', '4', '6'}, 
                    (2, 13): {'3', 'D'}, 
                    (2, 14): {'1', '9', '4', 'D', '6'}, 
                    (2, 15): {'6', '1', 'D'}, 
                    (3, 12): {'9', 'B', '4', '6'}, 
                    (3, 13): {'B', '5'}
                },
                n = 4
            ), 
            5: candidate.Candidate(
                {
                    (4, 3): {'4', 'F', 'D', '7', '6'}, 
                    (5, 1): {'5', 'G', 'D', '7'}, 
                    (5, 2): {'5', 'G', '7'}, 
                    (5, 3): {'4', '7', 'D', '5', 'G'}, 
                    (6, 0): {'6', '4', 'D', '5'}, 
                    (6, 1): {'F', 'G', 'D', '5'}, 
                    (6, 2): {'6', 'G', '5'}, 
                    (7, 0): {'2', '7'}
                },
                n = 4
            ), 
            6: candidate.Candidate(
                {
                    (4, 4): {'4', 'F', '7', '2', 'E'}, 
                    (4, 5): {'4', 'F', '7', '2', 'E'}, 
                    (4, 6): {'F', 'E', '4', '7'}, 
                    (4, 7): {'2', '7'}, 
                    (5, 4): {'8', '1', '3', '4', '7', '5', 'G'}, 
                    (5, 5): {'8', '4', '5', '7'}, 
                    (5, 6): {'1', '4', '7', '5', 'G'}, 
                    (5, 7): {'3', '8', '7'}, 
                    (6, 4): {'1', '3', '4', 'F', '5', 'E', 'G'}, 
                    (6, 5): {'F', 'E', '4', '5'}, 
                    (7, 4): {'8', 'B', 'F', '7', '2', 'G'}
                },
                n = 4
            ), 
            7: candidate.Candidate(
                {
                    (4, 8): {'F', '4', 'D'}, 
                    (4, 9): {'4', 'A'}, 
                    (4, 10): {'F', '4', 'A'}, 
                    (4, 11): {'F', 'C', 'A'}, 
                    (5, 8): {'4', '1', 'D', 'G'}, 
                    (5, 9): {'9', '4'}, 
                    (7, 10): {'9', 'F', 'G'}, 
                    (7, 11): {'9', 'F'}
                },
                n = 4
            ), 
            8: candidate.Candidate(
                {
                    (5, 15): {'D', 'C'}, 
                    (6, 12): {'3', '6'}, 
                    (6, 13): {'3', 'D'}, 
                    (6, 14): {'6', 'D'}, 
                    (6, 15): {'6', 'E', 'D'}, 
                    (7, 12): {'9', '8'}, 
                    (7, 13): {'8'}, 
                    (7, 14): {'9', '7'}
                },
                n = 4
            ), 
            9: candidate.Candidate(
                {
                    (9, 1): {'1', '5', '3', '7', '2', 'E', 'G'}, 
                    (9, 2): {'2', '3', '9', '7', '6', '5', 'E', 'G', 'A'},
                    (9, 3): {'1', '3', '9', '7', '6', '5', 'G', 'A'}, 
                    (10, 0): {'9', '7', '5', '2', 'E', 'A'}, 
                    (10, 1): {'5', 'E', '2', '7'}, 
                    (10, 2): {'9', '7', '5', '2', 'E', 'A'}, 
                    (10, 3): {'9', '5', 'A', '7'}, 
                    (11, 0): {'6', 'E', 'D', 'A'}, 
                    (11, 1): {'E', '1', 'D', 'G'}, 
                    (11, 2): {'6', 'E', 'G', 'A'}, 
                    (11, 3): {'1', 'D', '6', 'G', 'A'}
                },
                n = 4
            ), 
            10: candidate.Candidate(
                {
                    (8, 4): {'9', 'C', 'D', '5', '6', '2', 'A'}, 
                    (8, 5): {'9', 'C', '5', '6', '2', 'A'}, 
                    (8, 6): {'C', 'D', '5'}, 
                    (8, 7): {'9', '2', '6'}, 
                    (9, 4): {'2', '9', 'B', '7', '6', '5', 'E', 'A'}, 
                    (9, 5): {'2', '9', 'B', '7', '6', '5', 'E', 'A'}, 
                    (9, 6): {'B', 'E', '7', '5'}, 
                    (9, 7): {'9', 'B', '7', '6', '2'}, 
                    (10, 4): {'2', '9', 'B', 'C', '7', '5', 'E', 'A'}, 
                    (10, 6): {'B', 'C', '7', '5', 'E'}, 
                    (11, 4): {'B', '4', 'D', '6', 'E', 'A'}
                },
                n = 4
            ), 
            11: candidate.Candidate(
                {
                    (8, 8): {'2', 'G'}, 
                    (8, 9): {'9', '2', 'A'}, 
                    (8, 10): {'9', '2', 'G', 'A'}, 
                    (8, 11): {'9', 'A'}, 
                    (9, 8): {'1', 'F', '2', 'E', 'G'}, 
                    (9, 9): {'9', 'B', '2', 'E', 'A'}, 
                    (9, 10): {'1', '9', 'F', '2', 'G', 'A'}, 
                    (11, 11): {'B', '1', 'A'}
                },
                n = 4
            ),
            12: candidate.Candidate(
                {
                    (9, 14): {'6', '5'}, 
                    (9, 15): {'6', 'B', 'F', 'A'}, 
                    (10, 12): {'8', 'B', 'C'}, 
                    (10, 13): {'8', 'B', 'C', '5', 'A'}, 
                    (10, 14): {'5'}, 
                    (10, 15): {'B', 'F', 'C', 'A'}, 
                    (11, 12): {'6', 'B', 'G'}, 
                    (11, 13): {'B', 'G', 'A'}
                },
                n = 4
            ), 
            13: candidate.Candidate(
                {
                    (13, 0): {'9', '8', 'A', '5'}, 
                    (13, 1): {'8', '1', '3', 'F', 'C', '5'}, 
                    (13, 2): {'3', '9', 'C', '5', 'A'}, 
                    (13, 3): {'1', '3', '9', 'F', '5', 'A'}, 
                    (14, 0): {'9', 'A', '6'}, 
                    (14, 1): {'3', 'F', '1'}, 
                    (14, 2): {'3', '9', 'A', '6'}, 
                    (14, 3): {'1', '3', '9', 'F', '6', 'A'}, 
                    (15, 0): {'6', '5', 'E', '7'}, 
                    (15, 1): {'5', 'E', 'C', '7'}, 
                    (15, 2): {'7', 'C', '5', '6', 'E'}
                },
                n = 4
            ),
            14: candidate.Candidate(
                {
                    (12, 4): {'8', '3', 'C', '7', '6', 'E'}, 
                    (12, 5): {'8', 'C', '7', '6', 'E'}, 
                    (12, 6): {'E', 'C', '7'}, 
                    (12, 7): {'3', '8', '6', '7'}, 
                    (13, 4): {'8', '3', '9', 'B', 'F', 'C', 'G'}, 
                    (13, 5): {'8', '9', 'B', 'F', 'C'}, 
                    (13, 6): {'B', 'F', 'G', 'C'}, 
                    (14, 4): {'3', 'B', '9', 'F', 'D', '6'}, 
                    (14, 5): {'9', 'B', 'F', '6'}, 
                    (15, 4): {'B', 'C', 'D', '7', '6', 'E', 'G'}, 
                    (15, 5): {'B', 'C', '7', '6', 'E'}
                },
                n = 4
            ), 
            15: candidate.Candidate(
                {
                    (12, 8): {'6', '1'}, 
                    (12, 9): {'6', 'A'}, 
                    (12, 10): {'3', '1', 'A'}, 
                    (12, 11): {'1', 'A'}, 
                    (13, 8): {'2', '1'}, 
                    (13, 9): {'B', '2', 'A'}, 
                    (15, 10): {'4'}, 
                    (15, 11): {'B', '5'}
                },
                n = 4
            ), 
            16: candidate.Candidate(
                {
                    (13, 14): {'1'}, 
                    (13, 15): {'B', '1', 'C', 'A'}, 
                    (14, 13): {'B', 'D', 'A'}, 
                    (14, 14): {'4', '1', 'D'}, 
                    (14, 15): {'B', '1', 'D', 'A'}, 
                    (15, 12): {'B', '4', 'C', 'G'}, 
                    (15, 13): {'B', 'C', 'G', 'D'}
                },
                n = 4
            )
        })

        # 4. candidates are not available in a certain group
        eg2.pop((0, 1))
        eg2.pop((1, 0))
        result_nosub_1 = (eg2.group(by = 'submatrix') == {
            1: candidate.Candidate({}, n = 2), 
            2: candidate.Candidate(
                {
                    (0, 3): {'2'}, 
                    (1, 2): {'4', '1'}, 
                    (1, 3): {'1'}
                },
                n = 2
            ),
            3: candidate.Candidate(
                {
                    (2, 0): {'3', '2', '4'}, 
                    (2, 1): {'3', '4', '1'}, 
                    (3, 0): {'3', '2'}, 
                    (3, 1): {'3', '1'}
                },
                n = 2
            ), 
            4: candidate.Candidate(
                {
                    (2, 2): {'2', '1'}, 
                    (2, 3): {'3', '2', '1'}, 
                    (3, 2): {'2', '1'}
                },
                n = 2
            )
        })

        result = {
            'row': result_row, 
            'col': result_col, 
            'submatrix2': result_submatrix2,
            'submatrix3': result_submatrix3,
            'submatrix4': result_submatrix4,
            'nosub_1': result_nosub_1
        }
        expected_result = {
            'row': True, 
            'col': True, 
            'submatrix2': True,
            'submatrix3': True,
            'submatrix4': True,
            'nosub_1': True
        }
        self.assertEqual(result, expected_result)


    def test_group_error(self):
        '''
        Test if .group(by) raises ValueError if by is neither 'submatrix',
        'row', nor 'col'.
        '''

        eg = candidate.Candidate(
            {
                (0, 1): {'4'}, 
                (0, 3): {'2'}, 
                (1, 0): {'4', '3'}, 
                (1, 2): {'4', '1'}, 
                (1, 3): {'1'}, 
                (2, 0): {'2', '4', '3'}, 
                (2, 1): {'4', '3', '1'}, 
                (2, 2): {'2', '1'}, 
                (2, 3): {'2', '3', '1'}, 
                (3, 0): {'2', '3'}, 
                (3, 1): {'3', '1'}, 
                (3, 2): {'2', '1'}
            }, 
            n = 2
        )
        with self.assertRaises(ValueError): eg.group(by = 'subarray')


    def test_item_family(self):
        '''
        Test .__getitem__() and .__setitem__() to see if:
        1. item subscription is supported
        2. item assignment is supported
        3. item mutation is supported
        '''

        eg = candidate.Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        
        # Item subscription
        result_select = (eg[(0, 1)] == {1, 2, 4})
        expected_result_select = True

        # Item assignment
        eg[(0, 3)] = {7, 8}
        expected_assign = candidate.Candidate({
            (0, 1): {1, 2, 4},
            (0, 2): {6, 9},
            (0, 3): {7, 8}
        })
        result_assign = (eg == expected_assign)
        expected_result_assign = True

        # Mutation of an existing entry
        eg[(0, 2)] = {9}
        expected_mutate = candidate.Candidate({
            (0, 1): {1, 2, 4},
            (0, 2): {9},
            (0, 3): {7, 8},
        })
        result_mutate = (eg == expected_mutate)
        expected_result_mutate = True

        result = {
            'getitem_subscript': result_select,
            'setitem_assign': result_assign,
            'setitem_mutate': result_mutate
        }
        expected_result = {
            'getitem_subscript': expected_result_select,
            'setitem_assign': expected_result_assign,
            'setitem_mutate': expected_result_mutate
        }
        self.assertEqual(result, expected_result)


# END: testing Candidate #################################################

# START: testing Sudoku ##################################################


class TestSudoku(unittest.TestCase):

    def test_init(self):
        '''
        Test .__init__() to see if Sudoku is initialized:
        1. for list of lists of strings and integers
        2. when elements is a set of integers
        3. when elements is a set of both integers and strings
        4. when elements is None
        '''

        eg = [
            ['1', '.', '3', '.'],
            ['.', '2', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '4']
        ]
        q_small = sudoku.Sudoku(eg, elements = {'1', '2', '3', '4'})

        # 1. list of lists of strings and integers
        eg1 = [
            [  1, '.',   3, '.'],
            ['.',   2, '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.',   4]
        ]
        q_small1 = sudoku.Sudoku(eg1, elements = {'1', '2', '3', '4'})
        result_init1 = (q_small == q_small1)

        # 2. elements is a set of integers
        q_small2 = sudoku.Sudoku(eg, elements = {1, 2, 3, 4})
        result_init2 = (q_small == q_small2)

        # 3. elements is a set of both integers and strings
        q_small3 = sudoku.Sudoku(eg, elements = {1, '2', '3', 4})
        result_init3 = (q_small == q_small3)

        # 4. elements is None
        # 4.1. array contains only one type: str
        q_small4_1 = sudoku.Sudoku(eg)
        result_init4_1 = (q_small == q_small4_1)

        # 4.2. array contains more than one type: str and int
        q_small4_2 = sudoku.Sudoku(eg1)
        result_init4_2 = (q_small == q_small4_2) 

        result = {
            'init1': result_init1, 
            'init2': result_init2, 
            'init3': result_init3,
            'init4_1': result_init4_1,
            'init4_2': result_init4_2
        }
        expected_result = {            
            'init1': True, 
            'init2': True, 
            'init3': True,
            'init4_1': True,
            'init4_2': True
        }

        self.assertEqual(result, expected_result)


    def test_init_elements_error(self):
        '''
        Test .__init__() to see if it returns ValueError whenever
        self.elements = None, and self.array does not contain all of the 
        attempted elements at least once.
        '''

        with self.assertRaises(ValueError): sudoku.to_sudoku(questions.q4)


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


    def test_solve_logically(self):
        '''
        Test .solve_logically() to see if Sudoku question that requires:
        1. only .solve_globally() is solved.
        2. only .solve_locally() is solved.
        3. every reasoning except .solve_by_pairs() is solved.
        4. every reasoning including .solve_by_pairs() except the line 
           "self.itemsets(candidates_global)" is solved.
        5. not only every reasoning, but also more than one iteration of
           while loop in .solve_logically() is solved.
        And also, check if:
        6. (2 ** 2)-by-(2 ** 2) sudoku is solved.
        7. (4 ** 2)-by-(4 ** 2) sudoku is solved.
        8. (5 ** 2)-by-(5 ** 2) sudoku is solved.
        '''

        # 1. .solve_globally() is sufficient
        q1 = sudoku.to_sudoku(questions.q1)
        q1.solve_logically()
        result1 = (str(q1) == questions.a1, q1.is_valid_answer())

        # 2. .solve_locally() is sufficient
        # In fact, .solve_globally() doesn't do anything
        q2 = sudoku.to_sudoku(questions.q2)
        q2.solve_logically()
        result2 = (str(q2) == questions.a2, q2.is_valid_answer())

        # 3. .solve_by_pairs() not required
        q3 = sudoku.to_sudoku(questions.q3)
        q3.solve_logically()
        result3 = (str(q3) == questions.a3, q3.is_valid_answer())

        # 4. .solve_by_pairs() required, but not the line
        # "self.itemsets(candidates_global)" in .solve_by_pairs()
        q4 = sudoku.to_sudoku(
            questions.q4,
            elements = set([str(i) for i in range(1, 10)])
        )
        q4.solve_logically()
        result4 = (str(q4) == questions.a4, q4.is_valid_answer())

        # 5. more than one iteration in while loop required
        q5 = sudoku.to_sudoku(questions.q5)
        q5.solve_logically()
        result5 = (str(q5) == questions.a5, q5.is_valid_answer())

        # 6. (2 ** 2)-by-(2 ** 2) sudoku
        q6 = sudoku.to_sudoku(questions.q6, elements = {1, 2, 3, 4})
        q6.solve_logically()
        result6 = (str(q6) == questions.a6, q6.is_valid_answer())

        # 7. (4 ** 2)-by-(4 ** 2) sudoku, or hexadoku
        q7 = sudoku.to_sudoku(
            questions.q7,
            elements = set([str(i) for i in range(1, 10)])\
                .union({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
        )
        q7.solve_logically()
        result7 = (str(q7) == questions.a7, q7.is_valid_answer())

        # 8. (5 ** 2)-by-(5 ** 2) sudoku, or alphadoku
        q8 = sudoku.to_sudoku(
            questions.q8,
            elements = {
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y'
            }
        )
        q8.solve_logically()
        result8 = (str(q8) == questions.a8, q8.is_valid_answer())

        result = {
            'test1': result1,
            'test2': result2,
            'test3': result3,
            'test4': result4,
            'test5': result5,
            'test6': result6,
            'test7': result7,
            'test8': result8
        }
        expected_result = {
            'test1': (True, True),
            'test2': (True, True),
            'test3': (True, True),
            'test4': (True, True),
            'test5': (True, True),
            'test6': (True, True),
            'test7': (True, True),
            'test8': (True, True)
        }
        self.assertEqual(result, expected_result)


    def test_solve_forcefully(self):
        '''
        Test .solve_forcefully() to see if a brute force works.
        '''

        q_sta = sudoku.to_sudoku(questions.q_sta410_testing)
        q_sta.solve_logically()
        q_sta.solve_forcefully(quietly = True)
        result = (
            str(q_sta) in [
                questions.a_sta410_4, 
                questions.a_sta410_5,
                questions.a_sta410_6
            ],
            q_sta.is_valid_answer()
        )
        expected_result = (True, True)
        self.assertEqual(result, expected_result)


# END: testing Sudoku ####################################################


if __name__ == '__main__':
    unittest.main(exit = False)
