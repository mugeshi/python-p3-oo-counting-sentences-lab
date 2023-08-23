import re
import pytest
from count_sentences import MyString  # Import the MyString class

class TestMyString:
    def test_is_class(self):
        string = MyString()
        assert isinstance(string, MyString)

    def test_value_string(self):
        string = MyString()
        with pytest.raises(ValueError):
            string.value = 123

    def test_is_sentence(self):
        assert MyString("Hello World.").is_sentence() == True
        assert MyString("Hello World").is_sentence() == False

    def test_is_question(self):
        assert MyString("Is anybody there?").is_question() == True
        assert MyString("Is anybody there").is_question() == False

    def test_is_exclamation(self):
        assert MyString("It's me!").is_exclamation() == True
        assert MyString("It's me").is_exclamation() == False

def test_count_sentences(self):
    simple_string = MyString()
    simple_string.value = "one. two. three?"
    empty_string = MyString()
    complex_string = MyString()
    complex_string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo"
    assert simple_string.count_sentences() == 3
    assert empty_string.count_sentences() == 0
    assert complex_string.count_sentences() == 3

if __name__ == '__main__':
    pytest.main()
    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)