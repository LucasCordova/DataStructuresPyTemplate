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
            Usage:  1. tuple = Tuple('A', 'B')
                    2. tuple = Tuple(('A', 'B'))
            @:param *items a variable list of arguments that contain the items to be deep copied into the Tuple.
                    Note: since items comes in as a tuple and a Python tuple or a Python list may be used to instantite the Tuple, 
                    it will form an embedded tuple like (('A', 'B', 'C')) or (['A', 'B', 'C']), which must be flattened 
                    before it can be stored in a Python tuple. 
            @:return none
            @:raises TypeError if instance is provided and it is not a Tuple instance
        """
        flattened_items = tuple(Tuple._flatten_helper(items))
        self._items = deepcopy(flattened_items)

    @classmethod
    def clone(cls, tuple_instance: 'Tuple') -> 'Tuple':
        """ Clone the Tuple
            Usage:  tuple = Tuple.clone(tuple_instance)
            @:param tuple_instance a tuple instance to deep copy data from.
            @:return a deep object copy of the tuple
            @:raises TypeError if instance is provided and it is not an Tuple instance
        """
        if tuple_instance is not None and not isinstance(tuple_instance, Tuple):
            raise TypeError('Instance is not a Tuple')
        return cls(tuple_instance._items)


    @staticmethod
    def _flatten_helper(items):
        """ This is a private helper function that flattens data down to individual items.
            This is not part of the list of methods provided to students
        """
        if (isinstance (items,tuple)):
            for item in items:
                yield from Tuple._flatten_helper(item)
        else:
            yield items


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
        return self._items

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
