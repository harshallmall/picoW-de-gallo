# Pico outputting the value of a button when pushed or not
import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("The button has been pressed.")
        utime.sleep(2)