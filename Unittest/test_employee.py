import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    """si ejecutamos este test con python -m unittest test_employee podemos observera
    que los metodos se ejecutar en el orden en  el cual se escriben en este archivo"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print("setup")
        "cuando se crea el objeto employe se crea un email por defecto nombre.last@gmail.com"
        self.emp_1 = Employee("rene", "jalvin", 4000)
        self.emp_2 = Employee("beimar", "jal", 40000)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'rene.jalvin@gmail.com')
        self.assertEqual(self.emp_2.email, 'beimar.jal@gmail.com')

        self.emp_1.first = 'pedro'
        self.emp_2.first = 'juan'

        self.assertEqual(self.emp_1.email, 'pedro.jalvin@gmail.com')
        self.assertEqual(self.emp_2.email, 'juan.jal@gmail.com')
    
    def test_fullname(self):
        print("test fullname")
        self.assertEqual(self.emp_1.fullname, "rene jalvin")
        self.assertEqual(self.emp_2.fullname, "beimar jal")

        self.emp_1.first = "pedro"
        self.emp_2.first = "carlos"

        self.assertEqual(self.emp_1.fullname,'pedro jalvin')
        self.assertEqual(self.emp_2.fullname,'carlos jal')
    
    def test_apply_raise(self):
        print("test_apply raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 4200)
        self.assertEqual(self.emp_2.pay, 42000)
    
    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mock_request_get:
            mock_request_get.return_value.ok = True
            mock_request_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            print("rene", schedule)
            mock_request_get.assert_called_with('http://company.com/jalvin/May')
            self.assertEqual(schedule, 'Success')
            
            mock_request_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mock_request_get.assert_called_with('http://company.com/jal/June')
            self.assertEqual(schedule, 'Bad Response')
            
    
    def tearDown(self):
        print('tearDown\n')

    @classmethod
    def tearDownClass(cls):
        print("teardowclass")

        

