# Импорт библиотек
import argparse
import re
import PyPDF2 as pd


# Задание функции, которая будет находить регулярные выражения
def rebmf(pdf):
    red = input()           # Ввод регулярного выражения (далее - РВ)
    out = ""                # Переменная для цикла "STR"
    text = ""               # Переменная для цикла "Вывод функции"
    file = pd.PdfFileReader(open(pdf, mode='rb'),
                            strict=False)  # Загрузка-чтение pdf-файла
    for i in range(file.getNumPages()):
        text += file.getPage(i).extractText()
        # Получение текста i-той страницы (в PyPDF2 отсутствует возможность
        # выделить весь текст файла сразу), поэтому
        # просто зацикливаем выделение по страницам
    red = ".*" + red + ".*"
    # Делаем так для того, чтобы на выходе получать целую строку с РВ
    refinder = re.findall(red, text)  # Поиск соответствий по введенному РВ
    for i in range(len(refinder)):  # Тк на выходе в переменной refinder мы
        out += str(refinder[i])  # получаем список, то для лучшего восприятия,
        out += "\n"  # на выходе выведем найденные соответствия в виде строки,
    return(out)  # где все соответствия разделены новой строкой


# Задание еще одной функции (чисто для интереса), которая будет выводить
# количество страниц в открываемом pdf-файле
def lox(pdf):
    p = "Количество страниц в тексте - " + str(pd.PdfFileReader(
        open(pdf, mode='rb'),  # В переменную записывается исходнозаданная
        strict=False).getNumPages())  # строка и количество страниц pdf-файла
    return(p)


# Тепрь создаем интерфейс консоли с помощью argparce
parser = argparse.ArgumentParser(  # Задаем новый парсер
    description='Найдите в своем файле регулярные выражения!')
parser.add_argument('pdf', metavar='PDF', type=str,  # Теперь задаем аргументы
                    help='PDF-File for opening')  # (объекты) для парсера,
parser.add_argument('-re', '--regular', action='store_const',
                    const=rebmf, default=lox,
                    help='''Get the RE from your PDF
                    (default: count pages from PDF)''')
# А также свойства аргументов: имя опционального и позиционного аргументов,
# справка, а также значение(какая из функций активируется) для опционального
# аргумента по умолчанию и по вызову, тип данных для позиционного аргумента
args = parser.parse_args()  # Команда для записи того, что ввели с консоли
print(args.regular(args.pdf))  # Итоговый вывод значения функции
