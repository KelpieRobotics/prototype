import keyboard
import time
from datetime import datetime
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory(host='172.0.0.50')

motor_front = LED(17,pin_factory=factory)
motor_back = LED(18,pin_factory=factory)
motor_left = LED(23,pin_factory=factory)
motor_right = LED(25,pin_factory=factory)
lastKey = "none"

def proKeys(key):
    global lastKey
    #print(str(datetime.now().time()) + "> " + key + "\n")
    if(key == 'stop'):
        stopMotors()
    else:
        if (key == lastKey):
            print("keeping: " + key)

        else:
            print("changing to:" + key)
            lastKey = key
            stopMotors()
            if(key == "forward"):
                print("forward")
                motor_front.on()
            elif(key == "backward"):
                print("backward")
                motor_back.on()
            elif(key == "left"):
                print("left")
                motor_left.on()
            elif(key == "right"):
                print("right")
                motor_right.on()




def stopMotors():
    print("motors stopped : 5 sec lockoutstarted")
    motor_front.off()
    motor_back.off()
    motor_right.off()
    motor_left.off()
    print("motors stopped : 5 sec lockoutend")


motor_front.off()
motor_back.off()
motor_right.off()
motor_left.off()


while True:    
    try:
        if keyboard.is_pressed('w'): 
            proKeys("forward")
        elif keyboard.is_pressed('s'):
            proKeys("backward")
        elif keyboard.is_pressed('a'):
            proKeys("left")
        elif keyboard.is_pressed('d'):
            proKeys("right")
        elif keyboard.is_pressed('q'):
            proKeys("stop")

    except:
        print("error")

