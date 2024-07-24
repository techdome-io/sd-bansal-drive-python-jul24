import unittest
import re
import tempfile
from contextlib import contextmanager
from program2 import send_email


def clean_string(s):
    return re.sub(r'\s+', '', s)


class TestSendEmail(unittest.TestCase):

    def test_case_1(self):
        # Simple Template Rendering
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

    def test_case_2(self):
        # Missing Context Variable
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
            "company": "Techdome"
        }
        expected_output = """
            <html>
              <body>
                <h1>Hello, John {{last_name}}!</h1>
                <p>Thank you for registering with Techdome.</p>
              </body>
            </html>
        """
        result = send_email(None, 'john.doe@example.com',
                            context_data, template_code, [])
        self.assertEqual(clean_string(
            result['rendered_html']), clean_string(expected_output))
        print('Test Case 2 Passed')

    def test_case_3(self):
        # Complex Template with Conditionals
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
        print('Test Case 3 Passed')

    def test_case_4(self):
        # Email Validation
        with self.assertRaises(ValueError) as context:
            send_email(None, 'invalid-email', {}, '', [])
        self.assertEqual(str(context.exception), 'Invalid email address')
        print('Test Case 4 Passed')

    def test_case_5(self):
        # Attachment Validation
        template_code = '<html><body>Test</body></html>'
        context_data = {}
        with self.assertRaises(FileNotFoundError) as context:
            send_email(None, 'john.doe@example.com', context_data,
                       template_code, ['/invalid/path.jpg'])
        self.assertEqual(str(context.exception),
                         'Attachment file not found: /invalid/path.jpg')
        print('Test Case 5 Passed')

    def test_case_6(self):
        # Advanced Templating with Loop
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


if __name__ == "__main__":
    unittest.main()
