#/bin/python

from subprocess import call
from time import sleep

def stop(time):
    print("stopleft")
    call (["echo 5=150 > /dev/servoblaster"], shell=True)
    print("stopright")
    call (["echo 6=150 > /dev/servoblaster"], shell=True)
    sleep(time)

def call_command(servo,pulsewidth):
    call(["echo "+str(servo)+"="+str(pulsewidth)+" > /dev/servoblaster"], shell=True)

def forwards(time):
    call_command(5,200)
    call_command(6,100)
    sleep(time)
    stop(5.1)

def back(time):
    call_command(5,100)
    call_command(6,200)
    sleep(time)
    stop(5.1)

def left(time):
    call_command(5,200)
    sleep(time)
    stop(5.1)

def right(time):
    call_command(6,100)
    sleep(time)
    stop(5.1)
#Edit instruction here using the definitions forward back left right sleep

forwards(1)
back(1)
left(1)
