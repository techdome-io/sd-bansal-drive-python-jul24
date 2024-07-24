import unittest
from program2 import send_email


class TestCase3(unittest.TestCase):

    def test_case_4(self):
        with self.assertRaises(ValueError) as context:
            send_email(None, 'invalid-email', {}, '', [])
        self.assertEqual(str(context.exception), 'Invalid email address')
        print('Test Case 3 Passed')


if __name__ == '__main__':
    unittest.main()
