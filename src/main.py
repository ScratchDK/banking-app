from src.processing import filter_by_state, sort_by_date
from src.reader_utils import read_csv, read_excel, search_matches
from src.utils import transaction_processing
from src.widget import mask_account_card


def check_key(dict_: dict) -> bool:
    """Функция получает на вход словарь с данными о транзакций,
    и возвращает если есть совпадение по "RUB" и присутствуют все ключи в словаре.
    Функция используется для проверки исключений и сортировки в main"""
    try:
        if dict_["currency_code"] == "RUB":
            return True
        else:
            return False
    except KeyError:
        if dict_["operationAmount"]["currency"]["code"] == "RUB":
            return True
        else:
            return False


def main() -> None:
    """Функция отвечает за основную логику проекта и связывает функциональности между собой"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n "
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    input_choice = ["1", "2", "3"]

    input_user = ""
    while input_user not in input_choice:
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

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    list_status = ["EXECUTED", "CANCELED", "PENDING"]

    input_user_status = ""
    while input_user_status not in list_status:
        input_user_status = input("Введите статус: ").upper()

    status = filter_by_state(file_data, input_user_status)

    print("Отсортировать операции по дате? 'Да' или 'Нет'")

    input_user_date = input("Введите 'Да' или 'Нет': ")

    if input_user_date.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")

        input_user_ascending = input("Введите 'по возрастанию' или 'по убыванию': ").lower()
        if input_user_ascending == "по возрастанию":
            sorted_list = sort_by_date(status, False)
        elif input_user_ascending == "по убыванию":
            sorted_list = sort_by_date(status, True)
        else:
            sorted_list = sort_by_date(status)
    else:
        sorted_list = status

    print("Выводить только рублевые тразакции? 'Да' или 'Нет'")

    input_user_filter = input("Введите 'Да' или 'Нет': ").lower()

    if input_user_filter == "да":
        filter_rub = list(filter(lambda x: check_key(x), sorted_list))
    else:
        filter_rub = sorted_list

    print("Отфильтровать список транзакций по определенному слову в описании? 'Да' или 'Нет'?: ")

    input_user_word = input("Введите 'Да' или 'Нет': ").lower()

    if input_user_word == "да":
        word = input("Введите слово по которому пройдет фильтрация: ")
        filter_word = search_matches(filter_rub, word)

        if filter_word == "Совпадений не найдено!":
            print("Совпадений не найдено!")
            filter_word = filter_rub
    else:
        filter_word = filter_rub

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filter_word)}")

    for el in filter_word:
        if el.get("operationAmount"):
            if el.get("from"):
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['from'])} -> {mask_account_card(el['to'])}\n"
                    f"Сумма: {el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}\n"
                )
            else:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['to'])}\n"
                    f"Сумма: {el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}\n"
                )
        else:
            if el.get("from") and type(el["from"]) is not float:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['from'])} -> {mask_account_card(el['to'])}\n"
                    f"Сумма: {el['amount']} {el['currency_name']}\n"
                )
            else:
                print(
                    f"{el['date']} {el['description']}\n"
                    f"{mask_account_card(el['to'])}\n"
                    f"Сумма: {el['amount']} {el['currency_name']}\n"
                )
