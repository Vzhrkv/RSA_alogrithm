import unittest

from task1.main_algorithms import euclid_algo, expanded_euclid_algo, calculate_euler_function, get_prime_number


class TestEuclidAlgorithm(unittest.TestCase):
    """Test for Euclid's algorithm to find GCD"""

    def test_euclid_algo(self):
        """Test numbers input values"""
        self.assertEqual(euclid_algo(31, 13), 1)
        self.assertEqual(euclid_algo(77, 11), 11)
        self.assertEqual(euclid_algo(120, 18), 6)

    def test_euclid_algo_with_floats(self):
        """Test when one or two numbers are floats"""
        # self.assertRaises()
        pass

    def test_euclid_algo_with_big_numbers(self):
        self.assertEqual(euclid_algo(2 << 129, 2 << 128), 680564733841876926926749214863536422912)


class TestExpandedEuclidAlgorithm(unittest.TestCase):
    """Test for expanded Euclid's algorithm to find GCD, s and t"""

    def test_expanded_euclid_algorithm(self):
        """test for two numbers"""
        self.assertEqual(expanded_euclid_algo(7, 76), (1, 11, 6))
        self.assertEqual(expanded_euclid_algo(4, 62), (2, -15, 1))


class TestEulerFunction(unittest.TestCase):
    """Test Euler's function for two numbers"""

    def test_euler_function_calc(self):
        """Test for two natural numbers"""
        self.assertEqual(calculate_euler_function(11, 7), 60)
        self.assertEqual(calculate_euler_function(75, 3), 148)


class TestPrimeNumberGetter(unittest.TestCase):
    """Test for get prime number function"""

    def test_get_prime_number(self):
        """Test for small integers"""
        self.assertEqual(get_prime_number(13, 15, 17), 89)
        self.assertEqual(get_prime_number(13, 14, 17), 101)

    def test_get_prime_number_for_big_ints(self):
        """Test for big integers"""
        self.assertEqual(get_prime_number(2341583687, 3951112667, 257), 4283935619728305285)
        self.assertEqual(get_prime_number(3375782533, 3655398443, 65537), 12023882955474050681)
