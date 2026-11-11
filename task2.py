class AppError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class ValidationError(AppError):
    def __init__(self, message: str, field_name: str) -> None:
        super().__init__(message)
        self.field_name = field_name

    def __str__(self) -> str:
        return f"[Помилка у полі '{self.field_name}']: {self.args[0]}"


def validate_age(raw_age: str) -> int:
    try:
        age = int(raw_age)
        if age < 0 or age > 120:
            raise ValueError("Вік поза допустимим діапазоном")
        return age
    except ValueError as original_err:
        raise ValidationError("Некоректне значення віку", "age") from original_err


if __name__ == "__main__":
    print("--- Завдання 2: Ієрархія та ланцюжки виключень ---")
    try:
        validate_age("invalid_text")
    except ValidationError as err:
        print(f"Зловлено доменну помилку: {err}")
        if err.__cause__:
            print(f"Первинна причина (__cause__): {type(err.__cause__).__name__} -> {err.__cause__}")
