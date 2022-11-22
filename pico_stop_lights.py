# Pico LED stop lights
import machine
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

while True:
    led_green.value(3)
    utime.sleep(3)
    led_green.value(0)
    led_yellow.value(3)
    utime.sleep(3)
    led_yellow.value(0)
    led_red.value(3)
    utime.sleep(5)
    led_red.value(0)