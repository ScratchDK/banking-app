from typing import Generator

transactions = [
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
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
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
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


# Так как в filter нельзя использовать конструкцию try - except была добавлена эта функция
def check_key(dict_: dict, currency: str) -> bool:
    """Функция получает на вход словарь с данными о транзакций и валютой для сортировки,
    и возвращает если есть совпадение по валюте и присутствуют все ключи в словаре.
    Функция используется для проверки исключений и сортировки в filter_by_currency"""
    try:
        if dict_["operationAmount"]["currency"]["code"] == currency:
            return True
        else:
            return False
    except KeyError:
        return False


def filter_by_currency(list_transactions: list, currency: str) -> Generator[str, None, None]:
    """Функция получает на вход список транзакций и валюту для сортировки,
    и возвращет итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    filter_transactions = filter(lambda x: check_key(x, currency), list_transactions)

    for el in filter_transactions:
        yield el


def transaction_descriptions(list_transactions: list) -> Generator[str, None, None]:
    """Функция получает на вход список транзакций и возвращает описание каждой операции по очереди"""
    for el in list_transactions:
        try:
            yield el["description"]
        except KeyError:
            yield f"В nранзакций {el["id"]} остсутствует поле 'description'"


def card_number_generator(start: int, end: int) -> list | str:
    """Функция получает на вход начало и конец диапазона и выдает
    список с номерами банковских карт в формате XXXX XXXX XXXX XXXX"""
    card_null = "0000000000000000"
    new_list = []
    list_card_number = []
    start_x = start
    if start > end:
        return "Начало диапазона не может быть больше его окончания!"
    elif start < 0 or end > 9999999999999999:
        return "Выход за допустимые границы диапазона!"
    else:
        while start_x <= end:
            new_list.append(card_null[: -len(str(start_x))] + str(start_x))
            list_card_number = list(map(lambda x: f"{x[0:4]} {x[4:8]} {x[8:12]} {x[12:16]}", new_list))
            start_x += 1

    return list_card_number


usd_transactions = filter_by_currency(transactions, "USD")

for i in range(2):
    print(next(usd_transactions))


list_descriptions = transaction_descriptions(transactions)

for i in range(3):
    print(next(list_descriptions))


print(card_number_generator(100, 10))
print(card_number_generator(5, 10))
