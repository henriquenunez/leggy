from controller import Robot

# Create the robot instance
robot = Robot()

# Get references to Spot's motors
# Front left leg
front_left_abduction_motor = robot.getDevice('front left shoulder abduction motor')
front_left_rotation_motor = robot.getDevice('front left shoulder rotation motor')
front_left_elbow_motor = robot.getDevice('front left elbow motor')

# Front right leg
front_right_abduction_motor = robot.getDevice('front right shoulder abduction motor')
front_right_rotation_motor = robot.getDevice('front right shoulder rotation motor')
front_right_elbow_motor = robot.getDevice('front right elbow motor')

# Rear left leg
rear_left_abduction_motor = robot.getDevice('rear left shoulder abduction motor')
rear_left_rotation_motor = robot.getDevice('rear left shoulder rotation motor')
rear_left_elbow_motor = robot.getDevice('rear left elbow motor')

# Rear right leg
rear_right_abduction_motor = robot.getDevice('rear right shoulder abduction motor')
rear_right_rotation_motor = robot.getDevice('rear right shoulder rotation motor')
rear_right_elbow_motor = robot.getDevice('rear right elbow motor')

# Enable the motor position sensors
# front_left_abduction_motor.enablePosition(64)
# front_left_rotation_motor.enablePosition(64)
# front_left_elbow_motor.enablePosition(64)

# front_right_abduction_motor.enablePosition(64)
# front_right_rotation_motor.enablePosition(64)
# front_right_elbow_motor.enablePosition(64)

# rear_left_abduction_motor.enablePosition(64)
# rear_left_rotation_motor.enablePosition(64)
# rear_left_elbow_motor.enablePosition(64)

# rear_right_abduction_motor.enablePosition(64)
# rear_right_rotation_motor.enablePosition(64)
# rear_right_elbow_motor.enablePosition(64)

# Set the maximum motor velocity
max_velocity = front_left_abduction_motor.getMaxVelocity()

# Walking parameters
step_duration = 1.0  # Duration of each step
step_amplitude = 0.5  # Amplitude of the step movement

"""
# Walk to the right
def walk_right():
    # Move the right legs forward
    front_right_abduction_motor.setPosition(step_amplitude)
    rear_right_abduction_motor.setPosition(step_amplitude)
    
    # Move the left legs backward
    front_left_abduction_motor.setPosition(-step_amplitude)
    rear_left_abduction_motor.setPosition(-step_amplitude)

# Walk to the left
def walk_left():
    # Move the left legs forward
    front_left_abduction_motor.setPosition(step_amplitude)
    rear_left_abduction_motor.setPosition(step_amplitude)
    
    # Move the right legs backward
    front_right_abduction_motor.setPosition(-step_amplitude)
    rear_right_abduction_motor.setPosition(-step_amplitude)

# Walk to the right
def walk_right():
    # Move the right legs forward using rotation motors
    front_right_rotation_motor.setPosition(step_amplitude)
    rear_right_rotation_motor.setPosition(step_amplitude)
    
    # Move the left legs backward using rotation motors
    front_left_rotation_motor.setPosition(-step_amplitude)
    rear_left_rotation_motor.setPosition(-step_amplitude)

# Walk to the left
def walk_left():
    # Move the left legs forward using rotation motors
    front_left_rotation_motor.setPosition(step_amplitude)
    rear_left_rotation_motor.setPosition(step_amplitude)
    
    # Move the right legs backward using rotation motors
    front_right_rotation_motor.setPosition(-step_amplitude)
    rear_right_rotation_motor.setPosition(-step_amplitude)

# Walk to the right
def walk_right():
    # Move the right legs forward using rotation motors
    front_right_rotation_motor.setPosition(step_amplitude)
    rear_right_rotation_motor.setPosition(step_amplitude)
    
    # Move the left legs backward using rotation motors
    front_left_rotation_motor.setPosition(-step_amplitude)
    rear_left_rotation_motor.setPosition(-step_amplitude)
    
    # Activate the elbow motors
    front_right_elbow_motor.setPosition(-step_amplitude)
    rear_right_elbow_motor.setPosition(-step_amplitude)
    front_left_elbow_motor.setPosition(step_amplitude)
    rear_left_elbow_motor.setPosition(step_amplitude)

# Walk to the left
def walk_left():
    # Move the left legs forward using rotation motors
    front_left_rotation_motor.setPosition(step_amplitude)
    rear_left_rotation_motor.setPosition(step_amplitude)
    
    # Move the right legs backward using rotation motors
    front_right_rotation_motor.setPosition(-step_amplitude)
    rear_right_rotation_motor.setPosition(-step_amplitude)
    
    # Activate the elbow motors
    front_right_elbow_motor.setPosition(step_amplitude)
    rear_right_elbow_motor.setPosition(step_amplitude)
    front_left_elbow_motor.setPosition(-step_amplitude)
    rear_left_elbow_motor.setPosition(-step_amplitude)
"""

# Walk to the right
def walk_right():
    # Move the right legs forward using rotation motors
    front_right_rotation_motor.setPosition(step_amplitude)
    rear_left_rotation_motor.setPosition(step_amplitude)
    
    # Move the left legs backward using rotation motors
    front_left_rotation_motor.setPosition(-step_amplitude)
    rear_right_rotation_motor.setPosition(-step_amplitude)
    
    # Activate the elbow motors
    front_right_elbow_motor.setPosition(-step_amplitude)
    rear_left_elbow_motor.setPosition(-step_amplitude)

    front_left_elbow_motor.setPosition(step_amplitude)
    rear_right_elbow_motor.setPosition(step_amplitude)

# Walk to the left
def walk_left():
    # Move the left legs forward using rotation motors
    front_left_rotation_motor.setPosition(step_amplitude)
    rear_right_rotation_motor.setPosition(step_amplitude)
    
    # Move the right legs backward using rotation motors
    front_right_rotation_motor.setPosition(-step_amplitude)
    rear_left_rotation_motor.setPosition(-step_amplitude)
    
    # Activate the elbow motors
    front_right_elbow_motor.setPosition(step_amplitude)
    rear_left_elbow_motor.setPosition(step_amplitude)
    front_left_elbow_motor.setPosition(-step_amplitude)
    rear_right_elbow_motor.setPosition(-step_amplitude)



def walk_1():
    rear_left_rotation_motor.setPosition(-step_amplitude)
    rear_left_elbow_motor.setPosition(step_amplitude)

def walk_2():
    front_left_rotation_motor.setPosition(-step_amplitude)
    front_left_elbow_motor.setPosition(step_amplitude)

def walk_3():
    rear_right_rotation_motor.setPosition(-step_amplitude)
    rear_right_elbow_motor.setPosition(step_amplitude)

def walk_4():
    front_right_rotation_motor.setPosition(-step_amplitude)
    front_right_elbow_motor.setPosition(step_amplitude)

def walk():
    walk_1()
    walk_2()
    walk_3()
    walk_4()
"""
# Main control loop
while robot.step(64) != -1:
    # Execute walk_right for a certain duration
    walk_right()
    robot.step(int(step_duration * 1000))
    
    # Execute walk_left for a certain duration
    walk_left()
    robot.step(int(step_duration * 1000))
"""

# Initial setup
front_left_abduction_motor.setPosition(0)
front_right_abduction_motor.setPosition(0)
rear_left_abduction_motor.setPosition(0)
rear_right_abduction_motor.setPosition(0)

step_amplitude = 0.45

# Raise front
def raise_front():
    front_right_rotation_motor.setPosition(step_amplitude)
    front_right_elbow_motor.setPosition(-step_amplitude)

    front_left_rotation_motor.setPosition(step_amplitude)
    front_left_elbow_motor.setPosition(-step_amplitude)
    
def lower_front():
    rear_right_rotation_motor.setPosition(step_amplitude / 2)
    rear_right_elbow_motor.setPosition(-step_amplitude / 2)

    rear_left_rotation_motor.setPosition(step_amplitude / 2)
    rear_left_elbow_motor.setPosition(-step_amplitude / 2)

    front_right_rotation_motor.setPosition(-step_amplitude)
    front_right_elbow_motor.setPosition(1.6)

    front_left_rotation_motor.setPosition(-step_amplitude)
    front_left_elbow_motor.setPosition(1.6)

# Main control loop
while robot.step(64) != -1:
    raise_front()
    robot.step(int(step_duration * 1000))
    lower_front()
    robot.step(int(step_duration * 1000))
