from reader_utils import read_excel
from collections import Counter

descriptions = ["Перевод с карты на карту", "Перевод организации", "Открытие вклада"]


def count_transaction(list_dict: list, list_cat: list) -> dict:
    """Функция принимает на вход список словарей и список с категориями
     и возвращает словарь с подсчетом каждой категорий"""
    new_list = []

    for transaction in list_dict:
        category = transaction["description"]
        if category in list_cat:
            new_list.append(category)
        else:
            pass

    cat_counter = Counter(new_list)

    return dict(cat_counter)


file_excel = "transactions_excel.xlsx"

test_excel = read_excel(file_excel)

print(count_transaction(test_excel, descriptions))
