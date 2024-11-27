import pytest
import os
import datetime

from src.decorators import log

time_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 0, "division: [error] ZeroDivisionError. Inputs: ((5, 0), {})"),
        ("текст", 2, "division: [error] TypeError. Inputs: (('текст', 2), {})"),
        (12, 3, 4),
        (72, 12, 6),
        (11, 2, 5),
    ],
)
def test_log_func_division(a: int, b: int, expected: str | int) -> None:
    @log()
    def division(num_a: int, num_b: int) -> int:
        return num_a // num_b

    result = division(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 0, f"{time_start} - division: [error] ZeroDivisionError. Inputs: ((5, 0), {{}})\n"),
        ("текст", 2, f"{time_start} - division: [error] TypeError. Inputs: (('текст', 2), {{}})\n"),
        (12, 3, f"{time_start} - division: [ok]\n")
    ],
)
def test_log_func_division_writing (a: int, b: int, expected: str | int) -> None:
    @log("logs.txt")
    def division(num_a: int, num_b: int) -> int:
        return num_a // num_b

    division(a, b)

    with open("logs.txt", "r", encoding="utf-8") as file:
        result = file.read()

    os.remove("logs.txt")

    assert result == expected


def test_log_func_filter_by_currency(transactions: list) -> None:
    @log()
    def filter_by_currency(list_transactions: list, currency: str) -> list:
        filter_transactions = []
        for el in list_transactions:
            if el["operationAmount"]["currency"]["code"] == currency:
                filter_transactions.append(el)
            else:
                pass
        return filter_transactions

    result = filter_by_currency(transactions, "USD")
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.mark.parametrize(
    "data, filter_currency, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "USD",
            "filter_by_currency: [error] KeyError. "
            "Inputs: (("
            "["
            "{"
            "'id': 939719570, "
            "'state': 'EXECUTED', "
            "'date': '2018-06-30T02:08:58.425572', "
            "'description': 'Перевод организации', "
            "'from': 'Счет 75106830613657916952', "
            "'to': 'Счет 11776614605963066702'}, "
            "{"
            "'id': 142264268, "
            "'state': 'EXECUTED', "
            "'date': '2019-04-04T23:20:05.206878', "
            "'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, "
            "'description': 'Перевод со счета на счет', "
            "'from': 'Счет 19708645243227258542', "
            "'to': 'Счет 75651667383060284188'}], 'USD'), {})",
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "RUB",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
    ],
)
def test_log_func_filter_by_currency_error(data, filter_currency, expected) -> None:
    @log()
    def filter_by_currency(list_transactions: list, currency: str) -> list:
        filter_transactions = []
        for el in list_transactions:
            if el["operationAmount"]["currency"]["code"] == currency:
                filter_transactions.append(el)
            else:
                pass
        return filter_transactions

    result = filter_by_currency(data, filter_currency)
    print(result)
    assert result == expected
