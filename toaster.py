import curses
from gpiozero import Robot
from gpiozero import PWMLED

robot = Robot(left=(17, 18), right=(23, 25))
servo = PWMLED(4)

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
