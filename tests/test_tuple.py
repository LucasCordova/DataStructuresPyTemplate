import unittest
from adts.tuple import Tuple

class TupleTest(unittest.TestCase):
    
    def test_01_init_with_standard_input_stores_what_is_expected(self):
        #Arrange & Act
        example_tuple = Tuple(1,2,3)

        #Assert
        assert example_tuple._items == (1,2,3)

    def test_02_init_with_nonstandard_input(self):
        #Arrange & Act
        tuple_data = (1,2,3,4)
        example_tuple = Tuple(tuple_data)

        #Assert
        assert example_tuple._items == tuple_data

    def test_03_clone_with_valid_instance(self):
        #Arrange & Act
        example_tuple = Tuple(1,2,3)
        clone = Tuple.clone(example_tuple)
        #Assert
        assert example_tuple.data == clone.data

    def test_04_clone_with_invalid_instance(self):
        #Arrange & Act
        non_example_tuple = 'This is a string'
        
        #Assert
        with self.assertRaises(TypeError):
            Tuple.clone(non_example_tuple)
            
    def setUp(self):
        pass

    def test_template(self):
        """
        Test description
        """

        # Arrange

        # Act

        # Assert

        pass


if __name__ == '__main__':
    unittest.main()
