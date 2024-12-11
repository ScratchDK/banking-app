from src.utils import transaction_processing
from src.reader_utils import read_csv, read_excel
from src.processing import filter_by_state


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n "
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")

    input_user = input("Введите номер: ")

    file_data = []

    if input_user == "1":
        file_data = transaction_processing("operations.json")
        print("Для обработки выбран JSON-файл.")
    elif input_user == "2":
        file_data = read_csv("transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif input_user == "3":
        file_data = read_excel("transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Ни один из пунктов меню не был выбран!")

    print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    input_user = input("Введите статус: ")

    status = filter_by_state(file_data, input_user)

    for el in status:
        print(el)


main()
