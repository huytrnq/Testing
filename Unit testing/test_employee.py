import unittest
import employee

class TestEmployee(unittest.TestCase):
    
    ### setUpClass method is used to run some code before all tests
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    ### tearDownClass method is used to run some code after all tests
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    ### setUp method is used to run some code before each test
    def setUp(self) -> None:
        self.emp_1 = employee.Employee('Corey', 'Schafer', 50000)
        self.emp_2 = employee.Employee('Sue', 'Smith', 60000)
        return super().setUp()
    
    ### tearDown method is used to run some code after each test
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@gmail.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@gmail.com')
        
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
    def test_apply_raise(self):
        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 60000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
if __name__ == '__main__':
    unittest.main()