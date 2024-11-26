import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Проверка правильной фильтраций с валютой USD
def test_filter_by_currency_usd(transactions: list) -> None:
    result = filter_by_currency(transactions, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    assert next(result) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


# Проверка правильной фильтраций с валютой RUB
def test_filter_by_currency_rub(transactions: list) -> None:
    result = filter_by_currency(transactions, "RUB")
    assert next(result) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }

    assert next(result) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


# Проверка с значением фильтра валюты отсутствующим в списке
def test_filter_by_currency_eur(transactions: list) -> None:
    with pytest.raises(StopIteration) as e:
        result = filter_by_currency(transactions, "EUR")
        assert next(result) == str(e.value)


# Проверка с пустым списоком
def test_filter_by_currency_empty() -> None:
    with pytest.raises(StopIteration) as e:
        result = filter_by_currency([], "RUB")
        assert next(result) == str(e.value)


# Проверка на пропуск словаря с отсутствующими  ключами необходимыми для фильтрации
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
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "RUB",
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
        ),
    ],
)
def test_filter_by_currency_exception_test(data: list, filter_currency: str, expected: dict) -> None:
    result = filter_by_currency(data, filter_currency)
    assert next(result) == expected


# Проверка на корректность возвращаемых описаний транзакций
def test_transaction_descriptions(transactions: list) -> None:
    result = transaction_descriptions(transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"


# Проверка возвращаемого значения при отсутсвия ключа с описанием
@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
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
            ["В nранзакций 939719570 остсутствует поле 'description'", "Перевод со счета на счет"],
        )
    ],
)
def test_transaction_descriptions_exception_test(data: list, expected: list) -> None:
    result = transaction_descriptions(data)
    assert next(result) == expected[0]
    assert next(result) == expected[1]


# Проверка с пустым списоком
def test_transaction_descriptions_empty() -> None:
    with pytest.raises(StopIteration) as e:
        result = transaction_descriptions([])
        assert next(result) == str(e.value)


# Проверка на создание списка номеров карт в указанных границах диапазона,
# а также проверка исключений в случае если начало диапазона больше его окончания и выход за границы диапазона
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            100010,
            100020,
            [
                "0000 0000 0010 0010",
                "0000 0000 0010 0011",
                "0000 0000 0010 0012",
                "0000 0000 0010 0013",
                "0000 0000 0010 0014",
                "0000 0000 0010 0015",
                "0000 0000 0010 0016",
                "0000 0000 0010 0017",
                "0000 0000 0010 0018",
                "0000 0000 0010 0019",
                "0000 0000 0010 0020",
            ],
        ),
        (-10, 100, "Выход за допустимые границы диапазона!"),
        (100, 10, "Начало диапазона не может быть больше его окончания!"),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list) -> None:
    assert card_number_generator(start, end) == expected
