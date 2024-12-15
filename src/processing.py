from datetime import datetime

list_id = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_of_data: list, filter_state: str = "EXECUTED") -> list:
    """Функция получает на вход список данных (id, статус и дату) и значение для фильтраций по статусу,
    а затем возвращает новый список данных отобранных по фильтру"""
    new_list_data = []

    for el in list_of_data:
        if el.get("state") is None:
            pass
        elif el["state"] == filter_state:
            new_list_data.append(el)

    return new_list_data


def sort_by_date(list_of_data: list, ascending: bool = True) -> list:
    """Функция получает на вход список данных (id, статус и дату) и значение для сортировки по дате,
    а затем возвращает новый отсортированный список"""
    new_list_data = []

    for el in list_of_data:
        if not el.get("date"):
            raise KeyError("Список содержит словари с некорректными данными!")
        try:
            datetime.fromisoformat(el["date"])
            new_list_data.append(el)
        except ValueError:
            continue

    sorted_list_data = sorted(new_list_data, key=lambda x: x["date"], reverse=ascending)
    return sorted_list_data
