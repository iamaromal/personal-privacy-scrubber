import re

class PIIScrubber:
    def __init__(self):
        self.patterns = {
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'phone': r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b'
        }

    def scrub(self, text):
        scrubbed = text
        for pii_type, pattern in self.patterns.items():
            scrubbed = re.sub(pattern, f'[{pii_type.upper()}_REDACTED]', scrubbed)
        return scrubbed

if __name__ == "__main__":
    scrubber = PIIScrubber()
    sample = "Contact John Doe at john.doe@example.com or call 555-123-4567. SSN: 000-12-3456."
    print("Original:", sample)
    print("Scrubbed:", scrubber.scrub(sample))
