from gpiozero import LED
from time import sleep

#PINs dos LEDs
pin = LED(14)


while 1:
	pin.on() 	#Led 3 on
	sleep(1)
	pin.off()
	sleep(1)

