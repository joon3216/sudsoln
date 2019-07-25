
import sudsoln.appearance as appearance
import sudsoln.union as union


class Candidate():
    '''Sudoku puzzle candidate collection.'''

    def __init__(self, candidates, elements = None):
        '''(Candidate, {(int, int): set of objects}) -> None

        Precondition: 
        1. ints in "(int, int)" are from 0 to n ** 2 - 1 
        inclusive, where n is a Sudoku class attribute.
        2. objects in "set of objects" are elements of self.elements, 
        one of Sudoku class attributes.

        Initialize Candidate object.
        
        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(
        ...     eg, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg.n
        3
        '''

        assert elements != None, \
            'elements of Candidate must be specified'
        elements = set(map(lambda x: str(x), list(elements)))
        n = int(len(elements) ** .5)

        if candidates != {}:
            for k, v in candidates.items():
                candidates[k] = set(map(lambda x: str(x), list(v)))

        self.show = candidates
        self.n = n
        self.elements = elements


    def __dict__(self):
        '''(Candidate) -> {(int, int): set of objects}

        Return the dict representation of Candidate.

        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(
        ...     eg, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> dict(eg) == {(0, 1): {'1', '2', '4'}, (0, 2): {'9', '6'}}
        True
        '''

        return self.show


    def __eq__(self, other):
        '''(Candidate, Candidate) -> bool

        Return True iff keys and values of each key matches between
        self and other.

        >>> eg1 = Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg2 = Candidate(
        ...     {(0, 1): {'1', '2', '4'}, (0, 2): {'9', '6'}}, 
        ...     elements = set([i for i in range(1, 10)])
        ... )
        ...
        >>> eg3 = Candidate(
        ...     {(0, 1): {1, 2, 7}, (0, 3): {6, 8}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg1 == eg2
        True
        >>> eg1 == eg3
        False
        '''

        return self.show == other.show and\
            self.n == other.n and self.elements == other.elements


    def __getitem__(self, key):
        '''(Candidate, (int, int)) -> set of objects

        Return the value of self at key.

        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(
        ...     eg, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg[(0, 1)] == {'1', '2', '4'}
        True
        '''

        return self.show[key]


    def __repr__(self):
        '''(Candidate) -> str

        Return the Candidate representation of self.
        '''

        return 'Candidate(\n{0},\nelements = {1}\n)\n(n: {2})'.format(
            self.show, self.elements, self.n
        )


    def __setitem__(self, key, value):
        '''(Candidate, (int, int), set of objects) -> None

        Assign value to key that either already exists in self, or 
        initialize key with value if key doesn't already
        exist.

        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(
        ...     eg, 
        ...     elements = set([i for i in range(1, 10)])
        ... )
        ...
        >>> eg[(1, 2)] = {7}
        >>> eg == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}, (1, 2): {7}},
        ...     elements = set([i for i in range(1, 10)])
        ... )
        ...
        True
        >>> eg[(0, 1)] = {1}
        >>> eg == Candidate(
        ...     {(0, 1): {1}, (0, 2): {6, 9}, (1, 2): {7}},
        ...     elements = set([i for i in range(1, 10)])
        ... )
        ...
        True
        '''

        value = set(map(lambda x: str(x), list(value)))
        self.show[key] = value


    def appearances(self, names):
        '''(Candidate, [str, str]) -> Appearance

        Define union1 and union2 as the aggregated unions of self with
        name in names. Count the number of the same elements in union1 and 
        union2 respectively, record them into the very first element 
        (a list of two ints) of the resulting dictionary's value list, 
        and add the key of self to the second element (a set) of the value
        list if the value of self contains the element in either union1 or
        union2. Appearances in elements are to be counted.

        >>> V = Candidate({ # candidates of submatrix1
        ...         (0, 1): {'5', '4', '7', '9'}, 
        ...         (1, 0): {'9', '4'}, 
        ...         (1, 1): {'5', '4', '6', '9'}, 
        ...         (1, 2): {'5', '4', '6', '9'}, 
        ...         (2, 1): {'5', '4', '7', '9', '6'}
        ...     },
        ...     elements = set([i for i in range(1, 10)])
        ... )
        ...
        >>> appearances = V.appearances(names = ['row', 'col'])
        >>> appearances.show == {
        ...     '1': [[0, 0], set()], 
        ...     '2': [[0, 0], set()], 
        ...     '3': [[0, 0], set()], 
        ...     '4': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}], 
        ...     '5': [[3, 2], {(0, 1), (2, 1), (1, 1), (1, 2)}], 
        ...     '6': [[2, 2], {(1, 2), (1, 1), (2, 1)}], 
        ...     '7': [[2, 1], {(0, 1), (2, 1)}], 
        ...     '8': [[0, 0], set()], 
        ...     '9': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}]
        ... }
        ...
        True
        '''

        return appearance.Appearance(C = self, names = names)


    def copy(self):
        '''(Candidate) -> Candidate

        Return the deep copy of self.

        >>> eg = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg = Candidate(
        ...     eg, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg_copy = eg.copy()
        >>> id(eg) != id(eg_copy)
        True
        >>> id(eg[(0, 2)]) != id(eg_copy[(0, 2)])
        True
        '''

        copied = {}
        for k, v in self.items():
            copied[k] = v.copy()
        return Candidate(copied.copy(), elements = self.elements)

    
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
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (0, 2): {'2'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (1, 3): {'3', '2', '1'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (2, 0): {'3', '4'}, 
        ...             (2, 1): {'4'}, 
        ...             (3, 1): {'4', '1'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     4: Candidate(
        ...         {
        ...             (2, 3): {'3', '2'}, 
        ...             (3, 2): {'3', '4'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         elements = {1, 2, 3, 4}
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
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     1: Candidate(
        ...         {
        ...             (1, 0): {'4', '1'}, 
        ...             (1, 1): {'4', '2', '1'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (1, 3): {'3', '2', '1'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (2, 0): {'3', '4'}, 
        ...             (2, 1): {'4'}, 
        ...             (2, 3): {'3', '2'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (3, 1): {'4', '1'}, 
        ...             (3, 2): {'3', '4'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         elements = {1, 2, 3, 4}
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
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     1: Candidate(
        ...         {
        ...             (1, 1): {'4', '2', '1'}, 
        ...             (2, 1): {'4'}, 
        ...             (3, 1): {'4', '1'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     2: Candidate(
        ...         {
        ...             (0, 2): {'2'}, 
        ...             (1, 2): {'3', '2'}, 
        ...             (3, 2): {'3', '4'}
        ...         },
        ...         elements = {1, 2, 3, 4}
        ...     ), 
        ...     3: Candidate(
        ...         {
        ...             (1, 3): {'3', '2', '1'}, 
        ...             (2, 3): {'3', '2'}, 
        ...             (3, 3): {'3'}
        ...         },
        ...         elements = {1, 2, 3, 4}
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
                result[g] = Candidate({}, elements = self.elements)
            number = 0
            for i in range(n, n ** 2 + 1, n):
                for j in range(n, n ** 2 + 1, n):
                    number += 1
                    for k, v in self.items():
                        if i - n <= k[0] < i and j - n <= k[1] < j:
                            result[number].update({k: v})
            return result
        for g in range(n ** 2):
            result[g] = Candidate({}, elements = self.elements)
            for k, v in self.items():
                if (by == 'row' and k[0] == g) or\
                    (by == 'col' and k[1] == g):
                    result[g].update({k: v})
        return result

    
    def items(self):
        '''(Candidate) -> dict_items of {(int, int), {object}}

        Return dict_items of self.
        '''

        return self.show.items()

    
    def keys(self):
        '''(Candidate) -> dict_keys of (int, int)

        Return dict_keys of self.

        >>> eg1 = {(0, 1): {1, 2, 4}, (0, 2): {6, 9}}
        >>> eg1 = Candidate(
        ...     eg1, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg1.keys()
        dict_keys([(0, 1), (0, 2)])
        '''

        return self.show.keys()


    def pop(self, key):
        '''(Candidate) -> None

        Pop out key and the respective value from self.

        >>> eg1 = Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg1 == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {9, 6}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        >>> eg1.pop((0, 1))
        >>> eg1 == Candidate(
        ...     {(0, 2): {9, 6}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        '''

        self.show.pop(key)

    
    def refine(self, entries_to_mutate, appearances = None, names = None):
        '''(Candidate, Candidate, Appearance or None, [str, str] or None)
            -> None

        Precondition: names is not None if appearances is None

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
        ... },
        ... elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> candids = candids_old.copy()
        >>> candids == candids_old
        True
        >>> entries_to_mutate = Candidate(
        ...     {}, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>>
        >>> # Case 1: only candids changes
        >>> candids_part1 = candids.group('submatrix')[1]
        >>> appearances1 = candids_part1.appearances(['row', 'col'])
        >>> appearances1.sieve()
        >>> appearances1.show == {
        ...     '4': [[1, 2], {(0, 1), (0, 0)}], 
        ...     '9': [[1, 2], {(0, 0), (0, 2)}], 
        ...     '5': [[1, 2], {(0, 1), (0, 0)}]
        ... }
        ...
        True
        >>> candids.refine(entries_to_mutate, appearances1)
        >>> entries_to_mutate == Candidate(
        ...     {}, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
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
        ... },
        ... elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        >>> 
        >>> # Case 2: only entries_to_mutate changes
        >>> candids_part2 = candids.group('submatrix')[2]
        >>> candids_old = candids.copy()
        >>> appearances2 = candids_part2.appearances(['row', 'col'])
        >>> appearances2.sieve()
        >>> appearances2.show == {
        ...     '8': [[1, 2], {(0, 3), (0, 5)}], 
        ...     '6': [[1, 1], {(0, 3)}]
        ... }
        ...
        True
        >>> candids.refine(entries_to_mutate, appearances2)
        >>> entries_to_mutate == Candidate(
        ...     {}, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        False
        >>> entries_to_mutate == Candidate(
        ...     {(0, 3): {'6'}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        True
        >>> candids == candids_old 
        True
        >>>
        >>> # Case 3: both candids and entries_to_mutate change
        >>> candids_part3 = candids.group('submatrix')[3]
        >>> appearances3 = candids_part3.appearances(['row', 'col'])
        >>> appearances3.sieve()
        >>> appearances3.show == {
        ...     '1': [[1, 2], {(0, 6), (0, 8)}], 
        ...     '2': [[1, 1], {(2, 7)}], 
        ...     '5': [[1, 1], {(1, 6)}],
        ...     '7': [[2, 1], {(2, 7), (0, 7)}]
        ... }
        ...
        True
        >>> candids.refine(entries_to_mutate, appearances3)
        >>> entries_to_mutate == Candidate(
        ...     {}, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        False
        >>> entries_to_mutate == Candidate(
        ...     {(0, 3): {'6'}, (1, 6): {'5'}, (2, 7): {'2'}},
        ...     elements = set([str(i) for i in range(1, 10)])
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
        ... },
        ... elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        '''

        if appearances is None:
            assert names is not None, \
                'If appearances is None, then names must not be None.'
            appearances = self.appearances(names)
        appearances.sieve()
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


    def unions(self):
        '''(Candidate) -> Union

        Return the unions of candidates at each group.

        >>> V = Candidate({ # candidates of submatrix1
        ...     (0, 1): {'5', '4', '7', '9'}, 
        ...     (1, 0): {'9', '4'}, 
        ...     (1, 1): {'5', '4', '6', '9'}, 
        ...     (1, 2): {'5', '4', '6', '9'}, 
        ...     (2, 1): {'5', '4', '7', '9', '6'}
        ... },
        ... elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> unions = V.unions()
        >>> unions.show == {
        ...     'submatrix': {
        ...         1: {'7', '5', '9', '6', '4'}
        ...     }, 
        ...     'row': {
        ...         0: {'7', '4', '9', '5'}, 
        ...         1: {'4', '9', '6', '5'}, 
        ...         2: {'7', '9', '6', '4', '5'}
        ...     }, 
        ...     'col': {
        ...         0: {'9', '4'}, 
        ...         1: {'7', '5', '9', '6', '4'}, 
        ...         2: {'9', '6', '4', '5'}
        ...     }
        ... }
        ...
        True
        '''

        return union.Union(self)


    def update(self, other):
        '''(Candidate, Candidate or {(int, int): set of objects}) -> None

        Update self using other.

        >>> eg1 = Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> eg1.update(
        ...     Candidate(
        ...         {(1, 2): {1, 7}},
        ...         elements = set([str(i) for i in range(1, 10)])
        ...     )
        ... )
        ...
        >>> eg1 == Candidate(
        ...     {(0, 1): {1, 2, 4}, (0, 2): {6, 9}, (1, 2): {1, 7}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        >>> eg1.update(
        ...     Candidate(
        ...         {(0, 1): {1}}, 
        ...         elements = set([str(i) for i in range(1, 10)])
        ...     )
        ... )
        ...
        >>> eg1 == Candidate(
        ...     {(0, 1): {1}, (0, 2): {6, 9}, (1, 2): {1, 7}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        >>> eg1.update({(0, 0): {3}, (1, 2): {7}})
        >>> eg1 == Candidate(
        ...     {(0, 0): {3}, (0, 1): {1}, (0, 2): {6, 9}, (1, 2): {7}},
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        True
        '''

        if type(other) == dict:
            for k, v in other.items():
                other[k] = set(map(lambda x: str(x), list(v)))
            self.show.update(other)
        elif type(other) == Candidate:
            if self.n != other.n:
                raise ValueError('self.n != other.n')
            self.show.update(other.show)


    def values(self):
        '''(Candidate) -> dict_values of {objects}

        Return dict_values of self.
        '''

        return self.show.values()



if __name__ == '__main__':
    import doctest
    doctest.testmod()
