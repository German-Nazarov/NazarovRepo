import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def TroykaOut():
    troykaVlt = GPIO.input(troyka)
    print (troykaVlt)

def ToBinary(num):
    ans = [int(x) for x in bin(num)[2::].zfill(8)]
    return ans
    #print(ans)
    #GPIO.output(led, ans)

def adc():
    signal1 = 128
    signal2 = 64
    answer = 0

    for i in range(8):
        signal = ToBinary(int(answer))
        GPIO.output(dac, signal)
        time.sleep(0.01)
        compvalue = GPIO.input(comp)
        if (compvalue == 0):
            if (answer != 0):
                answer -= signal1
        else:
            answer += signal1
        
        signal1/=2
        signal2/=2
    lst=ToBinary(int(answer))
    voltage = float(int(3.3*answer/256*100)/100)
    x = voltage/3.3*8
    GPIO.output(led[i], 0)
    for i in range(8):
        if i<x:
            GPIO.output(led[i], 1)
        else:
            GPIO.output(led[i], 0)
    return int(answer)

Tz = time.time()
times = []
volts = []

try:
    if (adc() > 80):
        while adc() > 80:
            times.append(time.time() - Tz)
            real_volt = float(int(3.3*adc()/256*100)/100)
            volts.append(real_volt)
            print(adc(), time.time() - Tz)
    
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

    if (adc() < 220):
        while adc() < 220:
            times.append(time.time() - Tz)
            real_volt = float(int(3.3*adc()/256*100)/100)
            volts.append(real_volt)
            print(adc(), time.time() - Tz)
    
finally:
    plt.plot(volts)
    plt.show()
    print ("Time:", times[-1])
    print ("Period", times[-1]/len(times))
    print ("Freq", len(times)/times[-1])
    print ("Quant", 3.3 / 256)

    GPIO.output(dac, 0)

    with open ("time.txt", "w") as tms:
        for i in range (len(times)):
            tms.write(str(times[i])+'\n')

    with open ("volt.txt", "w") as vlts:
        for i in range (len(volts)):
            vlts.write(str(volts[i])+'\n')
    
    
    GPIO.cleanup()