import pytest

from src.widget import get_date, mask_account_card


# Проверка правильного преоброзования даты и обработки исключений при работе с недопустимыми форматами дат
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("31-02-2023", "Формат даты не поддерживается!"),
        ("31st of February, 2023", "Формат даты не поддерживается!"),
        ("2023-02", "Формат даты не поддерживается!"),
        ("31.02.23", "Формат даты не поддерживается!"),
        ("", "Формат даты не поддерживается!"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected


# Проверка правильной маскировки номера карты/счета с допустимыми и не правильными значениями или при их отсутствии
@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 14228426353", "Данный формат счета/номера карты не поддерживается!"),
        ("64686473678894779589 Счет", "Данный формат счета/номера карты не поддерживается!"),
        ("Platinum 8990922113665229 Visa", "Данный формат счета/номера карты не поддерживается!"),
        ("MasterCard 71583007347267581", "Данный формат счета/номера карты не поддерживается!"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 736", "Данный формат счета не поддерживаеться!"),
        ("Счет 123456789101112131415161718192021222324252627282930", "Данный формат счета не поддерживаеться!"),
        ("64686473678894779589 Счет", "Данный формат счета/номера карты не поддерживается!"),
        ("", "Данный формат счета/номера карты не поддерживается!"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected
