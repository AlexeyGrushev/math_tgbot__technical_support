page = 0


def return_page() -> int:
    return page


def addiction_page() -> None:
    global page
    page += 1
    return


def subtraction_page() -> None:
    global page
    page -= 1
    return


def default_page() -> None:
    global page
    page = 0
    return

FAQ_INFO = [
    """
<b>Math</b>

Приложение, которое помогает школьникам и студентам тренироваться правильно решать
полные квадратные уравнения, а также строить графики функции по математическим формулам.

В этом разделе Вы сможете найти ответы на наиболее частые вопросы о работе приложения.

Страница 1
    """,

    """
<b>Как использовать приложение Math для решения квадратных уравнений?</b>

Для решения квадратных уравнений введите формулу вида "ax^2 + bx + c = 0", где a, b и c - коэффициенты уравнения.
Нажмите кнопку "Решить", и приложение вычислит корни уравнения и скажет, решено оно верно или нет.
Также приложение записывает статистику решений, чтобы Вы могли оценивать свои результаты
Пожалуйста, убедитесь, что вы правильно ввели корни уравнения и используете правильный формат.
Если приложение все еще не решает уравнение, попробуйте обратиться к нашей технической поддержке.

Страница 2
    """,

    """
<b>Как использовать приложение Math для построения графиков?</b>

Для построения графиков введите формулу функции вида
"y = f(x)", где f(x) - функция, которую вы хотите построить.
Нажмите кнопку "Построить график", и приложение построит график функции.

Пожалуйста, убедитесь, что вы правильно ввели формулу функции и используете правильный формат.
Если приложение все еще не строит график, попробуйте обратиться к нашей технической поддержке.

<b>Обозначения:</b>
x*2 - x умножить на 2
x**2 - x в квадрате
sin(x) - Обозначение sin x

Страница 3
    """,
    """
<b>Как сохранить график, созданный в приложении Math?</b>

Последний построенный график функции сохраняется по пути:
<u>data/img/graphic.png</u>

Вы можете скопировать изображение в любое удобное место

Страница 4
    """,
    """
<b>Как связаться с технической поддержкой приложения Math?</b>

Чтобы связаться с технической поддержкой, отправьте сообщение нашему телеграм боту технической поддержки через раздел "Обратиться в поддержку📨".
Мы постараемся ответить вам как можно скорее и помочь решить вашу проблему.

Страница 5
    """
]