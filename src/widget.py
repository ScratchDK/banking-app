from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция получает на вход номер карты или счета и передает
    в импорт функций модуля masks для приведения к стандарту
    XXXX XX** **** XXXX для карт или **XXXX для счета"""

    split_account_card = account_card.split(" ")

    if split_account_card[0] == "Счет" and split_account_card[-1].isdigit():
        return get_mask_account(account_card)
    elif split_account_card[-1].isdigit() and len(split_account_card[-1]) == 16:
        return get_mask_card_number(account_card)
    else:
        return "Данный формат счета/номера карты не поддерживается!"


def get_date(date: str) -> str:
    """Функция получает на вход дату в виде строки и возвращает её в формате "ДД.ММ.ГГГГ"""

    try:
        datetime.fromisoformat(date)
    except ValueError:
        return "Формат даты не поддерживается!"

    modified_date = date[:10].split("-")[::-1]
    new_date = ".".join(modified_date)

    return new_date
