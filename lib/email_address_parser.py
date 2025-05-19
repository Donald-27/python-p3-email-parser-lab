# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Split input string by commas or spaces
        parts = re.split(r'[,\s]+', self.emails.strip())

        # Regex pattern to match valid emails (basic validation)
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        # Filter only valid emails, remove duplicates, then sort
        valid_emails = set(filter(email_pattern.match, parts))
        return sorted(valid_emails)
