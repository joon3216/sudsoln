
import unittest
import candidate



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
            'copy': result_copy, 'items': result_items, 
            'keys': result_keys, 'pop': result_pop,
            'update': result_update
        }
        expected_result = {
            'copy': expected_result_copy, 'items': expected_result_items, 
            'keys': expected_result_keys, 'pop': expected_result_pop,
            'update': expected_result_update           
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



if __name__ == '__main__':
    unittest.main(exit = False)