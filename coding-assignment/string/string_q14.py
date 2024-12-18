Question: Check if an email address is valid using regex.

import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
