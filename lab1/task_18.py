#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

    while wall_is_above() == 1:
        if wall_is_on_the_right() == 0:
            move_right()
        else:
            while wall_is_on_the_left() == 0:
                move_left()
    while wall_is_above() == 0:
        move_up()
    while wall_is_on_the_left() == 0:
        move_left()

if __name__ == '__main__':
    run_tasks()

