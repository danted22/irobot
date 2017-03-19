# Get your motors running...
# ... head out on the highway!

import time

# turn all motors off
def StopMotors():
    print("Stop")
    
# full impulse
def Forwards():
    print("Forwards")
    
# full reverse!
def Backwards():
    print("Backwards")
    
# turn right
def Right(hard=False):
    print("Right: " + hard)
    
# turn left
def Left(hard=False):
    print("Left: " + hard)
    
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
