from typing import Any


class Array2D:
    """ Class Array2D - representing 2D data using a 1D array
        Stipulations:
            1. Must use an Array object as the internal data structure from the Array assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    class _Row:
        """ Private inner class _Row - represents a row in the 2D array
        """

        def __init__(self, array2d: 'Array2D', row_index: int) -> None:
            """ Constructor - represents a row in the 2D array
                Usage:  row = _Row(array2d, row_index)
                @:param array2d the corresponding Array2D that the row belongs to.
                @:param row_index the row index of the row in question
                @:return none
            """
            raise NotImplementedError

        def __getitem__(self, column_index: int) -> Any:
            """ Bracket operator for getting an item
                Usage: val = array2d[row_index][column_index]
                @:param column_index the desired column_index
                @:return the item at array2d[row_index][column_index]
                @:raises IndexError if the location is out of bounds
            """
            raise NotImplementedError

        def __setitem__(self, column_index: int, data: Any) -> None:
            """ Bracket operator for setting an item
                        Usage: array2d[row_index][column_index] = val
                        @:param column_index the desired column_index
                        @:return the item at array2d[row_index][column_index]
                        @:raises IndexError if the location is out of bounds
            """
            raise NotImplementedError

    def __init__(self, row_len: int = 0, column_len: int = 0, instance: 'Array2D'=None) -> None:
        """ Constructor
            Usage:  array = Array(10)
            @:param size the desired size of the Array
            @:param instance an optional Array2D instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not a Array2D instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'Array2D') -> 'Array2D':
        """ Clone the array2d
            Usage:  array2d = Array2D.clone(instance)
            @:param instance an Array instance to deep copy data from.
            @:return a deep object copy of the array2d
            @:raises TypeError if instance is provided and it is not an Array2D instance
        """
        raise NotImplementedError

    def __getitem__(self, row_index: int) -> 'Array2D._Row':
        """ Bracket operator for getting an item
            Usage: val = array2d[row_index][column_index]
            @:param row_index the desired index
            @:return the _Row at the row_index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    def getitem(self, row_index: int, column_index: int) -> Any:
        """ Helper method for getting an item
            Usage: val = array2d.getitem(row_index, column_index)
            @:param row_index the desired row_index
            @:param column_index the desired column_index
            @:return the item at the row_index, column_index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    def setitem(self, row_index: int, column_index: int, data: Any) -> None:
        """ Helper method for setting an item
            Usage: array2d[row_index][column_index] = val
            @:param row_index the desired row_index to set
            @:param column_index the desired column_index to set
            @:param data the desired data to set at indexes
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        raise NotImplementedError

    @property
    def columns_len(self) -> int:
        """ len method for the length of the columns
                Usage: column_length = array2d.columns_len
                @:return the length of the columns
        """
        raise NotImplementedError

    @property
    def rows_len(self) -> int:
        """ len method for the length of the rows
            Usage: row_length = array2d.rows_len
            @:return the length of the rows
        """
        raise NotImplementedError

    def resize_columns(self, new_columns_len: int) -> None:
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

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in)
            Usage: if 3 in array2d:
            @:param item the desired item to check whether it's in the array
            @:return true if the array contains the item
            @:raises TypeError if other is not the right type to compare
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
