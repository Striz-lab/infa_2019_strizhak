#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	for i in range (100):
		while wall_is_beneath() == 0:
			move_down()
	for i in range (100):
		while wall_is_beneath() == 1:
			move_right()
	move_down()
	move_left()
	for i in range (100):
		while wall_is_on_the_left() == 0:
			move_left()



if __name__ == '__main__':
    run_tasks()
