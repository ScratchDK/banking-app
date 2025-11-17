from unittest.mock import patch

import pytest

from src.main import main


@pytest.mark.parametrize(
    "user_input",
    [
        (["1", "executed", "нет", "нет", "нет"]),
        (["2", "canceled", "да", "", "нет", "нет"]),
        (["3", "PENDING", "да", "по убыванию", "нет", "да", "перевод"]),
        (["2", "canceled", "да", "по возрастанию", "да", "нет"]),
        (["empty", "1", "canceled", "да", "по возрастанию", "да", "нет"]),
        (["3", "PENDING", "да", "по убыванию", "нет", "да", "blah"]),
    ],
)
def test_multiple_inputs(user_input: list) -> None:
    with patch("builtins.input", side_effect=user_input):
        main()
