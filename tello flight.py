from djitellopy import tello
from time import sleep



tello = tello.Tello()

# take off to 200cm
tello.takeoff()
tello.move_up(120)


# move forward 800cm
tello.move_forword(400)
tello.move_forword(400)
sleep(0.5)

# turn left and move 250cm
tello.rotate_counter_clockwise(90)
sleep(0.5)
tello.move_forward(250)

# turn again and move 800cm
tello.rotate_counter_clockwise(90)
sleep(0.5)
tello.move_forward(400)
tello.move_forword(400)
sleep(0.5)

# turn left move 250cm
tello.rotate_counter_clockwise(90)
sleep(0.5)
tello.move_forward(250)
sleep(0.5)

# land
tello.land(90)

