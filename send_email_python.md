# Email Sending Function Assignment

## Introduction

In this assignment, you are required to create a function in JavaScript that simulates the process of sending an email. This includes rendering an HTML template with context variables, creating a mock message object, and handling attachments. Since this is a simulated environment, you do not need to use real email services.

## Task

You must implement a function `sendEmail` that adheres to the following specifications:

### Function Signature

```python
def send_email(db, recipient_email, context_data, template_code, file_paths):
    """
    Calls send email service (simulated)

    :param db: Session variable (not used in the current scope, but consider it exists)
    :param recipient_email: Email address of the recipient
    :param context_data: Dictionary containing variables to be used in the template.
                         E.g., if the template has {{first_name}} and the dictionary has 'first_name',
                         then it should be replaced in the output.
    :param template_code: HTML template code
    :param file_paths: Local paths of attachments
    :return: A dictionary containing the simulated message details
    """
    # Implement your function here
```

### Steps to Implement

1. **Replace Template Variables**:

   - Parse the `templateCode` and replace any placeholders (e.g., `{{first_name}}`) with the corresponding values from `contextData`.

2. **Create Mock Message**:

   - Build a mock message object that includes the recipient email, rendered HTML, and a list of attachments.

3. **Return the Mock Message**:
   - The function should return this mock message object as a dictionary.

### Example HTML Template with Context

**Template Code:**

```html
<html>
  <body>
    <h1>Hello, {{first_name}} {{last_name}}!</h1>
    <p>Thank you for registering with {{company}}.</p>
  </body>
</html>
```

**Context Data:**

```javascript
{
    first_name: 'John',
    last_name: 'Doe',
    company: 'Tech Co.'
}
```

**Expected Output HTML:**

```html
<html>
  <body>
    <h1>Hello, John Doe!</h1>
    <p>Thank you for registering with Tech Co.</p>
  </body>
</html>
```

**Mock Message Object:**

```javascript
{
    recipientEmail: 'john.doe@example.com',
    renderedHtml: '<html><body><h1>Hello, John Doe!</h1><p>Thank you for registering with Tech Co.</p></body></html>',
    attachments: ['path/to/attachment1.jpg', 'path/to/attachment2.pdf']
}
```

## Bonus Points

1. **Error Handling (2 points)**

   - Implement robust error handling for various scenarios such as:
     - Missing required context variables.
     - Non-existent file paths.
   - Ensure that meaningful error messages are returned or logged.

2. **Template Engine (3 points)**

   - Implement a simple template engine to support more advanced templating features such as loops and conditionals.
   - E.g., `{% if first_name %}Hello, {{first_name}}{% else %}Hello, Guest{% endif %}`.

3. **Code Documentation (2 points)**

   - Provide detailed JSDoc comments for the function, and inline comments explaining complex logic.
   - Maintain a separate README file explaining the function's purpose, usage, and example scenarios.

4. **Email Validation (2 points)**

   - Implement email validation logic to ensure that the provided email addresses are correctly formatted.
   - Utilize regular expressions or use a third-party validation library.

5. **Attachment Validation (2 points)**

   - Verify that the file paths provided actually exist and that the files are accessible.
   - Handle and report issues with inaccessible files.

6. **Logging (2 points)**

   - Integrate logging to track the functioning of the `sendEmail` function.
   - Log message details along with timestamps, error messages, and processing duration.

7. **Performance Optimization (3 points)**
   - Optimize the function for performance, especially in how it processes and renders the templates.
   - Avoid redundant computations and optimize string operations.

## Submission

Please submit your function implementation with error handling, and supporting comments. Ensure your code is well-documented and follows best practices.

Good luck!
