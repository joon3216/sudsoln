
import sudsoln.candidate as candidate


class Appearance():
    '''Appearance collection.'''

    def __init__(self, C, names = None):
        '''(Appearance, Candidate, [str, str]) -> None

        Preconditions:
        1. names is not None and len(set(names)) == 2
        2. set(names).issubset(['col', 'row', 'submatrix'])

        Initialize Appearance object.
        '''

        assert names is not None, 'names should be specified.'
        assert len(set(names)) == 2, 'len(set(names)) != 2'
        assert set(names).issubset(['col', 'row', 'submatrix']), \
            'Invalid name in names'

        elements = C.elements
        unions = C.unions()
        union1, union2 = unions.aggregate(names)
        appearances = {}
        for a in elements:
            appearances[a] = [[0, 0], set()]
        for number1 in union1:
            appearances[number1][0][0] += 1
            for kV, vV in C.items():
                if number1 in vV:
                    appearances[number1][1].update([kV])
        for number2 in union2:
            appearances[number2][0][1] += 1
            for kV2, vV2 in C.items():
                if number2 in vV2:
                    appearances[number2][1].update([kV2])

        self.show = appearances
        self.elements = elements
        self.n = C.n
        self.names = names


    def __repr__(self):
        '''(Appearance) -> str

        Print the representation of Appearance.

        >>> V = candidate.Candidate(
        ...     {
        ...         (0, 1): {'4', '9', '7', '5'}, 
        ...         (1, 0): {'9', '4'}, 
        ...         (1, 1): {'4', '9', '6', '5'}, 
        ...         (1, 2): {'4', '9', '6', '5'},
        ...         (2, 1): {'7', '9', '6', '5', '4'}
        ...     }, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> names = ['row', 'col']
        >>> Appearance(V, names)
        Appearance(
        {
        '1': [[0, 0], set()],
        '2': [[0, 0], set()],
        '3': [[0, 0], set()],
        '4': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}],
        '5': [[3, 2], {(0, 1), (2, 1), (1, 1), (1, 2)}],
        '6': [[2, 2], {(1, 2), (1, 1), (2, 1)}],
        '7': [[2, 1], {(0, 1), (2, 1)}],
        '8': [[0, 0], set()],
        '9': [[3, 3], {(0, 1), (1, 2), (2, 1), (1, 0), (1, 1)}]
        },
        n: 3
        elements: {1, 2, 3, 4, 5, 6, 7, 8, 9}
        names: 'row', 'col' (in this order)
        )
        '''

        elements = self.elements
        headline, mid, endline = 'Appearance(\n{\n', "", ""

        KVs = list(self.show.items())
        KVs.sort()
        lenKVs = len(KVs)
        i = 0
        for k, v in KVs:
            if i != len(KVs) - 1:
                mid += "'{0}': {1},\n".format(k, v)
            else:
                mid += "'{0}': {1}\n}},\n".format(k, v)
            i += 1

        elements_ord = list(elements)
        elements_ord.sort()
        el_strs = ''
        for ch in enumerate(elements_ord):
            if ch[0] != len(elements_ord) - 1:
                el_strs += ch[1] + ', '
            else:
                el_strs += ch[1]
        endline += 'n: {0}\n'.format(self.n)
        endline += 'elements: {{{0}}}\n'.format(el_strs)
        endline += "names: '{0}', '{1}' (in this order)\n)".format(
            self.names[0], self.names[1]
        )

        return headline + mid + endline


    def items(self):
        '''(Appearance) -> dict_items

        Return dict_items of self.show.
        '''

        return self.show.items()


    def sieve(self):
        '''(Appearance) -> None

        Update self so that if the first element of the value list does
        not contain 1, then the responsible key gets removed from
        self.

        >>> V = candidate.Candidate(
        ...     {
        ...         (0, 1): {'4', '9', '7', '5'}, 
        ...         (1, 0): {'9', '4'}, 
        ...         (1, 1): {'4', '9', '6', '5'}, 
        ...         (1, 2): {'4', '9', '6', '5'},
        ...         (2, 1): {'7', '9', '6', '5', '4'}
        ...     }, 
        ...     elements = set([str(i) for i in range(1, 10)])
        ... )
        ...
        >>> names = ['row', 'col']
        >>> appearances = Appearance(V, names)
        >>> appearances.sieve()
        >>> appearances.show == {'7': [[2, 1], {(0, 1), (2, 1)}]}
        True
        '''

        appearances_cp = self.show.copy()
        for k2, v2 in appearances_cp.items():
            if 1 not in v2[0]:
                self.show.pop(k2)



if __name__ == '__main__':
    import doctest
    doctest.testmod()