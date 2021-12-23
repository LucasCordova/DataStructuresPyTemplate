from typing import Any
from copy import deepcopy


class Array:
    """ Class Array - representing 1D data using a List
            Stipulations:
            1. Must use a sized Python list as the internal data structure
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, size: int = 0, *items) -> None:
        """ Constructor
            Usage:  array = Array(10)
            @:param size the desired size of the Array (optional if providing instance)
            @:param *items a variable list of arguments that contain the items to be deep copied into the Array.
            @:return none
            @:raises TypeError if instance is provided and it is not an Array instance
        """
        raise NotImplementedError

    @classmethod
    def clone(cls, array_instance: 'Array') -> 'Array':
        """ Clone the array
            Usage:  array = Array.clone(instance)
            @:param instance an Array instance to deep copy data from.
            @:return a deep object copy of the array
            @:raises TypeError if instance is provided and it is not an Array instance
            """
        raise NotImplementedError

    def __getitem__(self, index: int) -> Any:
        """ Bracket operator for getting an item
            Usage: val = array[0]
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    def __setitem__(self, index: int, item: Any) -> None:
        """ Bracket operator for setting an item
            Usage: array[index] = val
            @:param index the desired index to set
            @:param item the desired item to set at index
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """ len operator for getting length of the array
            Usage: for i in range(len(array))
            @:return the length of the Array
        """
        raise NotImplementedError

    def resize(self, new_size: int) -> None:
        """ Resize an Array
            Usage: array.resize(5)
            @:param new_size the desired new size
            @:return none
        """
        raise NotImplementedError

    def __eq__(self, other: 'Array') -> bool:
        """ Equality operator ==
            Usage: are_equal = array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError
    
    def __ne__(self, other: 'Array') -> bool:
        """ Non-equality operator !=
            Usage: are_equal = array1 != array2
            @:param other the instance to compare self to
            @:return true if the arrays are not equal (deep check)
        """
        raise NotImplementedError

    def __iter__(self) -> Any:
        """ Iterator operator
            Usage: for item in array:
            @:return yields the item at index
        """
        raise NotImplementedError

    def __reversed__(self) -> Any:
        """ Reversed iterator operator
            Usage: for item in reversed(array):
            @:return yields the item at index starting at the end
        """
        raise NotImplementedError

    def __delitem__(self, index: int) -> None:
        """ Delete an item in the array. Copies the array contents from index + 1 down
            to fill the gap caused by deleting the item and shrinks the array size down by one
            Usage: del array[0]
            @:param index the desired index to delete
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        raise NotImplementedError

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in)
            Usage: if 3 in array:
            @:param item the desired item to check whether it's in the array
            @:return true if the array contains the item
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the array
            Usage: array.clear():
            @:return none
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(array):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
