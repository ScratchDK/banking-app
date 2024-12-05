from unittest.mock import patch

import pytest

from src.external_api import currency_conversion


@pytest.mark.parametrize(
    "in_data, received_data, expected",
    [
        (
            {
                "id": 179194306,
                "state": "EXECUTED",
                "date": "2019-05-19T12:51:49.023880",
                "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "МИР 5211277418228469",
                "to": "Счет 58518872592028002662",
            },
            {
                "success": True,
                "query": {"from": "USD", "to": "RUB", "amount": 6381.58},
                "info": {"timestamp": 1733205976, "rate": 106.501573},
                "date": "2024-12-03",
                "result": 679648.308225,
            },
            679648.308225,
        ),
        (
            {
                "id": 179194306,
                "state": "EXECUTED",
                "date": "2019-05-19T12:51:49.023880",
                "operationAmount": {"amount": "6381.58", "currency": {"name": "USD"}},
                "description": "Перевод организации",
                "from": "МИР 5211277418228469",
                "to": "Счет 58518872592028002662",
            },
            {
                "success": True,
                "query": {"from": "USD", "to": "RUB", "amount": 6381.58},
                "info": {"timestamp": 1733205976, "rate": 106.501573},
                "date": "2024-12-03",
                "result": 679648.308225,
            },
            "Отсутствуют необходимые для выполнения операции поля!",
        ),
        (
            {
                "id": 179194366,
                "state": "EXECUTED",
                "date": "2020-17-28T12:51:49.023880",
                "operationAmount": {"amount": "6381.58", "currency": {"name": "FRN", "code": "FRN"}},
                "description": "Перевод организации",
                "from": "МИР 5211277418228469",
                "to": "Счет 58518872592028002662",
            },
            {},
            "На данный момент конвертация валют доступна только для EUR и USD!",
        ),
    ],
)
def test_currency_conversion(in_data: dict, received_data: dict, expected: float) -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = received_data
        assert currency_conversion(in_data) == expected
