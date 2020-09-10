# ------------------------------------------
# 
# 	Project:  PYTHON RedSmallStateScrimmage1
#	Author:
#	Created:
#	Configuration:
# 
# ------------------------------------------

# Based on C++ version located here:
# https://raw.githubusercontent.com/FVR-Endermen/355R-2019-2020/master/preStateScrimmage1/RedSmallStateScrimmage1/src/main.cpp


# Library imports
from vex import *

# global constants 

wheel_radius_in_inches = 2.0
Pi = 3.14159267

"""
 something to measure -- its the diagonal distance between wheels
 through the CENTER of the robot.  DIAMETER of the robot
 Note this is something we end up tuning -- it would probably be
 exactly the diagonal for ideal wheels, but the mecanums slip a bit
 Currently calibrate by what number we need for a 180 degree turn to
 actually turn 180 degrees!
"""
diag_wheel_base_in_inches = 22.0

stop_feeder = True

 


# Begin project code

def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

#  Get more of the feeder lower
    #LiftStacker(0.1,true);

    feeder_action(55,True)


    # These were a test -- don't use!

    # strafe(20.0,50)
    # strafe (-20.0,50)

# the howfast numbers used to be RPM, now apparently its percent

    move_forward(15.0,75)
    move_forward(2.0,65)
    move_forward(29.0,25)

    #vex.wait(500)

    #feeder_action(46,True)
    # stop feeder before turning

    #lift_stacker(0.1, False)

    feeder_action(20,True)

    # rotate_clockwise(210.0)
    rotate_clockwise(180.0,85)

    move_forward(25.5, 100)

    rotate_clockwise(-45.5, 65)

    # vex.wait(1000)
    # feeder_action(50, True)
    move_forward(16.3, 100)

    feeder_action(0,false)

    move_forward(7.0,35)

    move_forward(-0.5,35)

    lift_stacker(3.75,true)

    move_forward(-20.0,20)

    # old place steps
    # lift_stacker(2.0,True)

    # feeder_action(40,False)
    # lift_stacker(1.0,False)

    # With new feeder

 """   

    lift_stacker(1.0, True)
    move_forward(-1.0,20)
    lift_stacker(0.5,True)
    move_forward(-1.0,20)
    lift_stacker(0.5,True)
    move_forward(-1.0,20)
    lift_stacker(0.1,True)
    move_forward(-1.0,20)
    lift_stacker(0.1,True)
    move_forward(-1.0,20)

    #lift_stacker(0.5,True)
    #lift_stacker(0.5,True)
    
    lift_stacker(0.8,True)
    # feeder_action(10,False)
    lift_stacker(1.15,True)

    # feeder_action(20,False)
    # vex.wait(500)

    feeder_action(40,False)
    lift_stacker(2.2.False)
    # lift_stacker(-2.2,True)
    feeder_action(0,True)

"""


def user_control():

    #Deadband stops the motors when Axis values are close to zero.
    deadband = 5

    #How fast the feeder motors will spin
    feeder_speed = 50
    lifter_speed = 15

    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:

        # SIMPLE TANK DRIVE

        # Get the velocity percentage of the left motor. (Axis 3)
        left_motor_speed = controller_1.axis3.position()
        # Get the velocity percentage of the right motor. (Axis 2)
        right_motor_speed = controller_1.axis2.position()

        # what is the state of button L1
        l1_down = controller_1.buttonL1.pressing()

        # what is the state of button R1
        r1_down = controller_1.buttonR1.pressing()

        # what is the state of button L2
        l2_down = controller_1.buttonL2.pressing()

        # what is the state of button R2
        r2_down = controller_1.buttonR2.pressing()

        up_arrow_pushed = controller_1.buttonUp.pressing()
        down_arrow_pushed = controller_1.buttonDown.pressing()

        # Set the speed of the left motor. If the value is less than the deadband,
        # set it to zero.

        if (abs(left_motor_speed) < deadband):
            # set the speed to zero
            left_front_motor.set_velocity(0, PERCENT)
            left_back_motor.set_velocity(0, PERCENT)

        else:
            # set to left_motor_speed
            left_front_motor.set_velocity(left_motor_speed, PERCENT)
            left_back_motor.set_velocity(left_motor_speed, PERCENT)

        # Set the speed of the right motor. If the value is less than the deadband,
        # set it to zero.

        if (abs(right_motor_speed) < deadband):
            # set the speed to zero
            right_front_motor.set_velocity(0, PERCENT)
            right_back_motor.set_velocity(0, PERCENT)

        else:
            # set to right_motor_speed
            right_front_motor.set_velocity(right_motor_speed, PERCENT)
            right_back_motor.set_velocity(right_motor_speed, PERCENT)

        # spin both motors in the forward direction

        left_front_motor.spin(forward)
        right_front_motor.spin(forward)
        left_back_motor.spin(forward)
        right_back(motor.spin(forward)


        # Feeder L1 and R1

        # stop motors if nobody is pressed or if BOTH are pressed

        if ( (not(l1_down) && not(r1_down))  ||  (l1_down && r1_down) ):
            feeder_left_motor.set_velocity(0,PERCENT)
            feeder_right_motor.set_velocity(0,PERCENT)
        else if (l1_down && not(r1_down)):
            feeder_left_motor.set_velocity(feeder_speed, PERCENT)
            feeder_right_motor.set_velocity(feeder_speed, PERCENT)
        else if (r1_down && not(l1_down)):
            feeder_left_motor.set_velocity(-feeder_speed, PERCENT)
            feeder_right_motor.set_velocity(-feeder_speed, PERCENT)
        else: 
            feeder_left_motor.set_velocity(0,PERCENT)
            feeder_right_motor.set_velocity(0,PERCENT) 

        # now that they are set, spin the feeder motors

        feeder_left_motor.spin(FORWARD)
        feeder_right_motor.spin(FORWARD)


        # similar logic for the lift motor


        if ( (not(l2_down) && not(r2_down))  ||  (l2_down && r2_down) ):
            lift_motor.set_velocity(0,PERCENT)
        else if (l2_down && not(r2_down)):
            lift_motor.set_velocity(feeder_speed, PERCENT)
        else if (r2_down && not(l2_down)):
            lift_motor.set_velocity(-feeder_speed, PERCENT)
        else: 
            lift_motor.set_velocity(0,PERCENT)

        # now that it is set, spin the lift motor

        lift_motor.spin(FORWARD)


        # up and down motors


       if ( (not(up_arrow_pushed) && not(down_arrow_pushed))  ||  (up_arrow_pushed && down_arrow_pushed) ):
            rack_n_pinion_motor.set_velocity(0,PERCENT)
        # up arrow tilts it up
        else if (up_arrow_pushed && not(down_arrow_pushed)):
            rack_n_pinion_motor.set_velocity(lifter_speed, PERCENT)
            # try and force the feeder down as we lift up
            lift_motor.set_velocity(feeder_speed, PERCENT)
        # down arrow tilts it down
        else if (down_arrow_pushed && not(up_arrow_pushed)):
            rack_n_pinion_motor.set_velocity(-lifter_speed, PERCENT)
        else: 
            rack_n_pinion_motor.set_velocity(0,PERCENT)

        # now that it is set, spin the lift motor

        rack_n_pinion_motor.spin(FORWARD)
        lift_motor.spin(FORWARD)

        wait(20, MSEC)




# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()

# testing to see what happens with the json file format if I 
# make something that has a \n\n\n\n in it

#print ("this \n is \n a \n set \n newlines \n")


def lift_stacker(n_rotations=0, direction=True):
    rack_and_pinion_angle = n_rotations * 360.0
    if (direction):
        # Get lift motor(s) pushing down
        lift_motor.set_velocity(20.0, PERCENT)
        lift_motor.spin(FORWARD)
        # Then push up rack
        rack_n_pinion_motor.spin_to_position(rack_and_pinion_angle, DEGREES, True)
        # Stop lift motor
        lift_motor.set_velocity(0.0, PERCENT)
        lift_motor.spin(FORWARD)
    else:
        rack_n_pinion_motor.spin_to_position(-rack_and_pinion_angle, DEGREES, True)

    rack_n_pinion_motor.set_position(0,DEGREES)



def feeder_action(feeder_speed=0, direction=True):
    if (direction):
        feeder_left_motor.set_velocity(feeder_speed,PERCENT)
        feeder_right_motor.set_velocity(feeder_speed,PERCENT)
        feeder_left_motor.spin(FORWARD)
        feeder_right_motor.spin(FORWARD)
    else:
        feeder_left_motor.set_velocity(-feeder_speed,PERCENT)
        feeder_right_motor.set_velocity(-feeder_speed,PERCENT)
        feeder_left_motor.spin(FORWARD)
        feeder_right_motor.spin(FORWARD)  



# Function to move forward, howfar is in INCHES

def move_forward(howfar, howfast):

# need to convert inches to number of rotations and then to degrees
# number of rotations is how many circumferences the argument howfar is

    n_rotations = howfar / Pi / wheel_radius_in_inches / 2.0
    rotation_degrees = n_rotations * 360.0

# motion speed

# in v1.01 this was in rpm -- apparently in the python api this is now PERCENT
    motor_velocity = howfast

"""
What this is doing:
spinToPosition tells it to spin the wheel until it hits the requested position
the second argument is "degrees" which is a constant that tells it the angle is
in -- believe it or not -- degrees
the last argument tells it to wait or not before moving to the next one.
The default is true.  This means if we leave the default with the four statements
below, it will rotate the first wheel, then the next, then the next, and the last
If we set false, it will get the motor started, then move on to the next statement.
So here we set the first 3 to false, but the last one to true.  This should
move all 4 at essentially the same time, but wait until the last one is done.
It should move the drivetrain as a whole here.
"""

# it will be interesting if this still works -- 
    left_front_motor.spin_to_position(rotation_degrees, DEGREES, motorvelocity, PERCENT, False) # false keeps spinning
    right_front_motor.spin_to_position(rotation_degrees, DEGREES, motorvelocity, PERCENT, False) # also False
    left_back_motor.spin_to_position(rotation_degrees, DEGREES, motorvelocity, PERCENT, False) # also False
    right_back_motor.spin_to_position(rotation_degrees, DEGREES, motorvelocity, PERCENT, True) # now True to stop

# attempt to re-set motor encoder 

    left_front_motor.set_position(0,DEGREES)
    right_front_motor.set_position(0,DEGREES)
    left_back_motor.set_position(0,DEGREES)
    right_back_motor.set_position(0,DEGREES)






# Function to strafe (comes from MoveForward), howfar is in INCHES
# Positive is to the right, negative to the left

def strafe(howfar=0, howfast=0):

# need to convert inches to number of rotations and then to degrees 
# number of rotations is how many circumferences the argument howfar is

    n_rotations = howfar / Pi / wheel_radius_in_inches / 2.0
    rotation_degrees = n_rotations * 360.0

#  motion speed

    motor_velocity = howfast

"""
 What this is doing:
 spinToPosition tells it to spin the wheel until it hits the requested position
 the second argument is "degrees" which is a constant that tells it the angle is
 in -- believe it or not -- degrees
 the last argument tells it to wait or not before moving to the next one.
 The default is true.  This means if we leave the default with the four statements
 below, it will rotate the first wheel, then the next, then the next, and the last
 If we set false, it will get the motor started, then move on to the next statement.
 So here we set the first 3 to false, but the last one to true.  This should
 move all 4 at essentially the same time, but wait until the last one is done.
 It should move the drivetrain as a whole here.

 Now modified this to strafe -- which is moving left to right.  To do that
 make the front and back wheels move in opposite directions.Brain

 Move right =
  RightFrontMotor reverse
  RightBackMotor  forward
  LeftFrontMotor  forward
  LeftBackMotor   reverse

  Changing sign of nRotations to do this
"""

    left_front_motor.spin_to_position(rotation_degrees, DEGREES, motor_velocity, PERCENT, False) # False keeps spinning
    right_front_motor.spin_to_position(-rotation_degrees, DEGREES, motor_velocity, PERCENT, False) # also False
    left_back_motor.spin_to_position(-rotation_degrees, DEGREES, motor_velocity, PERCENT, False) # also False
    right_back_motor.spin_to_position(rotation_degrees, DEGREES, motor_velocity, PERCENT, True) # now True

 # attempt to re-set motor encoder 

    left_front_motor.set_position(0,DEGREES)
    right_front_motor.set_position(0,DEGREES)
    left_back_motor.set_position(0,DEGREES)
    right_back_motor.set_position(0,DEGREES)


# Function to rotate the robot clockwise, howfar is in DEGREES

def rotate_clockwise(howfar=0, howfast=0):

"""
 The idea is to rotate the motors enough to have them travel along
 the circumference of the circle drawn by the wheels around the
 center of the robot.
"""

    robot_circumference = Pi * diag_wheel_base_in_inches

# now we convert howfar into a number of ROBOT rotations

    robot_rotations = howfar / 360.0

# how many wheel rotations is one robot rotation

    wheel_circumference = Pi * wheel_radius_in_inches * 2.0

# how many times the wheel goes around to travel the circumference (one robot rotation)

    wheel_rotations_in_robot_rotation = robot_circumference / wheel)circumference

# to turn clockwise, left wheels drive forward, right wheels drive backward

    wheel_rotations = robot_rotations * wheel_rotations_in_robot_rotation

# and back to degrees

    left_wheel_degrees = wheel_rotations * 360.0
    right_wheel_degrees = 0.0 - left_wheel_degrees

# now we drive!

    left_front_motor.spin_to_position(left_wheel_degrees,DEGREES, False)
    left_back_motor.spin_to_position(left_wheel_degrees,DEGREES, False)

    right_front_motor.spin_to_position(right_wheel_degrees, DEGREES, False)
    right_back_motor.spin_to_position(right_wheel_degrees, DEGREES, True)


# attempt to re-set motor encoder 

    left_front_motor.set_position(0,DEGREES)
    right_front_motor.set_position(0,DEGREES)
    left_back_motor.set_position(0,DEGREES)
    right_back_motor.set_position(0,DEGREES)
