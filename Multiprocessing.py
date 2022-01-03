"""
Multiprocessing test
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


import multiprocessing, time


def multi1():
    count1 = 0
    while True:
        count1 += 1
        time.sleep(1)
        print(count1)


def multi2():
    count2 = 0
    while True:
        count2 += 1
        time.sleep(2)
        print(count2)



if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=multi1)
    process_2 = multiprocessing.Process(target=multi2)
    process_1.start()
    process_2.start()

