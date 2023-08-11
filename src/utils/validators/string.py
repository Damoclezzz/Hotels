from typing import Callable


class StringValidator:
    @staticmethod
    def __type_check(validator: Callable):
        def wrapped_validator(*args, **kwargs):
            for value in (args + tuple(kwargs.values())):
                if not isinstance(value, str):
                    raise TypeError(f'Wrong type: {type(value)} in StringValidator')

            validator(*args)

        return wrapped_validator

    @staticmethod
    @__type_check
    def contains_digit(value: str):
        for char in value:
            if char.isdigit():
                return True

        return False

    @staticmethod
    @__type_check
    def contains_upper(value: str):
        for char in value:
            if char.isupper():
                return True

        return False
