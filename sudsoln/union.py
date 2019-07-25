
import sudsoln.candidate as candidate


class Union():
    '''Union of candidates at each group.'''

    def __init__(self, C):
        '''(Union, Candidate) -> None

        Initialize Union.

        >>> # import sudsoln.candidate as sc
        >>> V = candidate.Candidate(
        ...     { # candidates of submatrix1
        ...         (0, 1): {'5', '4', '7', '9'}, 
        ...         (1, 0): {'9', '4'}, 
        ...         (1, 1): {'5', '4', '6', '9'}, 
        ...         (1, 2): {'5', '4', '6', '9'}, 
        ...         (2, 1): {'5', '4', '7', '9', '6'}
        ...     },
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> unions = Union(V)
        '''
        
        elements = C.elements

        group_col = C.group('col')
        group_col_cp = group_col.copy()
        group_row = C.group('row')
        group_row_cp = group_row.copy()
        group_sub = C.group('submatrix')
        group_sub_cp = group_sub.copy()
        
        gcu = {}
        gru = {}
        gsu = {}
        
        for Kc, Vc in group_col_cp.items():
            if Vc == candidate.Candidate({}, elements = elements):
                group_col.pop(Kc)
        for Kr, Vr in group_row_cp.items():
            if Vr == candidate.Candidate({}, elements = elements):
                group_row.pop(Kr)
        for Ks, Vs in group_sub_cp.items():
            if Vs == candidate.Candidate({}, elements = elements):
                group_sub.pop(Ks)
                
        for ck, cv in group_col.items():
            gcu[ck] = set()
            for cvv in cv.values():
                gcu[ck] = gcu[ck].union(cvv)
        for rk, rv in group_row.items():
            gru[rk] = set()
            for rvv in rv.values():
                gru[rk] = gru[rk].union(rvv)
        for sk, sv in group_sub.items():
            gsu[sk] = set()
            for svv in sv.values():
                gsu[sk] = gsu[sk].union(svv)

        result = {'submatrix': gsu, 'row': gru, 'col': gcu}

        self.show = result
        self.n = C.n


    def __eq__(self, other):
        '''(Union, Union) -> bool
        
        Return True iff self.show == other.show and n are the same.
        '''

        return self.show == other.show and self.n == other.n


    def __repr__(self):
        '''(Union) -> str

        Print the representation of Union.
        '''

        headline, endline = "Union(\n", "n: {0}\n)".format(self.n)
        itms = [(k, v) for k, v in self.show.items()]
        itms.sort()
        mid = "{{'{0}': {1},\n".format(itms[0][0], itms[0][1])
        for i in range(1, len(itms) - 1):
            mid += " '{0}': {1},\n".format(itms[i][0], itms[i][1])
        last = len(itms) - 1
        mid += " '{0}': {1}}},\n".format(itms[last][0], itms[last][1])

        return headline + mid + endline


    def aggregate(self, names):
        '''(Union, [str, str]) -> [objects], [objects]
        
        Preconditions:
        1. len(set(names)) == 2
        2. set(names).issubset(['col', 'row', 'submatrix'])
        
        Aggregate value sets of self by names, and return two lists of
        numbers/objects consisting of elements in value sets.

        >>> V = candidate.Candidate(
        ...     { # candidates of submatrix1 of 9x9 sudoku
        ...         (0, 1): {'5', '4', '7', '9'}, 
        ...         (1, 0): {'9', '4'}, 
        ...         (1, 1): {'5', '4', '6', '9'}, 
        ...         (1, 2): {'5', '4', '6', '9'}, 
        ...         (2, 1): {'5', '4', '7', '9', '6'}
        ...     },
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> unions = Union(V)
        >>> rows_union, cols_union = unions.aggregate(['row', 'col'])
        >>> rows_union.sort(); cols_union.sort()
        >>> rows_union == [
        ...     '4', '4', '4', '5', '5', '5', '6', '6', '7', '7', 
        ...     '9', '9', '9'
        ... ]
        ...
        True
        >>> cols_union == [
        ...     '4', '4', '4', '5', '5', '6', '6', '7', '9', '9', '9'
        ... ]
        ...
        True
        '''

        letter1, letter2 = names[0], names[1]
        union1, union2 = [], []
        for K, V in self.items():
            if K == letter1: # usually row
                for v in V.values():
                    union1.extend(list(v))
            elif K == letter2: # usually col
                for v in V.values():
                    union2.extend(list(v))
        return union1, union2
    
    
    def items(self):
        '''(Union) -> dict_items
        
        Return the dict_items of self.show.
        '''
        
        return self.show.items()
        

    def keys(self):
        '''(Union) -> dict_keys
        
        Return the keys of self.show.
        '''

        return self.show.keys()


    def values(self):
        '''(Union) -> dict_values
        
        Return the values of self.show.
        '''
        
        return self.show.values()



if __name__ == '__main__':  
    import doctest
    doctest.testmod()
