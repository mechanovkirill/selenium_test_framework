import random
import string
import logging

logger = logging.getLogger(__name__)


class DataGenerator:
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    cyrillic_lowercase_letters = "".join([chr(i) for i in range(0x0431, 0x0450)])
    cyrillic_uppercase_letters = "".join([chr(i) for i in range(0x0410, 0x0430)])
    punctuation = string.punctuation
    whitespace = string.whitespace

    @staticmethod
    def _validate_string(string_: str, chars_types_: tuple, min_len: int, max_len: int) -> bool:
        if min_len > len(string_) > max_len:
            return False
        string_ = set(string_)
        d = {chars_types_[i]: False for i in range(len(chars_types_))}
        for char in string_:
            for st in chars_types_:
                if char in st:
                    d[st] = True
                    break
        res = 0
        for val in d.values():
            if not val:
                res += 1
        if res > 0:
            return False
        else:
            return True

    def generate_random_string_with_chosen_char_types(
            self,
            min_len: int = 0,
            max_len: int = 0,
            ascii_lower_letters: bool = False,
            ascii_upper_letters: bool = False,
            digits_: bool = False,
            cyrillic_lower_letters: bool = False,
            cyrillic_upper_letters: bool = False,
            punctuation_: bool = False,
            whitespace_: bool = False
    ) -> str | None:
        """Parameters ascii_lower_letters -...- whitespace_ determine whether characters
        from the corresponding categories will be used. Min and max len define string length.
        WARNING: if len string is less than number of char_types an INVALID string will be returned."""
        if max_len > 0 and 0 < min_len <= max_len:
            string_ = []
            length = random.randint(min_len, max_len)
            params = (ascii_lower_letters, ascii_upper_letters, digits_, cyrillic_lower_letters,
                      cyrillic_upper_letters, punctuation_, whitespace_)
            char_types = (
                self.lowercase_letters, self.uppercase_letters, self.digits,
                self.cyrillic_lowercase_letters, self.cyrillic_uppercase_letters, self.punctuation, self.whitespace,)

            while len(string_) < length:
                for i in range(len(params)):
                    if params[i] is True:
                        string_.append(random.choice(char_types[i]))
                        if len(string_) == length:
                            break

            random.shuffle(string_)

            string_ = "".join(string_)

            return string_
        else:
            logger.error("Can't string generate. Check are given max and min lengths.")

    def get_rand_valid_password_for_a1qa_task(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=25,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
            cyrillic_lower_letters=True
        )
        char_types = (self.lowercase_letters, self.uppercase_letters, self.digits, self.cyrillic_lowercase_letters)
        if self._validate_string(passw, char_types, 10, 25):
            return passw
        else:
            self.get_rand_valid_password_for_a1qa_task()

    def get_rand_valid_email_name(self) -> str:
        e_name = self.generate_random_string_with_chosen_char_types(
            min_len=6,
            max_len=12,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
        )
        char_types = (self.lowercase_letters, self.uppercase_letters)
        if self._validate_string(e_name, char_types, 6, 12):
            return e_name
        else:
            self.get_rand_valid_email_name()

    def get_rand_valid_email_domain(self) -> str:
        e_dom = self.generate_random_string_with_chosen_char_types(
            min_len=2,
            max_len=8,
            ascii_lower_letters=True,
        )
        char_types = (self.lowercase_letters,)
        if self._validate_string(e_dom, char_types, 2, 8):
            return e_dom
        else:
            self.get_rand_valid_email_domain()

    def __get_short_password(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=1,
            max_len=9,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
            cyrillic_lower_letters=True
        )
        return passw

    def __get_password_without_digits(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=25,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            cyrillic_lower_letters=True
        )
        char_types = (self.lowercase_letters, self.uppercase_letters, self.cyrillic_lowercase_letters)
        if self._validate_string(passw, char_types, 10, 25):
            return passw
        else:
            self.__get_password_without_digits()

    def __get_password_without_upper(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=25,
            ascii_lower_letters=True,
            digits_=True,
            cyrillic_lower_letters=True
        )
        char_types = (self.lowercase_letters, self.digits, self.cyrillic_lowercase_letters)
        if self._validate_string(passw, char_types, 10, 25):
            return passw
        else:
            self.__get_password_without_upper()

    def __get_password_without_cyrillic(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=25,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
        )
        char_types = (self.lowercase_letters, self.uppercase_letters, self.digits)
        if self._validate_string(passw, char_types, 10, 25):
            return passw
        else:
            self.__get_password_without_cyrillic()

    def get_list_of_invalid_rand_passwords(self) -> list[str]:
        return [
            "",
            "           ",
            self.__get_short_password(),
            self.__get_password_without_digits(),
            self.__get_password_without_upper(),
            self.__get_password_without_cyrillic(),
            self.get_rand_valid_password_for_a1qa_task(),
        ]
