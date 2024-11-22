def get_mask_card_number(card_number: str) -> str:
    """Функция получает на вход номер карты и возвращает его в формате XXXX XX** **** XXXX"""
    split_number = card_number.split(" ")
    if len(split_number[-1]) == 16 and split_number[-1].isdigit():
        name_card = " ".join(split_number[:-1])
        return f"{name_card} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        return 'Данный формат карт не поддерживаеться!'


def get_mask_account(bank_account_number: str) -> str:
    """Функция получает на вход номер счета и возвращает его в формате **XXXX"""
    split_number = bank_account_number.split(" ")
    if split_number[0] == "Счет" and split_number[-1].isdigit() and 4 < len(split_number[-1]) < 40:
        return f"{split_number[0]} **{bank_account_number[-4:]}"
    else:
        return 'Данный формат счета не поддерживаеться!'
