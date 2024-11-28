import datetime
from typing import Any, Callable


def log(filename: str = "") -> Callable[[Callable[..., Any]], Any]:
    """Функция 'обертка' для ведения логов входящих функций, если в параметрах указан файл,
    то статус выполнения функции сохраняется в него, если нет то выводится в консоль."""

    def my_decorator(func: Callable) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_start = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error = f"{func.__name__}: [error] {type(e).__name__}. Inputs: ({args}, {kwargs})"

                if filename != "":
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{time_start} - {error}\n")
                else:
                    print(f"{time_start} - {error}\n")
                return error
            else:
                if filename != "":
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{time_start} - {func.__name__}: [ok]\n")
                else:
                    print(f"{time_start} - {func.__name__}: [ok]")
                return result

        return wrapper

    return my_decorator
