from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
orientation = sense.get_orientation()
pitch = orientation["pitch"]
roll = orientation["roll"]
yaw = orientation["yaw"]
print("Nicken {0} Rollen {1} Gieren {2}".format(pitch, roll, yaw))