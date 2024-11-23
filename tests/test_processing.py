import pytest

from src.processing import filter_by_state, sort_by_date


# Проверка на вывод списка при указанном фильтре и при отсутствий словарей с указанным фильтром во входящем списке
@pytest.mark.parametrize(
    "filter_state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("NO_STATUS", []),
    ],
)
def test_filter_by_state(list_id: list, filter_state: str, expected: list) -> None:
    assert filter_by_state(list_id, filter_state) == expected


# Проверка на сортировку по дате в порядке увеличения, уменьшения
@pytest.mark.parametrize(
    "ascending, expected",
    [
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(list_id: list, ascending: bool, expected: list) -> None:
    assert sort_by_date(list_id, ascending) == expected


# Проверка на сортировку по дате c наличием в списке словарей с нестандартными датами
def test_sort_by_date_non_standart(date_non_standart: list) -> None:
    assert sort_by_date(date_non_standart) == [
        {"id": 187513269, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 844751227, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Проверка на вызов исключения при фильтраций списка с отсутствием ключа state
def test_filter_by_state_without_data() -> None:
    with pytest.raises(KeyError) as e:
        filter_by_state([{"id": 939719570, "date": "2018-06-30T02:08:58.425572"}])
    assert str(e.value) == "'Список содержит словари с некорректными данными!'"


# Проверка на вызов исключения при фильтраций списка с отсутствием ключа date
def test_sort_by_date_without_data() -> None:
    with pytest.raises(KeyError) as e:
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED"},
            ]
        )
    assert str(e.value) == "'Список содержит словари с некорректными данными!'"
