#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
	move_right()
	for i in range (9):
		while wall_is_beneath() == 1:
			move_right()


if __name__ == '__main__':
    run_tasks()
