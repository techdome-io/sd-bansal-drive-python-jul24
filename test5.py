import unittest
from program2 import send_email
from util import clean_string


class TestCase5(unittest.TestCase):

    def test_case_3(self):
        template_code = """
            <html>
              <body>
                {% if first_name %}
                  <h1>Hello, {{first_name}}!</h1>
                {% else %}
                  <h1>Hello, Guest!</h1>
                {% endif %}
                <p>Thank you for registering.</p>
              </body>
            </html>
        """
        context_data = {
            "first_name": "Jane"
        }
        expected_output = """
            <html>
              <body>
                  <h1>Hello, Jane!</h1>
                <p>Thank you for registering.</p>
              </body>
            </html>
        """
        result = send_email(None, 'jane.doe@example.com',
                            context_data, template_code, [])
        self.assertEqual(clean_string(
            result['rendered_html']), clean_string(expected_output))
        print('Test Case 5 Passed')


if __name__ == '__main__':
    unittest.main()
