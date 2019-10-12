#!/usr/bin/python3

from pyrob.api import *


@task (delay=0.01)
def task_7_5():
    move_right()
    fill_cell()
    a = 1
    while not wall_is_on_the_right():
        for i in range(a):

            for i in range(a):
                if not wall_is_on_the_right():
                    move_right()
            if not wall_is_on_the_right():
                fill_cell()
            a +=1
        





if __name__ == '__main__':
    run_tasks()
