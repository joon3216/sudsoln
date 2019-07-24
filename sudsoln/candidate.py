
class Candidate():
    '''Sudoku puzzle candidate collection.'''

    def __init__(self, candidates, n = 3):
        '''(Candidate, {(int, int): set of objects}[, int]) -> None

        Precondition: 
        1. ints in "(int, int)" are from 0 to n ** 2 - 1 
        inclusive, where n is a Sudoku class attribute or a user-defined
        integer.
        2. objects in "set of values" are elements of one_to_n_sq, one of 
        Sudoku class attributes.

        Initialize Candidate object.
        
        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(eg)
        '''

        self.show = candidates
        self.n = n


    def __dict__(self):
        '''(Candidate) -> {(int, int): set of objects}

        Return the dict representation of Candidate.

        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(eg)
        >>> dict(eg)
        {(0, 1): {1, 2, 4}, (0, 2): {9, 6}}
        '''

        return self.show


    def __eq__(self, other):
        '''(Candidate, Candidate) -> bool

        Return True iff keys and values of each key matches between
        self and other.

        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg2 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg3 = Candidate({(0, 1): {1, 2, 7}, (0, 3): {6, 8}})
        >>> eg1 == eg2
        True
        >>> eg1 == eg3
        False
        '''

        return self.show == other.show and self.n == other.n


    def __getitem__(self, key):
        '''(Candidate, (int, int)) -> set of objects

        Return the value of self at key.

        >>> eg = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg[(0, 1)]
        {1, 2, 4}
        '''

        return self.show[key]


    def __repr__(self):
        '''(Candidate) -> str

        Return the Candidate representation of self.
        '''

        return 'Candidate(\n{0},\nn = {1}\n)'.format(self.show, self.n)


    def __setitem__(self, key, value):
        '''(Candidate, (int, int), set of objects) -> None

        Assign value to key that either already exists in self, or 
        initialize key with value if key doesn't already
        exist.

        >>> eg = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg[(1, 2)] = {7}
        >>> eg == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}, (1, 2): {7}}
        ... )
        ...
        True
        >>> eg[(0, 1)] = {1}
        >>> eg == Candidate({(0, 1): {1}, (0, 2): {6, 9}, (1, 2): {7}})
        True
        '''

        self.show[key] = value


    def copy(self):
        '''(Candidate) -> Candidate

        Return the deep copy of self.

        >>> eg = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg_copy = eg.copy()
        >>> id(eg) != id(eg_copy)
        True
        >>> id(eg[(0, 2)]) != id(eg_copy[(0, 2)])
        True
        '''

        copied = {}
        for k, v in self.items():
            copied[k] = v.copy()
        return Candidate(copied.copy(), n = self.n)

    
    def group(self, by):
        '''(Candidate, str) -> {int: Candidate}

        Precondition: by == 'submatrix' or 'row' or 'col'

        Return the candidate values grouped by 'by', which is either
        'submatrix', 'row', or 'col'.

        >>> import sudsoln as ss
        >>> import sudsoln.questions as sq
        >>> q6 = ss.to_sudoku(sq.q6, elements = {1, 2, 3, 4})
        >>> q6 = q6.candidates()
        >>> q6.group(by = 'submatrix') == {
        ...     1: Candidate(
        ...         {
        ...             (0, 0): {'1'}, 
        ...             (1, 0): {'4', '1'}, 
        ...             (1, 1): {'4', '2', '1'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (0, 2): {'2'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (1, 3): {'3', '2', '1'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (2, 0): {'3', '4'}, 
        ...             (2, 1): {'4'}, 
        ...             (3, 1): {'4', '1'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     4: Candidate(
        ...         {
        ...             (2, 3): {'3', '2'}, 
        ...             (3, 2): {'3', '4'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         n = 2
        ...     )
        ... }
        ...
        True
        >>> q6.group(by = 'row') == {
        ...     0: Candidate(
        ...         {
        ...             (0, 0): {'1'}, 
        ...             (0, 2): {'2'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     1: Candidate(
        ...         {
        ...             (1, 0): {'4', '1'}, 
        ...             (1, 1): {'4', '2', '1'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (1, 3): {'3', '2', '1'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (2, 0): {'3', '4'}, 
        ...             (2, 1): {'4'}, 
        ...             (2, 3): {'3', '2'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (3, 1): {'4', '1'}, 
        ...             (3, 2): {'3', '4'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         n = 2
        ...     )
        ... }
        ...
        True
        >>> q6.group(by = 'col') == {
        ...     0: Candidate(
        ...         {
        ...             (0, 0): {'1'}, 
        ...             (1, 0): {'4', '1'}, 
        ...             (2, 0): {'3', '4'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     1: Candidate(
        ...         {
        ...             (1, 1): {'4', '2', '1'}, 
        ...             (2, 1): {'4'}, 
        ...             (3, 1): {'4', '1'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (0, 2): {'2'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (3, 2): {'3', '4'}
        ...         },
        ...         n = 2
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (1, 3): {'3', '2', '1'}, 
        ...             (2, 3): {'3', '2'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         n = 2
        ...     )
        ... }
        ...
        True
        '''

        if by not in ['submatrix', 'row', 'col']:
            raise ValueError(
                "by must be either 'submatrix', 'row', or 'col', not " +\
                "'" + str(by) + "'."
            )
        result = {}
        n = self.n
        if by == 'submatrix':
            for g in range(1, n ** 2 + 1):
                result[g] = Candidate({}, n = n)
            number = 0
            for i in range(n, n ** 2 + 1, n):
                for j in range(n, n ** 2 + 1, n):
                    number += 1
                    for k, v in self.items():
                        if i - n <= k[0] < i and j - n <= k[1] < j:
                            result[number].update({k: v})
            return result
        for g in range(n ** 2):
            result[g] = Candidate({}, n = n)
            for k, v in self.items():
                if (by == 'row' and k[0] == g) or\
                    (by == 'col' and k[1] == g):
                    result[g].update({k: v})
        return result

    
    def items(self):
        '''(Candidate) -> dict_items of (int, int), {object}

        Return dict_items of self.

        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg1.items()
        dict_items([((0, 1), {1, 2, 4}), ((0, 2), {9, 6})])
        '''

        return self.show.items()

    
    def keys(self):
        '''(Candidate) -> dict_keys of (int, int)

        Return dict_keys of self.

        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg1.keys()
        dict_keys([(0, 1), (0, 2)])
        '''

        return self.show.keys()


    def pop(self, key):
        '''(Candidate) -> None

        Pop out key and the respective value from self.

        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg1 == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {9, 6}},
        ...     n = 3
        ... )
        ...
        True
        >>> eg1.pop((0, 1))
        >>> eg1 == Candidate({(0, 2): {9, 6}}, n = 3)
        True
        '''

        self.show.pop(key)

    
    def refine(self, entries_to_mutate, appearances):
        '''(Candidate, Candidate, {int: [[int, int], {(int, int)}]}) 
            -> None

        Update self and entries_to_mutate so that any unique candidate 
        number and the respective entry according to appearances is added
        to entries_to_mutate, and any candidate number that should be
        eliminated from some values of self due to the uniqueness of 
        candidate number in a certain row or column in appearances is
        eliminated.

        >>> candids_old = Candidate({
        ...     (0, 0): {'4', '9', '7', '5', '1'}, 
        ...     (0, 1): {'5', '4'}, 
        ...     (0, 2): {'9', '1', '7'}, 
        ...     (0, 3): {'8', '6'}, 
        ...     (0, 5): {'3', '8'}, 
        ...     (0, 6): {'1', '3', '5'}, 
        ...     (0, 7): {'5', '7', '3'}, 
        ...     (0, 8): {'1', '3', '5'}, 
        ...     (1, 2): {'2'}, 
        ...     (1, 6): {'5'}, 
        ...     (2, 0): {'2', '1', '7'}, 
        ...     (2, 2): {'2', '1', '7'}, 
        ...     (2, 4): {'3'}, 
        ...     (2, 7): {'2', '7', '3'}, 
        ...     (3, 0): {'2', '6'}, 
        ...     (3, 2): {'2', '8', '6'}, 
        ...     (3, 4): {'5', '7', '8', '6'}, 
        ...     (3, 6): {'5', '8', '6'}, 
        ...     (3, 7): {'5', '8', '6'}, 
        ...     (4, 0): {'3', '6'}, 
        ...     (4, 2): {'3', '8', '6'}, 
        ...     (4, 4): {'5', '8', '6'}, 
        ...     (4, 6): {'9', '8', '5', '3', '6'}, 
        ...     (4, 7): {'5', '3', '8', '6'}, 
        ...     (5, 0): {'3', '6', '4'}, 
        ...     (5, 3): {'8', '6'}, 
        ...     (5, 4): {'8', '6'}, 
        ...     (5, 5): {'9', '8'}, 
        ...     (5, 8): {'9', '3'}, 
        ...     (6, 0): {'9', '1', '5', '3', '6', '2'}, 
        ...     (6, 1): {'2', '8', '5'}, 
        ...     (6, 3): {'2', '8'}, 
        ...     (6, 4): {'3', '8'}, 
        ...     (6, 5): {'3', '8'}, 
        ...     (6, 7): {'8', '5', '3', '6', '2'}, 
        ...     (6, 8): {'9', '2', '5', '3', '1'}, 
        ...     (7, 0): {'9', '2', '3', '6', '1'}, 
        ...     (7, 1): {'2', '8'}, 
        ...     (7, 2): {'9', '1', '8', '3', '6', '2'}, 
        ...     (7, 4): {'3', '8', '4'}, 
        ...     (7, 6): {'9', '8', '3', '6', '1'}, 
        ...     (7, 7): {'4', '8', '3', '6', '2'}, 
        ...     (7, 8): {'9', '1', '3', '2'}, 
        ...     (8, 0): {'5', '7', '3', '2'}, 
        ...     (8, 1): {'2', '8', '5'}, 
        ...     (8, 2): {'2', '7', '8', '3'}, 
        ...     (8, 6): {'5', '3', '8'}, 
        ...     (8, 7): {'4', '8', '5', '3', '2'}, 
        ...     (8, 8): {'2', '3', '5'}
        ... })
        ...
        >>> candids = candids_old.copy()
        >>> candids == candids_old
        True
        >>> entries_to_mutate = Candidate({})
        >>>
        >>> # Case 1: only candids changes
        >>> appearances1 = {
        ...     '4': [[1, 2], {(0, 1), (0, 0)}], 
        ...     '9': [[1, 2], {(0, 0), (0, 2)}], 
        ...     '5': [[1, 2], {(0, 1), (0, 0)}]
        ... }
        >>> candids.refine(entries_to_mutate, appearances1)
        >>> entries_to_mutate == Candidate({})
        True
        >>> candids == candids_old
        False
        >>> candids == Candidate({
        ...     (0, 0): {'5', '1', '9', '4', '7'}, 
        ...     (0, 1): {'5', '4'}, 
        ...     (0, 2): {'1', '9', '7'}, 
        ...     (0, 3): {'8', '6'}, 
        ...     (0, 5): {'8', '3'}, 
        ...     (0, 6): {'1', '3'}, # '5' eliminated
        ...     (0, 7): {'3', '7'}, # '5' eliminated
        ...     (0, 8): {'1', '3'}, # '5' eliminated
        ...     (1, 2): {'2'}, 
        ...     (1, 6): {'5'}, 
        ...     (2, 0): {'1', '2', '7'}, 
        ...     (2, 2): {'1', '2', '7'}, 
        ...     (2, 4): {'3'}, 
        ...     (2, 7): {'2', '3', '7'}, 
        ...     (3, 0): {'2', '6'}, 
        ...     (3, 2): {'8', '2', '6'}, 
        ...     (3, 4): {'5', '8', '6', '7'}, 
        ...     (3, 6): {'5', '8', '6'}, 
        ...     (3, 7): {'5', '8', '6'}, 
        ...     (4, 0): {'3', '6'}, 
        ...     (4, 2): {'8', '3', '6'}, 
        ...     (4, 4): {'5', '8', '6'}, 
        ...     (4, 6): {'5', '6', '9', '8', '3'}, 
        ...     (4, 7): {'5', '8', '3', '6'}, 
        ...     (5, 0): {'4', '3', '6'}, 
        ...     (5, 3): {'8', '6'}, 
        ...     (5, 4): {'8', '6'}, 
        ...     (5, 5): {'9', '8'}, 
        ...     (5, 8): {'9', '3'}, 
        ...     (6, 0): {'5', '6', '1', '9', '2', '3'}, 
        ...     (6, 1): {'5', '8', '2'}, 
        ...     (6, 3): {'8', '2'}, 
        ...     (6, 4): {'8', '3'}, 
        ...     (6, 5): {'8', '3'}, 
        ...     (6, 7): {'5', '6', '8', '2', '3'}, 
        ...     (6, 8): {'5', '1', '9', '2', '3'}, 
        ...     (7, 0): {'6', '1', '9', '2', '3'}, 
        ...     (7, 1): {'8', '2'}, 
        ...     (7, 2): {'2', '6', '1', '9', '8', '3'}, 
        ...     (7, 4): {'8', '3', '4'}, 
        ...     (7, 6): {'6', '1', '9', '8', '3'}, 
        ...     (7, 7): {'6', '8', '2', '3', '4'}, 
        ...     (7, 8): {'1', '9', '2', '3'}, 
        ...     (8, 0): {'5', '2', '3', '7'}, 
        ...     (8, 1): {'5', '8', '2'}, 
        ...     (8, 2): {'8', '2', '3', '7'}, 
        ...     (8, 6): {'5', '8', '3'}, 
        ...     (8, 7): {'5', '8', '2', '3', '4'}, 
        ...     (8, 8): {'5', '2', '3'}
        ... })
        ...
        True
        >>> 
        >>> # Case 2: only entries_to_mutate changes
        >>> candids_old = candids.copy()
        >>> appearances2 = {
        ...     '8': [[1, 2], {(0, 3), (0, 5)}], 
        ...     '6': [[1, 1], {(0, 3)}]
        ... }
        >>> candids.refine(entries_to_mutate, appearances2)
        >>> entries_to_mutate == Candidate({})
        False
        >>> entries_to_mutate == Candidate({(0, 3): {'6'}})
        True
        >>> candids == candids_old 
        True
        >>>
        >>> # Case 3: both candids and entries_to_mutate change
        >>> appearances3 = {
        ...     '1': [[1, 2], {(0, 6), (0, 8)}], 
        ...     '2': [[1, 1], {(2, 7)}], 
        ...     '7': [[2, 1], {(2, 7), (0, 7)}]
        ... }
        ...
        >>> candids.refine(entries_to_mutate, appearances3)
        >>> entries_to_mutate == Candidate({})
        False
        >>> entries_to_mutate == Candidate(
        ...     {(0, 3): {'6'}, (2, 7): {'2'}}
        ... )
        ...
        True
        >>> candids == candids_old
        False
        >>> candids == Candidate({
        ...     (0, 0): {'5', '9', '4', '7'}, # '1' eliminated
        ...     (0, 1): {'5', '4'}, 
        ...     (0, 2): {'9', '7'},           # '1' eliminated
        ...     (0, 3): {'8', '6'}, 
        ...     (0, 5): {'8', '3'}, 
        ...     (0, 6): {'1', '3'}, 
        ...     (0, 7): {'3', '7'}, 
        ...     (0, 8): {'1', '3'}, 
        ...     (1, 2): {'2'}, 
        ...     (1, 6): {'5'}, 
        ...     (2, 0): {'1', '2', '7'}, 
        ...     (2, 2): {'1', '2', '7'}, 
        ...     (2, 4): {'3'}, 
        ...     (2, 7): {'2', '3', '7'}, 
        ...     (3, 0): {'2', '6'}, 
        ...     (3, 2): {'8', '2', '6'}, 
        ...     (3, 4): {'5', '8', '6', '7'}, 
        ...     (3, 6): {'5', '8', '6'}, 
        ...     (3, 7): {'5', '8', '6'}, 
        ...     (4, 0): {'3', '6'}, 
        ...     (4, 2): {'8', '3', '6'}, 
        ...     (4, 4): {'5', '8', '6'}, 
        ...     (4, 6): {'5', '6', '9', '8', '3'}, 
        ...     (4, 7): {'5', '8', '3', '6'}, 
        ...     (5, 0): {'4', '3', '6'}, 
        ...     (5, 3): {'8', '6'}, 
        ...     (5, 4): {'8', '6'}, 
        ...     (5, 5): {'9', '8'}, 
        ...     (5, 8): {'9', '3'}, 
        ...     (6, 0): {'5', '6', '1', '9', '2', '3'}, 
        ...     (6, 1): {'5', '8', '2'}, 
        ...     (6, 3): {'8', '2'}, 
        ...     (6, 4): {'8', '3'}, 
        ...     (6, 5): {'8', '3'}, 
        ...     (6, 7): {'5', '6', '8', '2', '3'}, 
        ...     (6, 8): {'5', '1', '9', '2', '3'}, 
        ...     (7, 0): {'6', '1', '9', '2', '3'}, 
        ...     (7, 1): {'8', '2'}, 
        ...     (7, 2): {'2', '6', '1', '9', '8', '3'}, 
        ...     (7, 4): {'8', '3', '4'}, 
        ...     (7, 6): {'6', '1', '9', '8', '3'}, 
        ...     (7, 7): {'6', '8', '2', '3', '4'}, 
        ...     (7, 8): {'1', '9', '2', '3'}, 
        ...     (8, 0): {'5', '2', '3', '7'}, 
        ...     (8, 1): {'5', '8', '2'}, 
        ...     (8, 2): {'8', '2', '3', '7'}, 
        ...     (8, 6): {'5', '8', '3'}, 
        ...     (8, 7): {'5', '8', '2', '3', '4'}, 
        ...     (8, 8): {'5', '2', '3'}
        ... })
        ...
        True
        '''

        for k3, v3 in appearances.items():
            if v3[0] == [1, 1]: # only candid value in the subm
                entries_to_mutate[list(v3[1])[0]] = {k3}
            elif v3[0][0] == 1: # eliminate the same candid in rows
                cols_exception = []
                for v3_item1 in list(v3[1]):
                    cols_exception.append(v3_item1[1])
                for k_g1, v_g1 in self.items():
                    if k_g1[0] == list(v3[1])[0][0] and\
                        k_g1[1] not in cols_exception and k3 in v_g1:
                        v_g1.remove(k3)
            elif v3[0][1] == 1: # eliminate the same candid in cols
                rows_exception = []
                for v3_item2 in list(v3[1]):
                    rows_exception.append(v3_item2[0])
                for k_g2, v_g2 in self.items():
                    if k_g2[1] == list(v3[1])[0][1] and\
                        k_g2[0] not in rows_exception and k3 in v_g2:
                        v_g2.remove(k3)


    def update(self, other):
        '''(Candidate, Candidate or {(int, int): set of objects}) -> None

        Update self using other.

        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg1.update(Candidate({(1, 2): {1, 7}}))
        >>> eg1 == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}, (1, 2): {1, 7}}
        ... )
        ...
        True
        >>> eg1.update(Candidate({(0, 1): {1}}))
        >>> eg1 == Candidate(
        ...     {(0, 1): {1}, (0, 2): {6, 9}, (1, 2): {1, 7}}
        ... )
        ...
        True
        >>> eg1.update({(0, 0): {3}, (1, 2): {7}})
        >>> eg1 == Candidate(
        ...     {(0, 0): {3}, (0, 1): {1}, (0, 2): {6, 9}, (1, 2): {7}}
        ... )
        ...
        True
        '''

        if type(other) == dict:
            self.show.update(other)
        elif type(other) == Candidate:
            if self.n != other.n:
                raise ValueError('self.n != other.n')
            self.show.update(other.show)


    def values(self):
        '''(Candidate) -> dict_values of {objects}

        Return dict_values of self.
            
        >>> eg1 = Candidate({(0, 1): {1, 2, 4}, (0, 2): {6, 9}})
        >>> eg1.values()
        dict_values([{1, 2, 4}, {9, 6}])
        '''

        return self.show.values()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
