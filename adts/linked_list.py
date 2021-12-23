from typing import Any

from adts.list_node import ListNode


class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on ListNode class to store the items, previous, and next nodes.
            Stipulations:
            1. Must manage the linked list using only two ListNode objects (_head and _tail)
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, instance: 'LinkedList' =None) -> None:
        """ Constructor for the LinkedList
            Usage:  linked_list = LinkedList()
            @:param instance an optional instance of a LinkedList to deep copy from
            @:return none
            @:raises TypeError if instance is provided and it is not a LinkedList instance
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'LinkedList') -> 'LinkedList':
        """ Clone the LinkedList
            Usage:  new_linked_list = LinkedList.clone(instance)
            @:param instance a LinkedList instance to deep copy data from.
            @:return a deep object copy of the linked list
            @:raises TypeError if instance is provided and it is not an LinkedList instance
        """
        raise NotImplementedError

    def append(self, item: Any) -> None:
        """ Append an item to the end of the list
            Usage: linked_list.append(item)
            @:param item the desired item to append to the linked list
            @:return none
        """
        raise NotImplementedError

    def prepend(self, item: Any) -> None:
        """ Prepend an item to the end of the list
            Usage: linked_list.prepend(item)
            @:param item the desired item to prepend to the linked list
            @:return none
        """
        raise NotImplementedError

    def insert_before(self, before_item: Any, new_item: Any) -> None:
        """ Insert a new item before a specified item
            Usage: linked_list.insert_before(before_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        raise NotImplementedError

    def insert_after(self, after_item: Any, new_item: Any) -> None:
        """ Insert a new item after a specified item
            Usage: linked_list.insert_after(after_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        raise NotImplementedError

    @property
    def head(self) -> ListNode:
        """ Return the ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: head = linked_list.head
            @:return head the ListNode instance representing the head of the linked list
        """
        raise NotImplementedError

    @property
    def tail(self) -> ListNode:
        """ Return the ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: tail = linked_list.tail
            @:return tail the ListNode instance representing the tail of the linked list
        """
        raise NotImplementedError

    @property
    def first(self) -> Any:
        """ Return the item at the head of the linked list.
            Usage: first_item = linked_list.first
            @:return first the item stored in the head of the list
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    @property
    def last(self) -> Any:
        """ Return the item at the tail of the linked list.
            Usage: last_item = linked_list.last
            @:return last the item stored in the tail of the list
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the linked list
            Usage: linked_list.clear():
            @:return none
        """
        raise NotImplementedError

    def extract(self, item: Any) -> None:
        """ Extract an item from the Linked List
            @:param item the item to remove
            @:return: None
            @:raises: KeyError if the item is not found
        """
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        """ Property to determine whether the list is empty
            @:return bool whether the list is empty
        """
        raise NotImplementedError

    def remove_first(self) -> None:
        """ Remove the first item in the linked list
            Usage: linked_list.remove_first()
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    def remove_last(self) -> None:
        """ Remove the last item in the linked list
            Usage: linked_list.remove_last()
            @:raises IndexError if the list is empty
        """
        raise NotImplementedError

    def __contains__(self, item: Any) -> bool:
        """ Equality operator ==
            Usage: if item in linked_list:
            @:param item the item to search for
            @:return true if the linked list contains the item
        """
        raise NotImplementedError

    def __eq__(self, other: 'LinkedList') -> bool:
        """ Equality operator ==
            Usage: list1 == list2
            @:param other the instance to compare self to
            @:return true if the lists are equal (deep check)
        """
        raise NotImplementedError

    def __iter__(self) -> Any:
        """ Iterator operator
            Usage: for item in LinkedList:
            @:return yields the item at ListNode
        """
        raise NotImplementedError

    def __reversed__(self) -> Any:
        """ Reversed iterator operator
            Usage: for item in reversed(list):
            @:return yields the item at ListNode
        """
    raise NotImplementedError

    def __len__(self) -> int:
        """ len operator for getting length of the linked list
            Usage: size = len(linked_list)
            @:return the length of the LinkedList
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(linked_list):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
