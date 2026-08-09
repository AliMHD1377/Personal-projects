# به نام خدا

import random
from abc import ABC, abstractmethod
import nltk
import string

nltk.download("words")


class PasswordGenerator(ABC):
    """
    کلاس پایه برای تولید رمزهای عبور
    """
    @abstractmethod
    def generate(self) -> str:
        """
        زیرکلاس‌ها باید این متد را برای تولید رمز عبور بازنویسی کنند
        """
        pass


class PinCodeGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self):
        return "".join(random.choices(string.digits, k=self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, no_of_words: int = 4, separator="-", capitalize=False, vocabulary=None):
        self.no_of_words = no_of_words
        self.separator = separator
        self.capitalize = capitalize
        self.vocabulary = vocabulary

        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()

    def generate(self):
        selected = random.choices(self.vocabulary, k=self.no_of_words)
        
        if self.capitalize:
            selected = [w.capitalize() for w in selected]
            
        return self.separator.join(selected)


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, numbers=False, symbols=False):
        self.length = length
        self.characters: str = string.ascii_letters
        if numbers:
            self.characters += string.digits
        if symbols:
            self.characters += string.punctuation

    def generate(self):
        return "".join(random.choices(self.characters, k=self.length))


if __name__ == "__main__":
    pin_gen = PinCodeGenerator(5)
    print(pin_gen.generate())

    random_gen = RandomPasswordGenerator(numbers=True, symbols=True)
    print(random_gen.generate())
    
    mem_gen = MemorablePasswordGenerator(capitalize=True)
    print(mem_gen.generate())
