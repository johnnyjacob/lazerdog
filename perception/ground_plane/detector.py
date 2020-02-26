#/bin/python
#
# Copyright (c) 2020 Johnny Jacob <johnnyjacob@gmail.com>
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

import cv2
#import numpy
from apriltag import apriltag

TAGTYPE = 'tagStandard41h12'
imagepath = '/home/jony/Pictures/tag-detect-test.png'
BBCOLOR = 255,0,255
FONT = cv2.FONT_HERSHEY_SIMPLEX 

if __name__ == '__main__':
    tag_detector = apriltag(TAGTYPE)
    cam = cv2.VideoCapture(2)

    while cv2.waitKey(1) != 0x1b:
        ret, image = cam.read()
        greys = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detections = tag_detector.detect(greys)

        for det in detections:
            rect = det["lb-rb-rt-lt"].astype(int).reshape((-1,1,2))
            cv2.polylines(image, [rect], True, BBCOLOR, 2)
            ident = str(det["id"])
            pos = det["center"].astype(int) + (-10,10)
            cv2.putText(image, ident, tuple(pos), FONT, 1, BBCOLOR, 2)

        cv2.imshow ("Detections" , image)
    
    
