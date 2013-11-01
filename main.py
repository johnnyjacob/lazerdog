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
from panandtilt import Panandtilt
from laser import Laser

head = Panandtilt(5, 150, 6, 150)
head.servo_reset_position

point = Laser (8)
point.on()

for x in range(0,100):
    print head.pan_current_position
    print head.tilt_current_position
    head.pan_left(1)
    sleep(0.01)

for x in range(0,100):
    print head.pan_current_position
    print head.tilt_current_position
    head.pan_right(1)
    sleep(0.01)

for x in range(0,100):
    print head.pan_current_position
    print head.tilt_current_position
    head.tilt_up(1)
    sleep(0.01)

for x in range(0,100):
    print head.pan_current_position
    print head.tilt_current_position
    head.tilt_down(1)
    sleep(0.01)
