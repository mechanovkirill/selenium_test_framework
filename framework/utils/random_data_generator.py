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
    def _calc(value):
        res = 0
        if value is True:
            res += 1
        return res

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
        from the corresponding categories will be used. Min and max len define string length."""
        if max_len > 0 and 0 < min_len <= max_len:
            string_ = []
            length = random.randint(min_len, max_len)
            params_number = 0
            params = (ascii_lower_letters, ascii_upper_letters, digits_, cyrillic_lower_letters,
                      cyrillic_upper_letters, punctuation_, whitespace_)
            char_types = (
                self.lowercase_letters, self.uppercase_letters, self.digits,
                self.cyrillic_lowercase_letters, self.cyrillic_uppercase_letters, self.punctuation, self.whitespace,)
            for i in params:
                params_number += self._calc(i)
            k = round(length / params_number)
            if k == 0:
                k = 1
            for n in range(len(params)):
                if params[n] is True:
                    string_.extend(random.choices(char_types[n], k=k))

            random.shuffle(string_)

            while min_len > len(string_) or len(string_) > max_len:
                if len(string_) > max_len:
                    string_.pop(0)
                if len(string_) < min_len:
                    string_.append(random.choice(string_))

            string_ = "".join(string_)

            return string_
        else:
            logger.error("Can't string generate. Check are given max and min lengths.")

    def get_rand_valid_password(self, min_len: int = 8, max_len: int = 18) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=min_len,
            max_len=max_len,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
        )
        return passw

    def get_rand_valid_passw_for_a1qa_task(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=25,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
            cyrillic_lower_letters=True
        )
        return passw

    def get_rand_valid_email_name(self) -> str:
        e_name = self.generate_random_string_with_chosen_char_types(
            min_len=6,
            max_len=12,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
        )
        return e_name

    def get_rand_valid_email_domain(self) -> str:
        e_dom = self.generate_random_string_with_chosen_char_types(
            min_len=2,
            max_len=8,
            ascii_lower_letters=True,
        )
        return e_dom

    def get_list_of_invalid_rand_passwords(self) -> list[str]:
        return [
            "",
            "           ",
            self.generate_random_string_with_chosen_char_types(
                min_len=1,
                max_len=9,
                ascii_lower_letters=True,
                ascii_upper_letters=True,
                digits_=True,
                cyrillic_lower_letters=True
            ),
            self.generate_random_string_with_chosen_char_types(
                min_len=10,
                max_len=25,
                ascii_lower_letters=True,
                ascii_upper_letters=True,
                cyrillic_lower_letters=True
            ),
            self.generate_random_string_with_chosen_char_types(
                min_len=10,
                max_len=25,
                ascii_lower_letters=True,
                digits_=True,
                cyrillic_lower_letters=True
            ),
            self.generate_random_string_with_chosen_char_types(
                min_len=10,
                max_len=25,
                ascii_lower_letters=True,
                ascii_upper_letters=True,
                digits_=True,
            ),
            self.generate_random_string_with_chosen_char_types(
                min_len=10,
                max_len=25,
                ascii_lower_letters=True,
                ascii_upper_letters=True,
                digits_=True,
                cyrillic_lower_letters=True
            ),
        ]
