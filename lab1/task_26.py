#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_2_4():
    for i in range (4):
        for i in range (9):
            move_right()
    
    
            fill_cell()
            move_down()
            move_right()
            fill_cell()
            move_left()
            move_down()
            fill_cell()
            move_up()
            fill_cell()
            move_left()
            fill_cell()
        
            move_up()
            move_right(3)
    
            move_right()

        move_right()
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()

        move_up()
        while not wall_is_on_the_left():
            move_left()
        move_down(4)

    for i in range (9):
        move_right()
        
        
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
            
        move_up()
        move_right(3)
        move_right()
    
    move_right()
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
        
    move_up()
    while not wall_is_on_the_left():
        move_left()





if __name__ == '__main__':
    run_tasks()
