import unittest
from unittest import mock
from tests_simple_employee import Employee


class TestSimpleEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Doctor', 'Who', 2000)

    def test_instance(self):
        self.assertIsInstance(self.employee, Employee)

    def test_email(self):
        self.assertEqual(self.employee.email, 'Doctor.Who@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Doctor Who')

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertIsInstance(self.employee.pay, int)
        self.assertEqual(self.employee.pay, 2100)

    def test_monthly_schedule_func_bad_requests(self):
        with mock.patch('tests_simple_employee.requests.get') as response:
            response.return_value.ok = 0
        self.assertEqual(Employee.monthly_schedule(self.employee, 'November'), 'Bad Response!')

    def test_monthly_schedule_func_good_requests(self):
        with mock.patch('tests_simple_employee.requests.get') as response:
            response.return_value.ok = 200
            response.return_value.text = 'Info'
            result = self.employee.monthly_schedule('June')
        self.assertEqual(result, 'Info')


if __name__ == '__main__':
    unittest.main()
