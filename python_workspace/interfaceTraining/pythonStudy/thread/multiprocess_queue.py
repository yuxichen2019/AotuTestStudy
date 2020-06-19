import multiprocessing
import os


class A:
    def __init__(self, num):
        self.num = num
        pass

    def get(self):
        return self.num


one = A(1)
two = A(2)


def put_msg(que):
    print('写数据，我的进程号是{0}'.format(os.getpid()))
    for i in [one, two]:
        que.put(i)


def get_msg(que):
    print('读数据,我的进程号是{0}'.format(os.getpid()))
    while True:
        msg = que.get()
        print('{0}拿到的数据：{1}'.format(os.getpid(), msg.get()))


if __name__ == '__main__':
    print('当前是父进程，进程号：{0}'.format(os.getpid()))
    queue = multiprocessing.Queue()
    child1 = multiprocessing.Process(target=put_msg, args=(queue,))
    child2 = multiprocessing.Process(target=get_msg, args=(queue,))

    child1.start()
    child2.start()
    child1.join()
    child2.terminate()  # 因为死循环，需要终止
    print('子进程启动')
    print('进程结束')