import subprocess
import sys
import os

child_path = os.path.join(os.path.dirname(__file__), 'child.py')
command = [sys.executable, child_path]  # sys.execcutable就是Python命令的路径

pipes = []
n = 0
while n < 5:
    # 开启5个进程
    pipe = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    pipe.stdin.write(str(n).encode('utf8'))  # 这里只接受字节串输入，可以查看源码
    pipe.stdin.close()
    pipes.append(pipe)
    n += 1

while pipes:
    pipe = pipes.pop()
    pipe.wait()