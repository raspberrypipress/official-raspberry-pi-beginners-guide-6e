from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]
    x = round(x)
    y = round(y)
    z = round(z)
    print("x={0}, y={1}, z={2}".format(x, y, z))