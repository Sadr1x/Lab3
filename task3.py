"""Завдання 3: Демонстрація імпорту, __name__ та структури."""

class PackageError(Exception):
    """Власна помилка пакету."""
    pass


if __name__ == "__main__":
    print("--- Завдання 3: Перевірка роботи модуля та __name__ ---")
    print(f"Назва поточного модуля (__name__): {__name__}")
    
    try:
        raise PackageError("Тестова помилка модуля")
    except PackageError as e:
        print(f"Успішно перехоплено помилку: {e}")
