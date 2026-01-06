from httpx import Request, RequestNotRead, Client


def make_curl_from_request(request: Request) -> str:
    """
    Генерирует команду cURL из HTTP-запроса httpx.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    # Создаем список с основной командой cURL, включая метод и URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # Добавляем тело запроса, если оно есть (например, для POST, PUT)
    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    # Объединяем части с переносами строк, исключая завершающий `\`
    return " \\\n  ".join(result)

#
# #Event hook
#
# def print_request(request: Request):
#     print(f"Выполняем запрос {request.method}")
#
# client = Client(event_hooks={"request": [print_request]}) #В ивент хук добавляем словарь и указываем там для request или response мы его юзаем
# #Сами функции (даже если она одна) передается в словаре, без ()
# #Функции будут вызваны в данном случае до выполнения запроса