from typing import Any


class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on LinkedList._ListNode class to store the items, previous, and next nodes.
            Stipulations:
            1. Must manage the linked list using only two LinkedList._ListNode objects (_head and _tail)
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. The LinkedList can contain duplicate items.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    class _Node:
        """ _LinkedList._ListNode - private class that represents a node in a linked list
                Stipulations:
                1. Must adhere to the docstring requirements per method, including raising
                raising appropriate exceptions where indicated.
        """

        def __init__(self, item, previous_node: 'LinkedList._Node' = None, next_node: 'LinkedList._Node' = None) -> None:
            """ Constructor - represents a row in the 2D array
                Usage:  node = _Node() or node = _Node(None, None) or node = _Node(previous_node, next_node)
                @:param item the item (data) to store in the node
                @:param previous_node the corresponding previous node of this node in the linked list
                @:param next_node the corresponding next node of this node in the linked list
                @:return none
            """
            raise NotImplementedError


        @property
        def item(self) -> Any:
            """ Getter for the item
                Usage: item = node.item
                @:return the item stored in the node
            """
            raise NotImplementedError

        @item.setter
        def item(self, item: Any) -> None:
            """ Setter for the item
                Usage: node.item = item
                @:param item the item to store in the node
                @:return none
            """
            raise NotImplementedError

        @property
        def previous(self) -> 'LinkedList._ListNode':
            """ Getter for the previous node
                Usage: previous_node = node.previous
                @:return the previous node of the node
            """
            raise NotImplementedError


        @previous.setter
        def previous(self, previous_node: 'LinkedList._Node') -> None:
            """ Setter for the previous node
                Usage: node.previous = previous
                @:param previous_node the node's previous_node instance
                @:return none
            """
            raise NotImplementedError

        @property
        def next(self) -> 'LinkedList._ListNode':
            """ Getter for the next node
                Usage: next_node = node.next
                @:return the next node of the node
            """
            raise NotImplementedError

        @next.setter
        def next(self, next_node: 'LinkedList._Node') -> None:
            """ Setter for the next node
                Usage: node.next = next_node
                @:param previous_node the node's previous_node instance
                @:return none
            """
            raise NotImplementedError

        def __eq__(self, other: 'LinkedList._Node') -> bool:
            """ Equality operator ==
                Usage: array1 == array2
                @:param other the instance to compare self to
                @:return true if the arrays are equal (deep check)
            """
            raise NotImplementedError


        def __str__(self) -> str:
            """ Return a string representation of the data and structure
                Usage: print(node):
                @:return str the string representation of the data and structure
            """
            raise NotImplementedError

    def __init__(self, python_list_instance: list = None) -> None:
        """ Constructor for the LinkedList
            Usage:  1. linked_list = LinkedList()
                    2. linked_list = LinkedList(['This', 'is', 'a', 'Python', 'list'])
            @:return none
            @:raises TypeError if optional python_list_instance provided is not a list
        """
        raise NotImplementedError


    @classmethod
    def clone(cls, linked_list_instance: 'LinkedList') -> 'LinkedList':
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

    
    def insert_at_index(self, index: int, new_item: Any) -> None:
        """ Insert an item at a specified index. The item currently at that index 
            should move to the right of the new item.
            Usage: linked_list.insert_at(5, new_item)
            @:param index the index that the user wishes to the new item
            @:param new_item the desired item to insert
            @:return none
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError


    def __getitem__(self, index: int) -> Any:
        """ Bracket operator for getting an item
            Usage: val = linked_list[0]
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        raise NotImplementedError


    def __setitem__(self, index: int, item: Any) -> None:
        """ Bracket operator for setting an item
            Usage: linked_list[index] = val
            @:param index the desired index to set
            @:param item the desired item to set at index
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        raise NotImplementedError


    @property
    def head(self) -> 'LinkedList._Node':
        """ Return the LinkedList._ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: head = linked_list.head
            @:return head the LinkedList._ListNode instance representing the head of the linked list
        """
        raise NotImplementedError

    @property
    def tail(self) -> 'LinkedList._ListNode':
        """ Return the LinkedList._ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: tail = linked_list.tail
            @:return tail the LinkedList._ListNode instance representing the tail of the linked list
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

    
    def extract_all(self, item: Any) -> None:
        """ Extract all instances of an item from the Linked List
            @:param item the item to remove
            @:return: None
            @:raises: KeyError if at least one instance of the item is not found
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
            Usage: for item in list:
            @:return yields the item at LinkedList._ListNode
        """
        raise NotImplementedError


    def __reversed__(self) -> Any:
        """ Reversed iterator operator
            Usage: for item in reversed(list):
            @:return yields the item at LinkedList._ListNode
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

