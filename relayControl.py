import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relayNum = [17]
timeDelay = int(6)

def relay(x, y):
        f = open("relayLog.txt", "a")
        t0 = time.time()
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        print("Relay" + str(x) +" = TRUE")
        isTrue = True
        f.write("Relay num." + str(relayNum[0]) + " is " + str(isTrue) + " at the time " + str(datetime.datetime.now()) + "\n")
        time.sleep(y)
        GPIO.output(x, GPIO.LOW)
        print("Relay" + str(x) + " = FALSE")
        isTrue = False
        f.write("Relay num." + str(relayNum[0]) + " is " + str(isTrue) + " at the time " + str(datetime.datetime.now()) + "\n")
        t1 = time.time()
        total = t1-t0
        f.close()
        return round(total, 1)

print("Proces trval "  + str(relay(relayNum[0], timeDelay))+ "s.\n" + "Kontakt c. " + str(relayNum[0]) + " a delayem" + " " + str(timeDelay))

