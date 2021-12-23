from typing import Any
from copy import deepcopy


class Tuple:
    """ Class Tuple - representing a tuple as a Tuple
            Stipulations:
            1. Must use a Python tuple as the internal data structure.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.

    """

    def __init__(self, *items: tuple) -> None:
        """ Constructor
            Usage:  tuple = Tuple('My', 'Tuple')
            @:param *data a variable list of arguments that contain the items to be deep copied into the Tuple.
            @:return none
            @:raises TypeError if instance is provided and it is not a Tuple instance
        """
        raise NotImplementedError

    @classmethod
    def clone(cls, tuple_instance: 'Tuple'):
        """ Clone the Tuple
            Usage:  tuple = Tuple.clone(tuple_instance)
            @:param tuple_instance a tuple instance to deep copy data from.
            @:return a deep object copy of the tuple
            @:raises TypeError if instance is provided and it is not an Tuple instance
        """
        raise NotImplementedError

    def __getitem__(self, index: int) -> Any:
        """ Bracket operator for getting an item from the Tuple. Only 0 through len(self._data) are permitted for index.
            Usage: tuple = Tuple('one', 'two', 'three')
            val = tuple[0] # val should contain the value 'one'
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError

    def __eq__(self, other: 'Tuple') -> bool:
        """ Equality operator ==
            Usage: tuple1 == tuple2
            @:param other the instance to compare self to
            @:return true if the tuples are equal (deep check)
        """
        raise NotImplementedError

    def __ne__(self, other: 'Tuple') -> bool:
        """ Non-Equality operator !=
            Usage: tuple1 != tuple2
            @:param other the instance to compare self to
            @:return true if the tuples are NOT equal (deep check)
        """
        raise NotImplementedError

    @property
    def data(self) -> tuple:
        """ Data Getter property used only for testing
            Usage: tuple_data: tuple = tuple.data
            @:param none
            @:return _data the tuple containing the Tuple's data
        """
        raise NotImplementedError

    def __iter__(self) -> Any:
        """ Iterator operator
            Usage: for item in tuple:
            @:return yields the item at index
        """
        raise NotImplementedError

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in)
            Usage: tuple = Tuple(1, 2, 3)
                   result = 1 in tuple # result should be true
            @:param item the desired item to check whether it's in the tuple
            @:return true if the tuple contains the item
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(tuple):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
