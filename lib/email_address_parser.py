
import re

class EmailAddressParser:
    """
    Given a string of email addresses separated by commas and/or spaces,
    parse them into a unique, alphabetically sorted list.
    """

    # A light-weight email pattern suitable for this lab
    _EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self, addresses: str):
        # Guard against None and ensure we always have a string
        self.addresses = addresses or ""

    def parse(self):
        """
        Return a list of unique email addresses (alphabetically sorted).
        Handles commas, spaces, or any mix of the two as separators.
        Filters out tokens that don't look like emails.
        """
        # Split on any run of commas and/or whitespace
        tokens = re.split(r"[,\s]+", self.addresses.strip())

        # Keep only non-empty tokens that look like emails
        emails = [t for t in tokens if t and self._EMAIL_PATTERN.match(t)]

        # Uniqueness + alphabetical sort
        return sorted(set(emails))
