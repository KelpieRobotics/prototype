#################################################################################
# the following code is based on documention provided by gpiozero.readthedocs.io
#################################################################################

# import libaries 
import curses
from gpiozero import Robot
from gpiozero import PWMLED
from datetime import datetime

# Imports used for retriving sensor data
# import RPi.GPIO as GPIO
# import dht11

# Used for configuring GPIO pins strictly for sensor data
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.cleanup()

# Assigns pins for thrust motors, claw servo, and DHT11 sensor
robot = Robot(left=(17, 18), right=(23, 25)) # uses gpiozero robot class for both forward and reverse direction on both port and starboard motors
servo = PWMLED(4) # uses gpiozero PWMLED class for servo as there is no servo class built into the gpiozero
# sensor = dht11.DHT11(pin = 11) 

# initial servo value
servo.value = 0

# Function for changing the position of the servo
def extend(dCycle):
    servo.value = dCycle

# Assigns movement actions to keyboard keys
actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
}
# Disables servo after the position is set to zero 
servo.off

def main(window):
      
    next_key = None
    while True:
        # Used for retriving sensor data, displaying it to the CLI and loging the data to a csv file
        # sensor_result = sensor.read()
        # if result.is_valid():
        #     print("Temperature: %-3.1f C" % sensor_result.temperature)
        #     print("Humidity: %-3.1f %%" % sensor_result.humidity)
        #     f = open("sensor.csv", "a")
        #     f.write(datetime.now().strftime("%H:%M:%S")+","+str(sensor_result.temperature)+","+str(sensor_result.humidity)+"\n")
        #     f.close()
        # else:
        #     print("Error: %d" % sensor_result.error_code)
        #     f = open("sensor.csv", "a")
        #     f.write(datetime.now().strftime("%H:%M:%S")+",ERROR," + str(sensor_result.error_code)+"\n")
        #     f.close()
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
            # If the key being pressed is one of the movement commands it'll use the dictionary to call the correct function in the robot class
            if action is not None:
                action()
            # If the Shift key and the left key is pressed, the servo will retract 
            elif key == curses.KEY_SLEFT:
                extend(0.07)
            # If the Shift key and the left key is pressed, the servo will extend 
            elif key == curses.KEY_SRIGHT:
                extend(0.20)
            # If the Backspace key is pressed the servo will stop attempting to move, this is necessary as in the current state the servo is jittery
            elif key == curses.KEY_BACKSPACE:
                extend(0.00)
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()

curses.wrapper(main)