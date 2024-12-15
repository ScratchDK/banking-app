import json
import logging
import os
from typing import Any

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path_file_logs = os.path.join(base_dir, "logs", "utils.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file_logs, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transaction_processing(path_file: str) -> Any:
    """Обработка транзакций. На вход функция принимает путь до файла с транзакциями в формате .json
    и возвращает в виде списка. Если файл пустой или не содержит список транзакций возращает пустой список."""
    logger.info("Старт")
    full_path_file_data = os.path.join(base_dir, "data", path_file)

    try:
        with open(full_path_file_data, encoding="utf-8") as file_json:
            data = json.load(file_json)

    except Exception as e:
        logger.error(f"{type(e).__name__}, возвращен пустой список")
        return []
    else:
        logger.info("Успешно получены данные")
        return data


path_file_operations = "operations.json"
path_file_empty = "empty.json"
path_file_test = "utils_test.json"
