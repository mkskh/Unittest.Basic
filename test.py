import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

    # TASK 1
    # check if the specific value equals random value
    def test_value_equals(self):
        '''
        (Task 3)
        potential issues: if the test has passed once, it doesn't means that the test will be passed again.
        Because of random module our chance to pass the test is 1:19.
        '''
        self.assertEqual(rnd(2, 20), 5) # for example 5

    # TASK 2
    # check if the random value in required range
    def test_value_range(self):
        '''
        (Task 3)
        There're no potential issues. We check a range here, not a specific number.
        '''

        # Option 1
        # random_number = rnd(2, 20)
        # in_range = random_number in range(2,20 + 1)
        # self.assertTrue(in_range == True)

        # Option 2
        self.assertIn(rnd(2, 20), range(2, 20 + 1))

if __name__ == '__main__':
    unittest.main()