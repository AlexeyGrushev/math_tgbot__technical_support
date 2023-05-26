def format(data) -> str:
    FORMAT = f"""
<b>{data["theme"]}</b>
<i>{data["discription"]}</i>

{data["appeal"]}

Обращение от пользователя: @{data["user"]}
    """
    return FORMAT