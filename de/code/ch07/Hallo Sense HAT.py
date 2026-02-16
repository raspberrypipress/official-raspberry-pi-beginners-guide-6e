from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

sense.show_message("Hallo Welt!", text_colour=(yellow),
                   back_colour=(blue), scroll_speed=(0.05))