#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while wall_is_above() == 0:
        move_up()

    if wall_is_on_the_right() == 0:
        while wall_is_on_the_right() == 0:
            move_right()
    elif wall_is_on_the_left() == 0:
        while wall_is_on_the_left() == 0:
            move_left()


if __name__ == '__main__':
    run_tasks()

