#/bin/python
#
# Copyright (c) 2013 Johnny Jacob <johnnyjacob@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



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

    
    def __init__(self, pan_servo, pan_default, tilt_servo, tilt_default):
        Panandtilt.pan_default_position = self.pan_default
        Panandtilt.tilt_default_position = self.tilt_default
        self.servo_reset_position()
