from typing import Any


class ListStack:
    """ Class ListStack - representing a stack using a LinkedList
            Stipulations:
            1. Must use a LinkedList as the internal data structure from the LinkedList assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, instance: 'ListStack' = None) -> None:
        """ Constructor
            Usage:  stack = ListStack()
            @:param instance an optional ListStack instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ListStack instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'ListStack') -> 'ListStack':
        """ Clone the stack
            Usage:  stack = ListStack.clone(instance)
            @:param instance an ListStack instance to deep copy data from.
            @:return a deep object copy of the stack
            @:raises TypeError if instance is provided and it is not an Stack instance
        """
        raise NotImplementedError

    def push(self, item: Any) -> None:
        """ Push an item onto the stack
            Usage:   stack.push(item)
            @:param item to push
            @:return none
        """
        raise NotImplementedError

    def pop(self) -> Any:
        """ Pop an item from the stack and return the item
            Usage:   item = stack.pop()
            @:return item that is popped
            @:raises IndexError if the stack is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the stack
            Usage: stack.clear():
            @:return none
        """
        raise NotImplementedError

    @property
    def top(self) -> Any:
        """ Get the item at the top of the stack
            Usage:   item = stack.top
            @:return item that is at the top of the stack
            @:raises IndexError if the stack is empty
        """
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        """ Check whether the stack is empty
            Usage:   empty = stack.empty
            @:return empty boolean as to whether the stack is empty
        """
        raise NotImplementedError

    def __eq__(self, other: 'ListStack') -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """ len operator for getting length of the stack
            Usage: length = len(stack)
            @:return the length of the Stack (number of items on the stack)
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(stack):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
