import unittest
from program2 import send_email
from util import clean_string


class TestCase1(unittest.TestCase):

    def test_case_1(self):
        template_code = """
            <html>
              <body>
                <h1>Hello, {{first_name}} {{last_name}}!</h1>
                <p>Thank you for registering with {{company}}.</p>
              </body>
            </html>
        """
        context_data = {
            "first_name": "John",
            "last_name": "Doe",
            "company": "Techdome"
        }
        expected_output = """
            <html>
              <body>
                <h1>Hello, John Doe!</h1>
                <p>Thank you for registering with Techdome.</p>
              </body>
            </html>
        """
        result = send_email(None, 'john.doe@example.com',
                            context_data, template_code, [])
        self.assertEqual(clean_string(
            result['rendered_html']), clean_string(expected_output))
        print('Test Case 1 Passed')


if __name__ == '__main__':
    unittest.main()
