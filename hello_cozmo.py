#!/usr/bin/env python3

'''Merry Christmas

Make Cozmo say 'Merry Christmas' to Axel & Eléa.
'''

import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello Axel and Eléa. I wish you a Merry Christmas!").wait_for_completed()

cozmo.run_program(cozmo_program)
