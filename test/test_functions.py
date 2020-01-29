import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        input_age_in_years = 10
        expected_age_in_months = 120
        self.assertEqual(expected_age_in_months, camper_age_input.convert_to_months(input_age_in_years))
        print('we passed age unit test first time')
        input_age_in_years = 3
        expected_age_in_months = 36
        self.assertNotEqual(expected_age_in_months, camper_age_input.convert_to_months(input_age_in_years))
        print('we passed age unit test')


if __name__ == '__main__':
    unittest.main()
