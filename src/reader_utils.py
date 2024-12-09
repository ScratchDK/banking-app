import os

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
        return type(e).__name__
    else:
        py_data = df.to_dict(orient="records")
        return py_data


file_csv = "transactions.csv"
file_excel = "transactions_excel.xlsx"

test_csv = read_csv(file_csv)

for el in test_csv:
    print(el)

test_excel = read_excel("error")

for el in test_excel:
    print(el)
