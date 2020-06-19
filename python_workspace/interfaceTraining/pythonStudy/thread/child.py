import sys
import os
import time

input_msg = sys.stdin.read()
msg = '当前获取到的参数：{0}，当前进程号：{1}'.format(input_msg, os.getpid())
print(msg)  # 子进程是标准输出不能直接在控制台看到
with open(r'./a.txt', 'a+', encoding='utf8') as f:
    f.write(msg)
    f.write('\n')
time.sleep(1000)