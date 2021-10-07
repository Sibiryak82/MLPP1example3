# Пример 3.7.PP4E\System\Streams\sorter.py

import sys
sum = 0
while True:
    try:
        line = input()    # или sys.stdin.readlines()
    except EOFError:      # или for line in sys.stdin:
        break             # input отсекает символы \n в конце строк
    else:
        sum += int(line)  # во 2-м издании использовалась функция string.atoi()
print(sum)