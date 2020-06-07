import multiprocessing
import os
import time


def run_case(*text):
    print('入参：{0}，当前进程号：{1}'.format(text, os.getpid()))
    time.sleep(100)


if __name__ == '__main__':  # windows必须使用这句话，不要问我为什么，我也不知道
    print('当前是父进程，进程号：{0}'.format(os.getpid()))
    child = multiprocessing.Process(target=run_case, args=(1,2,))
    print('子进程启动')
    child.start()
    child.join()
    print('进程结束')