#/bin/python

from subprocess import call
from time import sleep

class Panandtilt:
    pan_servo = 5
    tilt_servo = 6

    pan_default_position = 150
    tilt_default_position = 150

    pan_current_position = 0
    tilt_current_position = 0

    def servo_control(self, servo, pulsewidth):
        call(["echo "+str(servo)+"="+str(pulsewidth)+" > /dev/servoblaster"], shell=True)


    def servo_reset_position(self):
        Panandtilt.pan_current_position = Panandtilt.pan_default_position
        self.servo_control(Panandtilt.pan_servo, pan_default_position)

        Panandtilt.tilt_current_position = Panandtilt.tilt_default_position
        self.servo_control(Panandtilt.tilt_servo, Panandtilt.tilt_default_position)

    def pan_left(self, increment):
        Panandtilt.pan_current_position = Panandtilt.pan_current_position + increment
        self.servo_control(Panandtilt.pan_servo, Panandtilt.pan_current_position)

    def pan_right(self, increment):
        Panandtilt.pan_current_position = Panandtilt.pan_current_position - increment
        self.servo_control(Panandtilt.pan_servo, Panandtilt.pan_current_position)

    def tilt_up(self, increment):
        Panandtilt.tilt_current_position = Panandtilt.tilt_current_position + increment
        self.servo_control(Panandtilt.tilt_servo, Panandtilt.tilt_current_position)

    def tilt_down(self, increment):
        Panandtilt.tilt_current_position = Panandtilt.tilt_current_position - increment
        self.servo_control(Panandtilt.tilt_servo, Panandtilt.tilt_current_position)

    
    def __init__(self):
        Panandtilt.pan_default_position = 150
        Panandtilt.tilt_default_position = 150
        Panandtilt.pan_current_position = 150
        Panandtilt.tilt_current_position = 150


control = Panandtilt()
control.servo_reset_position
for x in range(0,100):
    print control.pan_current_position
    print control.tilt_current_position
    control.pan_left(1)
    sleep(0.01)

for x in range(0,100):
    print control.pan_current_position
    print control.tilt_current_position
    control.pan_right(1)
    sleep(0.01)

for x in range(0,100):
    print control.pan_current_position
    print control.tilt_current_position
    control.tilt_up(1)
    sleep(0.01)

for x in range(0,100):
    print control.pan_current_position
    print control.tilt_current_position
    control.tilt_down(1)
    sleep(0.01)
