import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def binary(n):
    ans = [int(x) for x in bin(n)[2::].zfill(8)]
    return ans

dac_v = binary(128)
GPIO.output(dac, dac_v)


try:
    while True:
        print(GPIO.input(comp))

finally:
    GPIO.output(dac, binary(0))
    GPIO.cleanup()