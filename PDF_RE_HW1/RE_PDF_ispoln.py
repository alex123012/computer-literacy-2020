#! /home/alexmakh/miniconda3/bin/python3
# Импорт модулей
import re
import PyPDF2 as pd
import argparse


# Создаем консольный интерфейс с помощью argparse
parser = argparse.ArgumentParser(  # Задаем новый парсер
    description='Найдите в своем файле регулярные выражения!')
parser.add_argument('pdf', metavar='PDF', type=str,  # Теперь задаем аргументы
                    help='PDF-File for opening')  # (объекты) для парсера,
parser.add_argument('re', metavar='RE', type=str,
                    help="Regular expression you want to match")
# А также свойства аргументов: имена аргументов, (Pdf-файл и регулярное
# выражение(далее РВ), справка, типы данных для обоих позиционных аргументов
args = parser.parse_args()  # Команда для записи того, что ввели с консоли


puk = pd.PdfFileReader(open(args.pdf, mode='rb'),
                       strict=False)  # Загрузка-чтение pdf-файла
text = ""  # Переменная для цикла выделения текста в тип данных string
for i in range(puk.getNumPages()):
    text += puk.getPage(i).extractText()
    # Получение текста i-той страницы (в PyPDF2 отсутствует возможность
    # выделить весь текст файла сразу), поэтому
    # просто зацикливаем выделение по страницам
out = ".*" + args.re + ".*"
# Делаем так для того, чтобы на выходе получать целую строку c РВ
count = re.findall(out, text)  # Поиск соответствий по введенному РВ
text = ""  # Переменная для цикла "вывода"
for i in range(len(count)):  # Тк на выходе в переменной count мы
    text += str(count[i])  # получаем список, то для лучшего восприятия,
    text += "\n"  # на выходе выведем найденные соответствия в виде строки,
print(text)     # где все соответствия разделены новой строкой
