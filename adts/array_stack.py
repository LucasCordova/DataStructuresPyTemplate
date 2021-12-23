from typing import Any


class ArrayStack:
    """ Class ArrayStack - representing a fixed-size stack using a 1D Array
                Stipulations:
                1. Must use an Array object as the internal data structure from the Array assignment.
                2. Must adhere to the docstring requirements per method, including raising
                   raising appropriate exceptions where indicated.
                               3. Must achieve a minimum of 92% code coverage through unit testing.

    """

    def __init__(self, max_size: int = 0, instance: 'ArrayStack' = None) -> None:
        """ Constructor
            Usage:  stack = ArrayStack(10)
            @:param size the desired size of the stack
            @:param instance an optional ArrayStack instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'ArrayStack') -> 'ArrayStack':
        """ Clone the stack
                Usage:  stack = ArrayStack.clone(instance)
                @:param instance an ArrayStack instance to deep copy data from.
                @:return a deep object copy of the stack
                @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        raise NotImplementedError

    def push(self, item: Any) -> None:
        """ Push an item onto the stack
                Usage:   stack.push(item)
                @:param item to enqueue
                @:return none
                @:raises IndexError if the stack is full
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
    def full(self) -> bool:
        """ Check whether the stack is full
                Usage:   full = stack.full
                @:return full boolean as to whether the stack is full
        """
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        """ Check whether the stack is empty
                Usage:   empty = stack.empty
                @:return empty boolean as to whether the stack is empty
        """
        raise NotImplementedError

    def __eq__(self, other: 'ArrayStack') -> bool:
        """ Equality operator ==
            Usage: stack1 == stack2
            @:param other the instance to compare self to
            @:return true if the stacks are equal (deep check)
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
