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

class Line:
    x0 = 0
    y0 = 0

    x1 = 0
    y1 = 0

    dx = 0
    dy = 0

    D = 0

    def plot(self, x, y):
        print x,y

    def next(self):
        x = 0
        y = self.y0
        self.D = (2*self.dy) - self.dx
        self.plot (self.x0, self.y0)
        for x in range(self.x0+1, self.x1+1):
            if (self.D > 0) :
                y = y +1 
                self.plot (x, y)
                self.D = self.D + (2*self.dy - 2*self.dx)
            else:
                self.plot (x, y)
                self.D = self.D + (2*self.dy)

    def __init__(self, x0, y0, x1, y1):
        Line.x0 = x0
        Line.y0 = y0
        Line.x1 = x1
        Line.y1 = y1
        
        Line.dx = x1 - x0
        Line.dy = y1 - y0

l  = Line (0,1,6,4)
l.next()
