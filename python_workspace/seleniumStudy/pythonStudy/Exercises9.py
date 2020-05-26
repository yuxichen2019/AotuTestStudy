# -*- coding: utf-8 -*- 
# 2020/05/25 16:02 
# seleniumStudy
# Exercises9.py 
# company

'''要求输入国际象棋棋盘'''

for i in range(8):
    for j in range(8):
        if ((i + j) % 2 == 0):
            print(chr(219) * 2, end="")  # 打印特殊字符，不换行
        else:
            print("  ", end="")
    print("")  # 打印完了一行之后需要换行