'''
定时器 + 装饰器的配合使用来计算某一个函数的运行时间
'''
import threading
import time
import numpy as np
import matplotlib.pyplot as plt


def my_supperTimer(func):
    def my_timer():
        start = time.time()
        func()
        end = time.time()
        print('程序用时：{} 秒'.format(end - start))

    return my_timer


@my_supperTimer
def one():
    def my_timer():
        print('hello world')
        global timer
        # timer = threading.Timer(3, my_timer)
        # timer.start()

        timer = threading.Timer(3, my_timer)
        timer.start()
        time.sleep(12)
        timer.cancel()

    return my_timer()


# def one():
#     x = np.random.rand(100)
#     y = x
#     plt.plot(x, y)
#     plt.show()


if __name__ == '__main__':
    one()