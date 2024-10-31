from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция получает на вход номер карты или счета и передает
    в импорт функций модуля masks для приведения к стандарту
    XXXX XX** **** XXXX для карт или **XXXX для счета"""
    if account_card[-20:].isdigit():
        return get_mask_account(account_card)
    elif account_card[-16:].isdigit():
        return get_mask_card_number(account_card)
    else:
        return "Данный формат счета/номера карты не поддерживается!"


def get_date(date: str) -> str:
    """Функция получает на вход дату в виде строки и возвращает её в формате "ДД.ММ.ГГГГ"""
    modified_date = date[:10].split("-")[::-1]
    new_date = ".".join(modified_date)

    return new_date


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))
