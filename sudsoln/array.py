
class Array():
    '''A 2-dimensional array.'''

    def __init__(self, lst):
        '''(Array, list of list of objects) -> None

        Precondition: 
        1. len(lst) == len(lst[0])
        2. 

        Initialize the Array object.

        >>> test = [
                [1, 2, 3, 4], 
                [5, 2, 0, 3], 
                [7, 5, 1, 0], 
                [2, 6, 2, 4]
            ]
        >>> test = Array(test)
        '''

        self.show = lst
        self.n = len(lst)

    def __getitem__(self, key):
        '''(Array, (int, int)) -> object

        Return the entry of self at key.
        '''

    def __repr__(self, key):
        '''(Array) -> str

        Return the Array representation of self.
        '''

    def __setitem__(self, key, value):
        '''(Array, (int, int), object) -> None

        Assign value to self's key.
        '''

    def copy(self):
        '''(Array) -> Array

        Return the deep copy of self.
        '''

    def flat(self):
        '''

        Flat version of self.
        '''

    def flatten(self):
        '''
        Flatten version of self.
        '''

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
