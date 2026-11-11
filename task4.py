from typing import List, Optional

def calculate_average(numbers: List[float]) -> float:
    """Обчислює середнє арифметичне значення елементів списку.

    Args:
        numbers (List[float]): Список числових значень.

    Returns:
        float: Середнє арифметичне число.

    Raises:
        ValueError: Якщо передано порожній список.
    """
    if not numbers:
        raise ValueError("Список не може бути порожнім")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("--- Завдання 4: Документація та інтроспекція ---")
    print("Атрибут __name__ функції:", calculate_average.__name__)
    print("Анотації типів (__annotations__):", calculate_average.__annotations__)
    print("\nДокументація функції (__doc__):\n")
    print(calculate_average.__doc__)
    
    print("Результат роботи help():")
    help(calculate_average)
