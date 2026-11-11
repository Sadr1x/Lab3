import json

def process_input(raw_value: str) -> float:
    try:
        number = float(raw_value)
        if number == 0:
            raise ZeroDivisionError()
        result = 100.0 / number
    except (ValueError, TypeError):
        print("[Except] Перехоплено помилку типу або формату даних.")
        raise
    except ZeroDivisionError:
        print("[Except] Перехоплено спробу ділення на нуль.")
        raise
    else:
        print(f"[Else] Успішний шлях! Результат: {result}")
        return result
    finally:
        print("[Finally] Блок звільнення ресурсів виконано.\n")

if __name__ == "__main__":
    print("--- Завдання 1: Тестування try/except/else/finally ---")
    try:
        process_input("10")
    except Exception:
        pass

    try:
        process_input("abc")
    except Exception:
        pass

    print("--- Завдання 1: Контекстний менеджер 'with' ---")
    try:
        with open("sample.json", "w", encoding="utf-8") as f:
            json.dump({"data": 123}, f)
        print("Файл успішно записано за допомогою 'with'.")
    except IOError as e:
        print(f"Помилка введення-виведення: {e}")
