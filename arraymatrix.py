"""
Class-based array allowing tuple subscripting
"""
import array as sys_array

class array:

    def __init__(self, M, N, P):
        "Create an M-element list of N-element row lists of P-element lists."
        self._data = sys_array.array("i", [0] * M * N * P)
        self._rows = M
        self._cols = N
        self._cows = P #I couldn't find an agreed upon term so I word mashed

    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col, cow = self._validate_key(key)
        return self._data[row*self._cols*self._cows+col*self._cows+cow]
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col, cow = self._validate_key(key)
        self._data[row*self._cols*self._cows+col*self._cows+cow] = value
    
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        row, col, cow = key
        if (0 <= row < self._rows and
                0 <= col < self._cols and
                0 <= cow < self._cows):
            return key
        raise KeyError("Subscript out of range")

