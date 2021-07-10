from gpiozero import LED

from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep
import keyboard

factory = PiGPIOFactory(host='192.168.1.205')

red = LED(17,pin_factory=factory)
blue = LED(18,pin_factory=factory)
red.off()
blue.off() 
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
            print('forward')
            red.on()
            blue.on()
        elif keyboard.is_pressed('s'):  # if key 'q' is pressed 
            print('reverse')
        elif keyboard.is_pressed('a'):  # if key 'q' is pressed 
            red.on()
            print('left')
        elif keyboard.is_pressed('d'):  # if key 'q' is pressed 
            blue.on()
            print('right')
              # finishing the loop
        red.off()
        blue.off()  
    except:
        break  # if user pressed a key other than the given key the loop will break

################
#!/usr/bin/env python

# Import required modules
import time

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Drive the motor clockwise
# Motor A:
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.HIGH) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
# Motor A:
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.HIGH) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.HIGH) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB