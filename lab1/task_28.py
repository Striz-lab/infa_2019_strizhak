#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_6():
    a = 0
    while (wall_is_on_the_right() + a == 5) == 0:
        if cell_is_filled():
            a = a + 1
            move_right()
        else:
            move_right()
    move_left()


if __name__ == '__main__':
    run_tasks()
