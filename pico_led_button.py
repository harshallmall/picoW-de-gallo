# Pico outputting text and both LEDs when button is pressed
import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
led_internal = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("The button has been pressed.")
        led_external.value(1)
        utime.sleep(2)
        led_internal.value(1)
        utime.sleep(2)
    led_external.value(0)
    led_internal.value(0)