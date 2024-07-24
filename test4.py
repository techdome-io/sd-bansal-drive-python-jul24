import unittest
from program2 import send_email


class TestCase4(unittest.TestCase):

    def test_case_5(self):
        template_code = '<html><body>Test</body></html>'
        context_data = {}
        with self.assertRaises(FileNotFoundError) as context:
            send_email(None, 'john.doe@example.com', context_data,
                       template_code, ['/invalid/path.jpg'])
        self.assertEqual(str(context.exception),
                         'Attachment file not found: /invalid/path.jpg')
        print('Test Case 4 Passed')


if __name__ == '__main__':
    unittest.main()
