import datetime
import numpy as np

empty = "."
n = 3
one_to_n_sq = set([str(i) for i in range(1, n ** 2 + 1)])
easy_q = np.array(\
    [\
        [5, 3, "", "", 7, "", "", "", ""],
        [6, "", "", 1, 9, 5, "", "", ""],
        ["", 9, 8, "", "", "", "", 6, ""],
        [8, "", "", "", 6, "", "", "", 3],
        [4, "", "", 8, "", 3, "", "", 1],
        [7, "", "", "", 2, "", "", "", 6],
        ["", 6, "", "", "", "", 2, 8, ""],
        ["", "", "", 4, 1, 9, "", "", 5],
        ["", "", "", "", 8, "", "", 7, 9]
    ]
)
question1 = np.array(\
    [\
        [empty, empty, empty, empty,     2, empty, empty, empty, empty],
        [    8,     3, empty,     7,     1,     4, empty,     9,     6], 
        [empty,     6, empty,     9, empty,     5,     4, empty,     8], 
        [empty,     9, empty,     3, empty,     1, empty, empty,     4], 
        [empty,     1, empty,     4, empty,     2, empty, empty,     7], 
        [empty,     7,     5, empty, empty, empty,     2,     1, empty], 
        [empty, empty,     4, empty, empty, empty,     7, empty, empty], 
        [empty, empty, empty,     5, empty,     7, empty, empty, empty], 
        [empty, empty, empty,     1,     9,     6, empty, empty, empty]
    ]
)
question2 = np.array(\
    [\
        ["", "",  3, "", "", "", "",  2, ""], 
        ["", "", "",  4,  1,  6, "", "",  5], 
        [ 6, "",  8, "", "", "", "", "", ""], 
        ["",  2, "",  9, "",  4, "",  6, ""], 
        ["",  6, "", "",  8, "", "",  7, ""], 
        ["",  3, "",  2, "",  7, "",  9, ""], 
        ["", "", "", "", "", "",  6, "",  4], 
        [ 2, "", "",  8,  4,  1, "", "", ""], 
        ["",  5, "", "", "", "",  9, "", ""]
    ]
)
question3 = np.array(\
    [\
        [ 3, "",  2, "", "", "", "",  6, ""], 
        ["", "", "",  7, "",  8,  1, "", ""], 
        ["", "", "", "", "", "", "", "", ""], 
        [ 5,  8, "",  4, "", "", "", "", ""], 
        ["", "", "", "", "", "", "",  1,  2], 
        ["", "", "",  1, "", "", "", "", ""], 
        ["",  1, "", "", "", "",  4, "", ""], 
        [ 6, "", "", "",  3, "", "", "", ""], 
        ["", "", "", "",  2, "", "", "", ""]
    ]
)
question4 = np.array(\
    [\
        ["", "", "",  7, "", "", "", "", ""], 
        [ 1, "", "", "", "", "", "", "", ""], 
        ["", "", "",  4,  3, "",  2, "", ""], 
        ["", "", "", "", "", "", "", "",  6], 
        ["", "", "",  5, "",  9, "", "", ""], 
        ["", "", "", "", "", "",  4,  1,  8], 
        ["", "", "", "",  8,  1, "", "", ""], 
        ["", "",  2, "", "", "", "",  5, ""], 
        ["",  4, "", "", "", "",  3, "", ""]
    ]
)
# candidate7 = question7.solve_by_pairs() yields one-element candid value
# If we plug that in into question7.itemsets(candidate7.show),
# and we use question7.solve_logically(),
# then we get the answer for question7.
question7 = np.array(\
    [\
        [ 8,  5, '', '', '',  2,  4, '', ''],
        [ 7,  2, '', '', '', '', '', '',  9],
        ['', '',  4, '', '', '', '', '', ''],
        ['', '', '',  1, '',  7, '', '',  2],
        [ 3, '',  5, '', '', '',  9, '', ''],
        ['',  4, '', '', '', '', '', '', ''],
        ['', '', '', '',  8, '', '',  7, ''],
        ['',  1,  7, '', '', '', '', '', ''],
        ['', '', '', '',  3,  6, '',  4, '']
    ]
)
question7_1 = np.array(\
    [\
        [ 8, '', '', '', '', '', '', '', ''],
        ['', '',  3,  6, '', '', '', '', ''],
        ['',  7, '', '',  9, '',  2, '', ''],
        ['',  5, '', '', '',  7, '', '', ''],
        ['', '', '', '',  4,  5,  7, '', ''],
        ['', '', '',  1, '', '', '',  3, ''],
        ['', '',  1, '', '', '', '',  6,  8],
        ['', '',  8,  5, '', '', '',  1, ''],
        ['',  9, '', '', '', '',  4, '', '']
    ]
)
sta410_question = np.array(\
    [\
        [ 1,  5,  7,  6,  4, '', '',  8, ''], 
        ['',  4, '', '', '', '', '', '', ''], 
        ['',  3,  2,  9, '', '',  1,  4, ''], 
        [ 7, '',  4,  1, '',  5,  2, '', ''],
        [ 2, '', '',  8,  6, '', '',  7,  4], 
        ['', '', '', '',  7, '', '', '',  1], 
        ['',  8, '', '',  2,  1, '', '', ''], 
        ['', '', '',  3, '',  4, '',  1,  9], 
        ['', '', '',  5, '',  6,  8,  2, '']
    ]
)
for i in range(n ** 2):
    for j in range(n ** 2):
        if easy_q[(i, j)] == '':
            easy_q.itemset((i, j), empty)
        if question2[(i, j)] == "":
            question2.itemset((i, j), empty)
        if question3[(i, j)] == "":
            question3.itemset((i, j), empty)
        if question4[(i, j)] == "":
            question4.itemset((i, j), empty)
        if question7[(i, j)] == "":
            question7.itemset((i, j), empty)
        if question7_1[(i, j)] == "":
            question7_1.itemset((i, j), empty)
        if sta410_question[(i, j)] == '':
            sta410_question.itemset((i, j), empty)



class Candidate():
    '''Sudoku puzzle candidate collection.'''

    def __init__(self, candidates):
        '''(Candidate, {(int, int): set of ints}) -> None
        Precondition: ints in (int, int) are from 0 to n ** 2 - 1
        inclusive; ints in values are from 1 to n ** 2 inclusive.
        Initialize Candidate object.
        '''

        self.show = candidates


    def __getitem__(self, key):
        '''(Candidate, (int, int)) -> set of ints
        Return the value of self at key.
        '''

        return self.show[key]


    def __eq__(self, other):
        '''(Candidate, Candidate) -> bool
        Return True iff keys and values of each keys match between
        self and other.
        '''

        return self.show == other.show


    def copy(self):
        '''(Candidate) -> Candidate
        
        Return the copy of self.
        '''

        return self.show.copy()


    def group(self, by):
        '''(Candidate, str) -> {int: {(int, int): set of int}}
        Precondition: by == 'submatrix' or 'row' or 'col'
        Return the candidate values grouped by 'by', which is either 
        'submatrix', 'row', or 'col'.       
        '''

        result = {}
        if by == 'submatrix':
            for g in range(1, n ** 2 + 1):
                result[g] = {}
            number = 0
            for i in range(n, n ** 2 + 1, n):
                for j in range(n, n ** 2 + 1, n):
                    number += 1
                    for k, v in self.items():
                        if i - n <= k[0] < i and j - n <= k[1] < j:
                            result[number].update({k: v})
            return result
        for g in range(n ** 2):
            result[g] = {}
            for k, v in self.items():
                if (by == 'row' and k[0] == g) or\
                    (by == 'col' and k[1] == g):
                    result[g].update({k: v})
        return result

    
    def items(self):
        '''(Candidate) -> dict_items of (int, int), {int}
        Return dict_items of self.
        '''

        return self.show.items()

    
    def keys(self):
        '''(Candidate) -> dict_keys of (int, int)
        Return dict_keys of self.
        '''

        return self.show.keys()


    def pop(self, key):
        '''(Candidate) -> None
        Pop out key and the respective value from self.
        '''

        self.show.pop(key)


    def refine(self, entries_to_mutate, appearances):
        '''(Candidate, dict, {int: [[int, int], {(int, int)}]}) -> None
        Update self and entries_to_mutate so that any unique candidate 
        number and the respective entry according to appearances is added
        to entries_to_mutate, and any candidate number that should be
        eliminated from some values of self due to the uniqueness of 
        candidate number in a certain row or column in appearances is
        eliminated.
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


    def values(self):
        '''(Candidate) -> dict_values of {int}
        Return dict_values of self.
        '''

        return self.show.values()



class Sudoku():
    '''Sudoku puzzle.'''
    
    def __init__(self, array):
        '''(Sudoku, list/array of [int and str]) -> NoneType
        
        Precondition: array.shape == (n ** 2, n ** 2)
        
        Initialize Sudoku puzzle.
        
        >>> empty = "."
        >>> question1 = Sudoku([\
        [empty, empty, empty, empty,     2, empty, empty, empty, empty],
        [    8,     3, empty,     7,     1,     4, empty,     9,     6], 
        [empty,     6, empty,     9, empty,     5,     4, empty,     8], 
        [empty,     9, empty,     3, empty,     1, empty, empty,     4], 
        [empty,     1, empty,     4, empty,     2, empty, empty,     7], 
        [empty,     7,     5, empty, empty, empty,     2,     1, empty], 
        [empty, empty,     4, empty, empty, empty,     7, empty, empty], 
        [empty, empty, empty,     5, empty,     7, empty, empty, empty], 
        [empty, empty, empty,     1,     9,     6, empty, empty, empty]
        ])
        >>> question1 = Sudoku(question1)
        '''
        
        # Need to raise error if union of all elements minus 
        # one_to_n_sq union {empty} is not the empty set.
        # Need to raise error if the shape of array is not square.
        # Need to raise error if the element denoting emptiness is not
        # a string.
        # Need to raise error if the element denoting emptiness is not
        # unique.
        self.show = np.array(array)


    def __eq__(self, other):
        '''(Sudoku, Sudoku) -> bool
        
        Return True iff all the entries of self and other are the same.
        '''
        
        return sum(sum(self.show == other.show)) == n ** 4


    def __str__(self):
        '''(Sudoku) -> str
        
        Return the string representation of self.
        '''
        
        result = ""
        flattened = self.show.flatten()
        for item in flattened:
            result += item
        return result


    def all_missings(self):
        '''(Sudoku) -> {str: {int: set of ints}}
        Return all missing values of all submatrices, rows, and columns
        of self.
        '''
        
        result = {'submatrix': {}, 'row': {}, 'col': {}}
        for i in range(n ** 2):
            result['submatrix'].update({i + 1: self.missing(s = i + 1)})
            result['row'].update({i: self.missing(r = i)})
            result['col'].update({i: self.missing(c = i)})
        return result


    def candidates(self, empty = '.'):
        '''(Sudoku[, str]) -> Candidate
        
        Return all numbers that can be entered at each entry of self 
        if that entry is empty.
        '''
        
        entries = {}
        for i in range(1, n ** 2 - 1, n): # e.g. n == 3 => 1, 4, 7
            subm, subm_missing = {}, {}
            for j in range(n): # define submatrices first
                subm[i + j] = self.submatrix(i + j)
                subm_missing[i + j] = self.missing(s = i + j)
            for K in range(n): # iterate over rows of a binded submatrix
                row_missing = self.missing(r = i + K - 1)
                subm_index = 0
                col_iters = list(range(n - 1, n ** 2, n))
                for L in range(n ** 2): # iterate over columns
                    if self.show[(i + K - 1, L)] == empty:
                        col_missing = self.missing(c = L)
                        entries[(i + K - 1, L)] =\
                            subm_missing[i + subm_index].intersection(\
                                row_missing, col_missing
                            )
                    if L == col_iters[subm_index]:
                        subm_index += 1
        return Candidate(entries)


    def col(self, c):
        '''(Sudoku) -> np.array of [int and str]
        
        Precondition: 0 <= c <= n ** 2 - 1
        
        Return one of n ** 2 columns of self selected by c.
        '''
        
        return self.show[:, c]


    def copy(self):
        '''(Sudoku) -> Sudoku
        
        Return a copy of self.
        '''
        
        puzzle_copy = self.show.copy()
        return Sudoku(puzzle_copy)


    def group(self, by):
        '''(Sudoku, str) -> {int: {(int, int): set of int}}
        Precondition: by == 'submatrix' or 'row' or 'col'
        Return the candidate values grouped by 'by', which is either 
        'submatrix', 'row', or 'col'.
        '''

        # Raise error if 'by' is neither of any specified strings.
        return self.candidates().group(by)


    def is_valid_answer(self, empty = "."):
        '''(Sudoku[, str]) -> bool
        Return True iff self is a valid sudoku answer, and False otherwise.
        '''

        if empty in self.show: # not even finished yet
            return False
        for i in range(n ** 2):
            if one_to_n_sq != set(self.submatrix(i + 1).flat):
                return False
            elif one_to_n_sq != set(self.row(i).flat):
                return False
            elif one_to_n_sq != set(self.col(i).flat):
                return False
        return True


    def itemset(self, entry, value):
        '''(Sudoku, (int, int), int) -> NoneType
        Precondition: value in one_to_n_sq; and each int in entry is from
        0 to n ** 2 - 1 inclusive.
        Mutate entry number of self to value.
        '''

        self.show.itemset(entry, value)


    def itemsets(self, entries):
        '''(Sudoku, {(int, int): set if ints} or Candidate) -> None
        Precondition: each int in entries is exactly one element of 
        one_to_n_sq.
        Mutate entry number of self according to values given in entries 
        if the value set has length 1.
        '''

        if type(entries) == dict:
            if entries == {}:
                return None
            for entry, values in entries.items():
                if len(values) == 1:
                    self.itemset(entry, list(values)[0])
        elif type(entries) == Candidate:
            if entries == Candidate({}):
                return None
            for entry, values in entries.items():
                if len(values) == 1:
                    self.itemset(entry, list(values)[0])


    def melt(self, include_empty = True):
        '''(Sudoku[, bool]) -> Candidate
        Return Candidate form of self, and include empty entries
        as well if include_empty is True (by default).
        '''

        result = {}
        for i in range(n ** 2):
            for j in range(n ** 2):
                result[(i, j)] = {self.show[(i, j)]}
        if not include_empty:
            result_copy = result.copy()
            for k, v in result_copy.items():
                if list(v)[0] == empty:
                    result.pop(k)
        return Candidate(result)


    def missing(self, s = None, r = None, c = None):
        '''(Sudoku[, int, int, int]) -> set of int
        
        Precondition: 1 <= s <= n ** 2 and\
        0 <= r <= n ** 2 - 1 and 0 <= c <= n ** 2 - 1
        
        Return all missing values of self at the specified submatrix 
        number s, the specified row number r, or the specified column 
        number c.
        If s is specified, then r and c will be ignored;
        if s is None and r is specified, then c will be ignored;
        If neither s, r, nor c are specified, the function returns 
        NoneType.
        '''
        
        if s is not None:
            return one_to_n_sq.difference(set(self.submatrix(s).flat))
        elif r is not None:
            return one_to_n_sq.difference(set(self.row(r).flat))
        elif c is not None:
            return one_to_n_sq.difference(set(self.col(c).flat))


    def row(self, r):
        '''(Sudoku) -> np.array of [int and str]
        
        Precondition: 0 <= r <= n ** 2 - 1
        
        Return one of n ** 2 rows of self selected by r.
        '''
        
        return self.show[r, :]


    def solve(self, max_trial = 300):
        '''(Sudoku, int) -> str
        Mutate self to the answer form, or until max_trial is met, and
        return the time it took to compute the answer.
        '''

        start = datetime.datetime.now()
        self.solve_logically()
        sudoku_copy = self.copy()
        if empty in self.show:
            print("Logical approaches weren't enough.")
            print("Solving with a brute force...")
            self.solve_forcefully(max_trial = max_trial)
        end = datetime.datetime.now()
        if self.is_valid_answer():
            return str(end - start)
        else:
            print('Mission failed; max_trial of', max_trial, 'met.')
            for i in range(n ** 2):
                for j in range(n ** 2):
                    self.itemset((i, j), sudoku_copy.show[(i, j)])
            return str(end - start)


    def solve_forcefully(self, max_trial = 300):
        '''(Sudoku, int) -> None
        Try out candidate numbers in each entry randomly until self is 
        mutated into the answer form, or until max_trial is met.
        '''

        trial = 1
        #sudoku_copy = self.show.copy()
        sudoku_melt = self.melt()
        while empty in self.show:
            if empty not in self.show:
                return None
            entries = self.solve_by_pairs()
            if set() in list(entries.values()):
                print(\
                    "Trial number ", trial, " out of ", max_trial, "; ",
                    round(trial * 100 / max_trial, 4), '%', ' in progress',
                    sep = ''
                )
                trial += 1
                if trial == max_trial:
                    return None
                self.itemsets(sudoku_melt)
            else:
                keys = list(entries.keys()); keys.sort()
                guess = np.random.choice(list(entries[keys[0]]), 1)[0]
                self.itemset(keys[0], guess)
                self.solve_logically()
                if empty not in self.show and not self.is_valid_answer():
                    self.itemsets(sudoku_melt)
        return None


    def solve_by_pairs(self):
        '''(Sudoku) -> Candidate
        Eliminate candidate numbers in other entries of the same rows or
        columns based on entries of submatrix it belongs, mutate self 
        into the closest answer form, and return a refined Candidate 
        (better than self.candidates() in a sense that it has fewer,
        equal at worst, candidate numbers at each entry) based on 
        iterations.
        '''

        names = ['row', 'col']
        changing = True
        candidates_global = self.candidates()
        candidates_group = self.group(by = 'submatrix')
        while changing:
            sudoku_copy = self.copy()
            entries_to_mutate = {}
            candidates_group_old = candidates_group.copy()
            for V in candidates_group_old.values(): # for each submatrix
                unions = initialize_unions(n, names)
                collect_unions(unions, n, names, V)
                r_union, c_union = aggregate_unions(unions, names)
                appearances = collect_appearances(r_union, c_union, V)
                sieve_appearances(appearances)
                candidates_global.refine(entries_to_mutate, appearances)
            self.itemsets(entries_to_mutate)
            self.itemsets(candidates_global)
            candidates_group = candidates_global.group(by = 'submatrix')
            if sudoku_copy == self and\
                candidates_group_old == candidates_group:
                changing = False
        return candidates_global


    def solve_globally(self):
        '''(Sudoku) -> None
        Find the only possible number at each entry of self, plug it 
        into that entry, and repeat the process until no new mutation 
        is made.
        '''

        changing = True
        while changing:
            sudoku_copy = self.copy()
            possible_numbers = self.candidates()
            for k, v in possible_numbers.items():
                if len(v) == 1:
                    self.itemset(k, list(v)[0])
            if sudoku_copy == self:
                changing = False


    def solve_locally(self, by):
        '''(Sudoku) -> NoneType
        Precondition: by == 'submatrix', 'row', or 'col'
        Find the unique candidate number within each 'by' of self,
        plug that number into that entry, and repeat the process across
        every other groups until no new mutation is made.
        '''

        changing = True
        while changing:
            sudoku_copy = self.copy()
            possible_numbers = self.unique_candidates(by = by)
            for k, v in possible_numbers.items():
                if len(v) == 1:
                    self.itemset(k, list(v)[0])
            if sudoku_copy == self:
                changing = False


    def solve_logically(self):
        '''(Sudoku) -> NoneType
        Mutate self to the answer form as close as possible (that is, 
        having the least number of empty's), using only logical 
        approaches that don't involve randomness or brute force in number
        assignment.
        '''

        there_is_a_progress = True
        sudoku_copy = self.copy()
        while there_is_a_progress:
            sudoku_copy_after_iter = self.copy()
            self.solve_globally()
            if empty not in str(self):
                return None
            for component in ['submatrix', 'row', 'col']:
                self.solve_locally(by = component)
                self.solve_globally()
                if empty not in str(self):
                    return None
            self.solve_by_pairs()
            if sudoku_copy == self or sudoku_copy_after_iter == self:
                there_is_a_progress = False


    def submatrix(self, s):
        '''(Sudoku) -> list/array of [int and str]
        Precondition: 1 <= s <= n ** 2
        Return one of n ** 2 submatrices of self selected by s.        
        '''
        
        number = 0
        for i in range(n, n ** 2 + 1, n):
            for j in range(n, n ** 2 + 1, n):
                number += 1
                if number == s:
                    return self.show[(i - n):(i), (j - n):(j)]
    

    def unique_candidates(self, by):
        '''(Sudoku, str) -> {(int, int): set of int}
        Precondition: by == 'submatrix' or 'row' or 'col'
        Return the unique candidate number at each entry, within each 
        group of self, grouped by 'by'.
        '''

        start = self.group(by = by)
        result = {}
        for V in start.values():
            keys = list(V.keys()); keys.sort() # sorting is unnecessary
            for i in range(len(keys)):
                blacklist, the_rest = [], set()
                blacklist.append(keys[i])
                for k, v in V.items():
                    if k not in blacklist:
                        the_rest.update(v)
                possible_nums = V[keys[i]].difference(the_rest)
                result.update({keys[i]: possible_nums})
        return result



def aggregate_unions(unions, names):
    '''({str: {ints}}, [str, str]) -> [ints], [ints]
    
    Precondition:
    1. len(names) == 2
    2. names has exactly two of either 'submatrix', 'row', or 'col'.
    3. If name is a key of unions, then name[:len(name) - 1] in names.
    Aggregate value sets of unions by names, and return two lists of
    numbers consisting of elements in value sets.
    >>> names = ['row', 'col']
    >>> unions = {\
            'row1': {'5', '4', '7', '9'}, 'row2': {'9', '5', '6', '4'}, 
            'row3': {'5', '9', '6', '4', '7'}, 
            'col1': {'9', '4'}, 'col2': {'5', '4', '7', '9', '6'}, 
            'col3': {'5', '4', '6', '9'}
        }
    >>> rows_union, cols_union = aggregate_unions(unions, names)
    >>> rows_union.sort(); cols_union.sort()
    >>> rows_union == [\
            '4', '4', '4', '5', '5', '5', '6', '6', '7', '7', 
            '9', '9', '9'
        ]
    True
    >>> cols_union == [\
            '4', '4', '4', '5', '5', '6', '6', '7', '9', '9', '9'
        ]
    True
    '''

    first_letter = names[0][0]
    union1, union2 = [], []
    for k_unions, v_unions in unions.items():
        if k_unions[:1] == first_letter: # usually row
            union1.extend(list(v_unions))
        else: # usually col
            union2.extend(list(v_unions))
    return union1, union2


def collect_appearances(union1, union2, V):
    '''([ints], [ints], {(int, int): {ints}}) -> 
        {int: [[int, int], {(int, int)}]}
    Count the number of the same elements in union1 and union2
    respectively, record them into the very first element (a list of two 
    ints) of the resulting dictionary's value list, and add the key of
    V to the second element (a set) of the value list if the value of V
    contains the element in either union1 or union2.
    >>> rows_union = [\
            '4', '4', '4', '5', '5', '5', '6', '6', '7', '7', 
            '9', '9', '9'
        ]
    >>> cols_union = [\
            '4', '4', '4', '5', '5', '6', '6', '7', '9', '9', '9'
        ]
    >>> V = {\
            (0, 1): {'4', '9', '7', '5'}, (1, 0): {'9', '4'}, 
            (1, 1): {'4', '9', '6', '5'}, (1, 2): {'4', '9', '6', '5'}, 
            (2, 1): {'7', '9', '6', '5', '4'}
        }
    >>> appearances = collect_appearances(rows_union, cols_union, V)
    >>> appearances == {\
            '1': [[0, 0], set()], 
            '2': [[0, 0], set()], 
            '3': [[0, 0], set()], 
            '4': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}], 
            '5': [[3, 2], {(0, 1), (2, 1), (1, 1), (1, 2)}], 
            '6': [[2, 2], {(1, 2), (1, 1), (2, 1)}], 
            '7': [[2, 1], {(0, 1), (2, 1)}], 
            '8': [[0, 0], set()], 
            '9': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}]
        }
    True
    '''

    appearances = {}
    for a in one_to_n_sq:
        appearances[a] = [[0, 0], set()]
    for number1 in union1:
        appearances[number1][0][0] += 1
        for kV, vV in V.items():
            if number1 in vV:
                appearances[number1][1].update([kV])
    for number2 in union2:
        appearances[number2][0][1] += 1
        for kV2, vV2 in V.items():
            if number2 in vV2:
                appearances[number2][1].update([kV2])
    return appearances


def collect_unions(unions, n, names, V):
    '''({str: set()}, int, [str, str], {(int, int): {ints}}) -> None
    Precondition: 
    1. Each value in unions is the empty set set().
    2. If name is a key of unions, then name[:len(name) - 1] in names.
    Update unions for each matched name in names so that each value set
    of unions is a collection of all candidate values specified in V,
    where V is a collection of subset candidates from n ** 2 by n ** 2 
    Sudoku.
    >>> n = 3
    >>> names = ['row', 'col']
    >>> unions = initialize_unions(n, names)
    >>> V = {\
            (0, 1): {'5', '4', '7', '9'}, (1, 0): {'9', '4'}, 
            (1, 1): {'5', '4', '6', '9'}, (1, 2): {'5', '4', '6', '9'}, 
            (2, 1): {'5', '4', '7', '9', '6'}
        }
    >>> collect_unions(unions, n, names, V)
    >>> unions == {\
            'row1': {'5', '4', '7', '9'}, 'row2': {'9', '5', '6', '4'}, 
            'row3': {'5', '9', '6', '4', '7'}, 
            'col1': {'9', '4'}, 'col2': {'5', '4', '7', '9', '6'}, 
            'col3': {'5', '4', '6', '9'}
        }
    True
    '''

    for k, v in V.items(): 
        for r in range(n):
            if k[0] in range(r, n ** 2, n):
                the_name1 = names[0] + str(r + 1)
                unions[the_name1].update(v)
                for c in range(n):
                    if k[1] in range(c, n ** 2, n):
                        the_name2 = names[1] + str(c + 1)
                        unions[the_name2].update(v)
                        break


def initialize_unions(n, names):
    '''(int, [str, str]) -> {str: set()}
    Precondition: 
    1. len(names) == 2
    2. names has exactly two of either 'submatrix', 'row', or 'col'.
    Create unions dictionary where each key is a numbered name of 
    Sudoku components (e.g. 'row1' or 'submatrix9') generated from names.
    
    >>> unions = initialize_unions(3, ['row', 'col'])
    >>> unions == {\
            'row1': set(), 'row2': set(), 'row3': set(),
            'col1': set(), 'col2': set(), 'col3': set()
        }
    True
    '''

    header1 = names[0]
    header2 = names[1]
    unions = {}
    for num in range(1, 2 * n + 1):
        if num <= n:
            the_name = header1 + str(num)
            unions.update({the_name: set()})
        else:
            the_name = header2 + str(num - n)
            unions.update({the_name: set()})
    return unions


def make_str_to_sudoku(sudoku_str):
    '''(str) -> Sudoku
    Precondition: set(list(sudoku_str)).issubset(one_to_n_sq.union('.'))
    Return the Sudoku object of sudoku_str if it is a string 
    representation of Sudoku.
    '''

    array = np.array(list(sudoku_str[:(n ** 4)])).reshape(n ** 2, n ** 2)
    return Sudoku(array)


def sieve_appearances(appearances):
    '''({int: [[int, int], {(int, int)}]}) -> None
    Update appearances so that if the first element of the value list
    does not contain 1, then the responsible key gets removed from
    appearances.
    >>> appearances = {\
            '1': [[0, 0], set()], 
            '2': [[0, 0], set()], 
            '3': [[0, 0], set()], 
            '4': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}], 
            '5': [[3, 2], {(0, 1), (2, 1), (1, 1), (1, 2)}], 
            '6': [[2, 2], {(1, 2), (1, 1), (2, 1)}], 
            '7': [[2, 1], {(0, 1), (2, 1)}], 
            '8': [[0, 0], set()], 
            '9': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}]
        }
    >>> sieve_appearances(appearances)
    >>> appearances == {'7': [[2, 1], {(0, 1), (2, 1)}]}
    True
    '''

    appearances_copy = appearances.copy()
    for k2, v2 in appearances_copy.items():
        if 1 not in v2[0]:
            appearances.pop(k2)
