import os
import json
from typing import Any


def transaction_processing(path_file: str) -> Any:
    """Обработка транзакций. На вход функция принимает путь до файла с транзакциями в формате .json
    и возвращает в виде списка. Если файл пустой или не содержит список транзакций возращает пустой список."""
    abs_path = os.path.abspath(path_file)
    print(abs_path)

    try:
        with open(abs_path, encoding="utf-8") as file_json:
            data = json.load(file_json)
    except Exception as e:
        print(type(e).__name__)
        return []
    else:
        return data


path_file_operations = "../data/operations.json"
path_file_empty = "../data/empty.json"
path_file_test = "../data/utils_test.json"

print(transaction_processing(path_file_empty))
