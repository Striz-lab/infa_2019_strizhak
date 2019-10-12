#!/usr/bin/python3

from pyrob.api import *


def finddoor():
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            return True
        else:
            move_right()
    if not wall_is_beneath():
        return True
    while not wall_is_on_the_left():
        if not wall_is_beneath():
            return True
        else:
            move_left()
    if not wall_is_beneath():
        return True
    return False




@task
def task_8_30():
    flag = finddoor()
    while flag:
        while not wall_is_beneath():
            move_down()
        flag = finddoor()


if __name__ == '__main__':
    run_tasks()
