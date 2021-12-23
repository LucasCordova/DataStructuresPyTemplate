from typing import Any


class CircularArrayQueue:
    """ Class CircularArrayQueue - representing a circular array queue using a 1D Array
            Stipulations:
            1. Must use an Array object as the internal data structure.
            2. Storage must wrap-around the array.
            3. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            4. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, max_size: int = 0, instance: 'CircularArrayQueue' = None) -> None:
        """ Constructor
            Usage:  queue = CircularArrayQueue(10)
            @:param size the desired size of the queue
            @:param instance an optional CircularArrayQueue instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an CircularArrayQueue instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'CircularArrayQueue') -> 'CircularArrayQueue':
        """ Clone the queue
            Usage:  queue = CircularArrayQueue.clone(instance)
            @:param instance an CircularArrayQueue instance to deep copy data from.
            @:return a deep object copy of the queue
            @:raises TypeError if instance is provided and it is not an CircularArrayQueue instance
        """
        raise NotImplementedError

    def enqueue(self, item: Any) -> None:
        """ Enqueue an item onto the queue
            Usage:   queue.enqueue(item)
            @:param item to enqueue
            @:return none
            @:raises IndexError if the queue is full
        """
        raise NotImplementedError

    def dequeue(self) -> Any:
        """ Dequeue an item from the queue and return the item
            Usage:   item = queue.dequeue()
            @:return item that is dequeued
            @:raises IndexError if the queue is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the queue
            Usage: array_queue.clear():
            @:return none
        """
        raise NotImplementedError

    @property
    def front(self) -> Any:
        """ Get the item at the front of the queue
            Usage:   item = queue.front
            @:return item that is in the front
            @:raises IndexError if the queue is empty
        """
        raise NotImplementedError

    @property
    def full(self) -> bool:
        """ Check whether the queue is full
            Usage:   full = queue.full
            @:return full boolean as to whether the queue is full
        """
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        """ Check whether the queue is empty
            Usage:   empty = queue.empty
            @:return empty boolean as to whether the queue is empty
        """
        raise NotImplementedError

    def __eq__(self, other: 'CircularArrayQueue') -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """ len operator for getting length of the queue
            Usage: length = len(queue)
            @:return the length of the Queue (number of items on the queue)
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(queue):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
