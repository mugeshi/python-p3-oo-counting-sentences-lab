import re  # Import the 're' module here

class MyString:
    def __init__(self, initial_value=""):
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
