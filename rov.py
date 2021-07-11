import curses
from gpiozero import Robot
from gpiozero import PWMLED
import RPi.GPIO as GPIO
import dht11
from datetime import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

robot = Robot(left=(17, 18), right=(23, 25))
servo = PWMLED(4)
instance = dht11.DHT11(pin = 24)




servo.value = 0

def extend(dCycle):
    servo.value = dCycle


actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
}

servo.off

def main(window):
    # initialize GPIO   
    next_key = None
    while True:
        result = instance.read()
        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            f = open("sample.csv", "a")
            f.write(datetime.now().strftime("%H:%M:%S")+","+str(result.temperature)+","+str(result.humidity)+"\n")
            f.close()
        else:
            print("Error: %d" % result.error_code)
            f = open("sample.csv", "a")
            f.write(datetime.now().strftime("%H:%M:%S")+",ERROR," + str(result.error_code)+"\n")
            f.close()
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
            elif key == curses.KEY_SLEFT:
                extend(0.07)
            elif key == curses.KEY_SRIGHT:
                extend(0.20)
            elif key == curses.KEY_BACKSPACE:
                extend(0.00)
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()

curses.wrapper(main)