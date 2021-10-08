# Пример 3.8.PP4E\Streams\moreplus.py

import sys

def defreply():
    """
    читает клавишу, нажатую пользователем,
    даже если stdin перенаправлен в файл или канал
    """
    if sys.stdin.isatty():              # если stdin связан с консолью
        return input('?')               # читать ответ из stdin
    else:
        if sys.platform[:3] == 'win':   # если stdin был перенаправлен,
            import msvcrt               # его нельзя использовать для чтения
            msvcrt.putch(b'?')          # ответа пользователя
            key = msvcrt.putch()        # использовать инструмент консоли
            msvcrt.putch(b'\n')         # getch(), которая не выводит символ
            return key                  # для нажатой клавиши
        else:
            assert False, 'platform not supported'
            #для Linux: open('/dev/tty').readline()[:-1]

def more(text, numlines=10):
    """
    реализует постраничный вывод содержимого строки в stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for lines in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y']: break

if __name__ == '__main__':               # если выполняется, ф не импортируется
    if len(sys.argv) == 1:               # если нет аргументов командной строки
        more(sys.stdin.read())           # вывести содержимое stdin
    else:
        more(open(sys.argv[1]).read())    # иначе вывести содержимое файла

