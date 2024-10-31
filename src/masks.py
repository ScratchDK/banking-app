def get_mask_card_number(card_number: str) -> str:
    """Функция получает на вход номер карты и возвращает его в формате XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(bank_account_number: str) -> str:
    """Функция получает на вход номер счета и возвращает его в формате **XXXX"""
    return f"**{bank_account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
