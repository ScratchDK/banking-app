import logging
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path_file = os.path.join(base_dir, "logs", "masks.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция получает на вход номер карты и возвращает его в формате XXXX XX** **** XXXX"""
    logger.info("Старт")
    split_number = card_number.split(" ")
    if len(split_number[-1]) == 16 and split_number[-1].isdigit():
        name_card = " ".join(split_number[:-1])
        card = f"{name_card} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
        logger.info("Успешно возвращено значение")
        return card
    else:
        err = "Данный формат карт не поддерживаеться!"
        logger.error(err)
        return err


def get_mask_account(bank_account_number: str) -> str:
    """Функция получает на вход номер счета и возвращает его в формате **XXXX"""
    logger.info("Старт")
    split_number = bank_account_number.split(" ")
    if split_number[0] == "Счет" and split_number[-1].isdigit() and 4 < len(split_number[-1]) < 21:
        account_number = f"{split_number[0]} **{bank_account_number[-4:]}"
        logger.info("Успешно возвращено значение")
        return account_number
    else:
        err = "Данный формат счета не поддерживаеться!"
        logger.error(err)
        return err
