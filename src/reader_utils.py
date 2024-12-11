import os
import re

# import csv
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_csv(path_file: str) -> list | str:
    """Функция принимает на вход названия файла .csv и возвращет из этого файла список словарей"""
    full_path_file_csv = os.path.join(base_dir, "data", path_file)

    # with open(full_path_file_csv, encoding='utf-8', mode='r') as file:
    #     reader = csv.reader(file, delimiter=';')
    #     for row in reader:
    #         print(row)

    try:
        df = pd.read_csv(full_path_file_csv, delimiter=";")
    except Exception as e:
        return type(e).__name__
    else:
        py_data = df.to_dict(orient="records")
        return py_data


def read_excel(path_file: str) -> list | str:
    """Функция принимает на вход названия файла .xlsx и возвращет из этого файла список словарей"""
    full_path_file_excel = os.path.join(base_dir, "data", path_file)

    try:
        df = pd.read_excel(full_path_file_excel)
    except Exception as e:
        return str(e)
    else:
        py_data = df.to_dict(orient="records")
        return py_data


def search_matches(list_dict: list, str_search: str) -> list:
    """Функция принимает на вход список словарей и строку поиска и возвращает список словарей где найдены совпадения"""
    pattern = re.compile(str_search, flags=re.IGNORECASE)
    new_list = []
    for el in list_dict:
        for value in el.values():
            if pattern.search(str(value)):
                new_list.append(el)
            else:
                pass
    return new_list


file_csv = "transactions.csv"
file_excel = "transactions_excel.xlsx"

test_csv = read_csv(file_csv)

test_excel = read_excel(file_excel)

list_transactions = search_matches(test_excel, "ПЕРЕВОД ОРГАНИЗАЦИИ")
