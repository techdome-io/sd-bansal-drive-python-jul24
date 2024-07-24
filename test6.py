import unittest
from program2 import send_email
from util import clean_string


class TestCase6(unittest.TestCase):

    def test_case_6(self):
        template_code = """
            <html>
              <body>
                <h1>Shopping List:</h1>
                <ul>
                  {% for item in items %}
                    <li>{{item}}</li>
                  {% endfor %}
                </ul>
              </body>
            </html>
        """
        context_data = {
            "items": ["Milk", "Bread", "Eggs"]
        }
        expected_output = """
            <html>
              <body>
                <h1>Shopping List:</h1>
                <ul>
                    <li>Milk</li>
                    <li>Bread</li>
                    <li>Eggs</li>
                </ul>
              </body>
            </html>
        """
        result = send_email(None, 'john.doe@example.com',
                            context_data, template_code, [])
        self.assertEqual(clean_string(
            result['rendered_html']), clean_string(expected_output))
        print('Test Case 6 Passed')


if __name__ == '__main__':
    unittest.main()
