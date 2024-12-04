import os
import json
from typing import Any


def transaction_processing(path_file: str) -> Any:
    """Обработка транзакций. На вход функция принимает путь до файла с транзакциями в формате .json
    и возвращает в виде списка. Если файл пустой или не содержит список транзакций возращает пустой список."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    full_path_file = os.path.join(base_dir, "data", path_file)

    try:
        with open(full_path_file, encoding="utf-8") as file_json:
            data = json.load(file_json)
    except Exception as e:
        print(type(e).__name__)
        return []
    else:
        return data


path_file_operations = "operations.json"
path_file_empty = "empty.json"
path_file_test = "utils_test.json"

print(transaction_processing(path_file_test))
