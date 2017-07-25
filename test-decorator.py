import unittest
#from emp import Employee 
import mock
from mock import patch
 
class Employee:
    ''' Creating Class Variables '''
    
    #class variables and instance vairable 
    num_of_emp = 0 
    raise_amt  = 1.04
     
    def __init__(self , fname, lname, pay):
        ''' Constructor of employee ''' 
        self.fname = fname
        self.lname = lname 
        self.pay   = pay
        self.email = fname + '.' + lname + '@company.com'
        #class vairable 
        Employee.num_of_emp += 1 
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.pay = self.pay + self.raise_amt
    
    #Class Method , use cls and de-corator  for creating class methods  
    @classmethod
    def set_raise_amt(cls , amount):
        cls.raise_amt = amount
        
class Emptest(unittest.TestCase,Employee):
    
    def setUp(self):        
        pass
    
    def tearDown(self):
        pass 
    
    @mock.patch('Employee.fullname')
    def test_empName(self, fullname):
        fullname.return_value  = mock.MagicMock()
        return '{} {}'.format('anil', 'gautam')
     
    
def isPrime(number):
    if number < 0 or number in (0,1):
        return False
    
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

class Primetest(unittest.TestCase):
    
    def test_Primes(self):
        self.assertTrue(isPrime(5))
        
class OtherTest(unittest.TestCase):
            
    def test_isTrue(self):
        self.assertTrue(True)
        
def test_Suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Primetest))
    suite.addTest(unittest.makeSuite(OtherTest))
    suite.addTest(unittest.makeSuite(Emptest))
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='test_Suit')
    
