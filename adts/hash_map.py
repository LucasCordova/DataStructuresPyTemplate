from typing import Any


class HashMap:
    """ Class HashMap - representing a HashMap (dictionary) where the
        buckets are based on an Array and the chains are based on LinkedLists
            Stipulations:
            1. Must use an Array<LinkedList<Pair>> as the internal data structure from the
               Array, LinkedList and Pair assignments.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, max_size: int, hash_function) -> None:
        """ Constructor
            Usage:  hash_map = hash_map(23, hash_function)
            @:param max_size the desired max size of the HashMap
            @:param hash_function the desired hash function
            @:return none
        """
        raise NotImplementedError

    @staticmethod
    def clone(instance: 'HashMap') -> 'HashMap':
        """ Clone the hash map
            Usage:  hash_map = HashMap.clone(instance)
            @:param instance an HashMap instance to deep copy data from.
            @:return a deep object copy of the hash map
            @:raises TypeError if instance is provided and it is not an HashMap instance
        """
        raise NotImplementedError

    def __getitem__(self, key: Any) -> Any:
        """ Bracket operator for getting an item value
            Usage: item = array[key]
            @:param key the key of the desired value
            @:return the item value associated with the key
            @:raises KeyError if the key is not present in the hashmap
        """
        raise NotImplementedError

    def __setitem__(self, key: Any, value: Any) -> None:
        """ Bracket operator for inserting a key/value pair into the hash map
            Usage: hash_map[key] = val
            @:param key the desired key set
            @:param value the value associated with the key
            @:raises KeyError if key is already present in the hash map
            @:return none
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """ len operator for getting size of the hash map (number of key/value pairs)
            Usage: length = len(hash_map)
            @:return the size of the hash map
        """
        raise NotImplementedError

    def resize(self, new_table_size: int, new_hash_function) -> None:
        """ Rehash a hash map
            Usage: hash_map.rehash(new_table_size, new_hash_function)
            @:param new_table_size the desired new table size
            @:param new_hash_function the desired new hash function
            @:return none
        """
        raise NotImplementedError

    def __eq__(self, other: 'HashMap') -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        raise NotImplementedError

    def __iter__(self):
        """ Iterator operator
            Usage: for key, value in hash_map:
            @:return yields the key at the index
            @:return yields the value at the index
        """
        raise NotImplementedError

    def __delitem__(self, key: Any) -> None:
        """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
            Usage: del hash_map[key]
            @:param key the desired key to delete
            @:return none
            @:raises KeyError if the key is not found
        """
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        """ Contains operator (in)
            Usage: if 3 in hash_map:
            @:param key the desired key to check whether it's in the hash_map
            @:return true if the hash_map contains the key
        """
        raise NotImplementedError

    def clear(self) -> None:
        """ Clear the hash map
            Usage: hash_map.clear():
            @:return none
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(hash_map):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError

    def keys(self) -> list:
        """ Returns a view object. The view object contains the keys of the dictionary, as a list.
            Usage: keys = hash_map.keys()
            @:return list a list containing the keys of the dictionary
        """
        raise NotImplementedError

    def values(self) -> list:
        """ Returns a view object. The view object contains the values of the dictionary, as a list.
            Usage: values = hash_map.values()
            @:return list a list containing the values of the dictionary
        """
        raise NotImplementedError

    def items(self) -> list:
        """ Returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
            Usage: items = hash_map.items()
            @:return items as a tuples in a list of the key/value pairs of the dictionary
        """
        raise NotImplementedError
