# Пример 3.3.PP4E\System\Environment\setenv.py

import os
print('setenv...', end=' ')
print(os.environ['USER'])      # выведет текущее значение переменной оболочки

os.environ['USER'] = 'Brian'   # неявно вызовет функцию os.putenv
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'  # изменения передается порождаемым программам
os.system('python echoenv.py') # и связанным с процессом библ. модулями на С

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())

