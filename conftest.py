import pytest


@pytest.fixture
def list_id():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def date_non_standart():
    return [
        {'id': 187513269, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 844751227, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': "31-02-2023"},
        {'id': 939719570, 'state': 'EXECUTED', 'date': "31st of February, 2023"},
        {'id': 594226727, 'state': 'CANCELED', 'date': "2023-02"},
        {'id': 615064591, 'state': 'CANCELED', 'date': "31.02.23"}
    ]