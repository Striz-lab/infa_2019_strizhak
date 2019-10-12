#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    i=1
    j=1
    k=1
    while not wall_is_on_the_right():
        move_right()
        k+=1
    move_left(k-1)
    while not wall_is_beneath():
        while not wall_is_on_the_right():
            if  not ( i==j or i+j==k+1):
                fill_cell()
            move_right()
            j+=1
        if  not ( i==j or i+j==k+1):
            fill_cell()
        j=1
        move_left(k-1)
        move_down()
        i+=1
    while not wall_is_on_the_right():
        if  not ( i==j or i+j==k+1):
            fill_cell()
        move_right()
        j+=1
    move_left(k-1)


if __name__ == '__main__':
    run_tasks()
