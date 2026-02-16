from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)