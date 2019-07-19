

# Under construction...


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
        self.n_sq = len(lst) ** 2