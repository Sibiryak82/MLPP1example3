# ������ 3.6.PP4E\System\Streams\sorter.py

import sys                               # ��� sorted(sys.stdin)
lines = sys.stdin.readlines()            # ������ ������� ������ �� stdin,
lines.sort()                             # ��������� ��
for line in lines: print(line, end='')   # ���������� ���������� � stdout
                                         # ��� ���������� ���������