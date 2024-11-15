from src.widget import *


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
