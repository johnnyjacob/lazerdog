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

from subprocess import call
from time import sleep

import panandtilt as Panandtilt
import lazer

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
