# Get your motors running...
# ... head out on the highway!

import RPi.GPIO as GPIO # import the GPIO library for controlling the Pi's pins
import time

# set GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set variables for motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# how many times to turn the pin on and off per second
Frequency = 20
# how long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# setting the duty cycle to 0 means the motors will not turn
Stop = 0

# set the GPIO pin mode
GPIO.setup(pinMotorBBackwards, GPIO.OUT) # left motor backwards
GPIO.setup(pinMotorBForwards, GPIO.OUT) # left motor forwards
GPIO.setup(pinMotorABackwards, GPIO.OUT) # right motor backwards
GPIO.setup(pinMotorAForwards, GPIO.OUT) # right motor forwards

# set the GPIO to software PWM at 'Frequency' hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# full impulse
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# full reverse!
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# turn right
def Right(hard=False):
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    if(hard == True):
        pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    else:
        pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorAForwards.ChangeDutyCycle(Stop)

# turn left
def Left(hard=False):
    if(hard == True):
        pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    else:
        pwmMotorBBackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)

move = {'forward'  : Forwards,
        'backward' : Backwards,
        'left'     : Left,
        'right'    : Right,
}

def Test(action):
    move[action]()
    time.sleep(1)
    StopMotors()
    return "Robot gonna do {}, ok?".format(action)
