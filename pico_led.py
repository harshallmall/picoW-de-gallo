# Pico blinking for internal and external LEDs
import machine
import utime
 
led_external = machine.Pin(15, machine.Pin.OUT)
led_internal = machine.Pin(25, machine.Pin.OUT)
 
while True:
    led_external.toggle()
    utime.sleep(5)
    led_internal.toggle()
    utime.sleep(5)