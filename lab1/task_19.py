#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while wall_is_on_the_right() == 0:
            move_right()
    if wall_is_above() == 1:
        while wall_is_on_the_left() == 0:
            move_left()
    while wall_is_above() == 0:
        move_up()
    while wall_is_on_the_left() == 0:
        move_left()
    if wall_is_beneath() == 1:
        while wall_is_on_the_right() == 0:
            move_right()

if __name__ == '__main__':
    run_tasks()
