import unittest

def is_prime(number):
    if number < 0 or number in (0, 1):
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

class PrimesTests(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-6))
        
class OtherTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
        
def test_suite():
    """builds the test suite."""
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(PrimesTests))
    suite.addTests(unittest.makeSuite(OtherTests))
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
