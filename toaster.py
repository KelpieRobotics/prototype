import curses
import RPi.GPIO as GPIO
import time
from gpiozero import Robot


robot = Robot(left=(17, 18), right=(23, 25))
servoCtl = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoCtl, GPIO.OUT)
pin = GPIO.PWM(servoCtl, 50)
pin.start(2.5)

def extend(value):
    pin.ChangeDutyCycle(value)

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    curses.KEY_F6:    extend(2.5),
    curses.KEY_F7:    extend(7.5),
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()

pin.stop()
curses.wrapper(main)
GPIO.cleanup()
