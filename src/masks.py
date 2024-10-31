def get_mask_card_number(card_number: str) -> str:
    """Функция получает на вход номер карты и возвращает его в формате XXXX XX** **** XXXX"""
    return f"{card_number[:-17]} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(bank_account_number: str) -> str:
    """Функция получает на вход номер счета и возвращает его в формате **XXXX"""
    return f"{bank_account_number[:-21]} **{bank_account_number[-4:]}"
