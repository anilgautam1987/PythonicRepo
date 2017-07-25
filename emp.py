
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
        

#No of employee zero 
print(Employee.num_of_emp)

        
emp1 = Employee('Anil' , 'Gautam' , 50000 )
#Instance Variable
#emp1.raise_amt = 1.05 
emp2 = Employee('Naveen' , 'Narayana Appa' , 60000 )

#Class Method changes the complete value
Employee.set_raise_amt(1.06)

''' Session 1 : Difference Between Class Variable and Instance Variable '''  
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.num_of_emp)

''' Session 2 : Difference Between Regular Method,Class Method and Static Method
    - Class method is used to change the class properties globally 
    - Class Method can be used as alternative Constructor 
''' 
#Employee.set_raise_amt(1.06)
#emp1.set_raise_amt(1.06)




