from typing import Any

from adts.array import Array


class Array2D:
    """ Class Array2D - representing 2D data using a 1D array
            Stipulations:
            1. Must use an Array object as the internal data structure from the Array assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, row_len: int = 0, column_len: int = 0) -> None:
        """ Constructor
            Usage:  array = Array(10)
            @:param size the desired size of the Array
            @:param instance an optional Array2D instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not a LinkedList instance
        """
        raise NotImplementedError


    @staticmethod
    def clone(array2d_instance: 'Array2D') -> 'Array2D':
        """ Clone the array2d
            Usage:  array2d = Array2D.clone(instance)
            @:param instance an Array instance to deep copy data from.
            @:return a deep object copy of the array2d
            @:raises TypeError if instance is provided and it is not an Array2D instance
        """
        raise NotImplementedError


    def __getitem__(self, indexes: tuple) -> Any:
        """ Bracket operator for getting an item
            Usage: val = array2d[row_index][column_index]
            @:param indexes the desired row, col indexes in a tuple
            @:return the item at that indexes requested
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError


    def __setitem__(self, indexes: tuple, item) -> None:
        """ Bracket operator for setting an item
            Usage: array2d[row_index][column_index] = item
            @:param indexes the desired row, col indexes in a tuple
            @:return None
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    @property
    def dimensions(self):
        """ method for getting dimensions of the Array2D
            Usage: row_len, col_len = array2D.dimensions
            @:return the dimensions of the Array2D in form row_len, col_len
        """
        raise NotImplementedError

    def resize_columns(self, new_col_len: int) -> None:
        """ Resize the length of the columns
            Usage: array2d.resize_columns(new_columns_len)
            @:param new_columns_len the desired new length of the columns
            @:raises ValueError if the new_columns_len does not make sense
            @:return none
        """
        raise NotImplementedError


    def resize_rows(self, new_rows_len: int) -> None:
        """ Resize the length of the rows
                Usage: array2d.resize_rows(new_row_len)
                @:param new_rows_len the desired new length of the rows
                @:raises ValueError if the new_rows_len does not make sense
                @:return none
        """
        raise NotImplementedError


    def __eq__(self, other: 'Array2D') -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError


    def __ne__(self, other: 'Array2D') -> bool:
        """ Equality operator ==
            Usage: array1 != array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in)
            Usage: if 3 in array2d:
            @:param item the desired item to check whether it's in the array
            @:return true if the array contains the item
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the array2d
                Usage: array2d.clear():
                @:return none
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
                Usage: print(array2d):
                @:return str the string representation of the data and structure
        """
        raise NotImplementedError

