import random
import string
import logging

logger = logging.getLogger(__name__)


class DataGenerator:
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    cyrillic_chars = [chr(i) for i in range(0x0410, 0x045F)]
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
            cyrillic_symbols: bool = False,
            punctuation_: bool = False,
            whitespace_: bool = False
    ) -> str | None:
        """Parameters ascii_lower_letters -...- whitespace_ determine whether characters
        from the corresponding categories will be used. Min and max len define string length."""
        if max_len > 0 and 0 < min_len <= max_len:
            string_ = []
            length = random.randint(min_len, max_len)
            params_number = 0
            params = (ascii_lower_letters, ascii_upper_letters, digits_, cyrillic_symbols, punctuation_, whitespace_)
            char_types = (
                self.lowercase_letters, self.uppercase_letters, self.digits,
                self.cyrillic_chars, self.punctuation, self.whitespace,)
            for i in params:
                params_number += self._calc(i)
            k = round(length / params_number)
            if k == 0:
                k = 1
            for n in range(params_number):
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
        logger.info(f"Generated password {passw}")
        return passw

    def get_rand_valid_passw_for_a1qa_task(self) -> str:
        passw = self.generate_random_string_with_chosen_char_types(
            min_len=10,
            max_len=15,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
            cyrillic_symbols=True
        )
        logger.info(f"Generated password {passw}")
        return passw

    def get_rand_valid_email_name(self) -> str:
        e_name = self.generate_random_string_with_chosen_char_types(
            min_len=6,
            max_len=12,
            ascii_lower_letters=True,
            ascii_upper_letters=True,
            digits_=True,
        )
        logger.info(f"Generated password {e_name}")
        return e_name

    def get_rand_valid_email_domain(self) -> str:
        e_dom = self.generate_random_string_with_chosen_char_types(
            min_len=2,
            max_len=8,
            ascii_lower_letters=True,
        )
        logger.info(f"Generated password {e_dom}")
        return e_dom
