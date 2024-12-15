from src.counters import count_transaction


def test_count_transaction(list_search_word: list, list_categories: list) -> None:
    print(list_search_word)
    assert count_transaction(list_search_word, list_categories) == {"Перевод организации": 2, "Открытие вклада": 2}
