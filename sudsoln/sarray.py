
class Array():
    '''A 2-dimensional array.'''

    def __init__(self, array):
        '''(Array, list of objects or [objects]) -> None

        Initialize the Array object.

        >>> test = [
                [1, 2, 3, 4], 
                [5, 2, 0, 3], 
                [7, 5, 1, 0], 
                [2, 6, 2, 4]
            ]
        >>> test = Array(test)
        '''

        mkstr = lambda x: str(x) if type(x) != str else x
        flat = []
        ncols = []
        for i in range(len(array)):
            ncols.append(len(array[i]))
            array[i] = list(map(mkstr, array[i]))
            flat.extend(array[i])
        ncols_is_uniform = (len(set(ncols)) == 1)

        self.show = array
        self.flat = flat
        self.nrow = len(array)
        self.ncol = max(ncols)
        if ncols_is_uniform:
            self.shape = (self.nrow, self.ncol)
        else:
            self.shape = (self.nrow, )
        self.size = sum(ncols)


    def __getitem__(self, key):
        '''(Array, (int, int)) -> object

        Return the entry of self at key.
        
        >>> test = [
        ...     [1, 2, 3, 4], 
        ...     [5, 2, 0, 3], 
        ...     [7, 5, 1, 0], 
        ...     [2, 6, 2, 4]
        ... ]
        ...
        >>> test = Array(test)
        >>> test[(0, 1)]
        '5'
        >>> test[2, 3]
        '0'
        '''
        
        return self.show[key]


    def __list__(self):
        '''(Array) -> list

        Return the list representation of self.

        >>> test = [
        ...     [1, 2, 3], 
        ...     [5, 2, 0], 
        ...     [7, 5, 1]
        ... ]
        ...
        >>> test = Array(test)
        >>> list(test)
        [['1', '2', '3'], ['5', '2', '0'], ['7', '5', '1']]
        '''

        return self.show


    def __repr__(self, key):
        '''(Array) -> str

        Return the Array representation of self.
        >>> test = [
        ...     [1, 2, 3, 4], 
        ...     [5, 2, 0, 3], 
        ...     [7, 5, 1, 0], 
        ...     [2, 6, 2, 4]
        ... ]
        ...
        >>> test = Array(test)
        >>> test
        Array([
        ['1', '2', '3', '4'],
        ['5', '2', '0', '3'],
        ['7', '5', '1', '0'],
        ['2', '6', '2', '4']
        ])
        '''

        headline, midline, endline = 'Array([', '', '])'
        


    def __setitem__(self, key, value):
        '''(Array, (int, int), object) -> None

        Assign value to self's key.
        '''

    def copy(self):
        '''(Array) -> Array

        Return the deep copy of self.
        '''


    def flatten(self):
        '''(Array) -> list of str

        Return the flatten version of self.

        >>> test = [
        ...     [1, 2, 3], 
        ...     [5, 2, 0], 
        ...     [7, 5, 1]
        ... ]
        ...
        >>> test = Array(test)
        >>> test.flatten()
        ['1', '2', '3', '5', '2', '0', '7', '5', '1']
        '''

        return self.flat


    def itemset(self):
        '''(Array) -> None
        
        Itemset
        '''

    def reshape(self):
        '''(Array) -> Array

        Reshape
        '''

    def shape(self):
        '''(Array) -> (int, int)

        Shape of self.
        '''
