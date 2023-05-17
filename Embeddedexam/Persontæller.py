import RPi.GPIO as GPIO
import time

RelayPin = 22 # set GPIO 17 to relay
EntryLEDPin = 14 # set GPIO led pins
ExitLEDPin = 23

#Entry sensor
TrigEntry = 4
EchoEntry = 27
EntryThreshold = 10

#Exit sensor
TrigExit = 18
EchoExit = 24
ExitThrehold = 10

#Maximum people allowed
Maximum = 5

# setup function for initialization
def Setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # set the GPIO modes to BCM numbering
    GPIO.setup(EntryLEDPin, GPIO.OUT, initial=GPIO.LOW)  # setup entry LED pin
    GPIO.setup(ExitLEDPin, GPIO.OUT, initial=GPIO.LOW)  # setup exit LED pin
    GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)  # setup relay pin
    GPIO.setup(TrigEntry, GPIO.OUT)
    GPIO.setup(EchoEntry, GPIO.IN)
    GPIO.setup(TrigExit, GPIO.OUT)
    GPIO.setup(EchoExit, GPIO.IN)

def turn_on_led():
    GPIO.output(EntryLEDPin, GPIO.HIGH)
    GPIO.output(ExitLEDPin, GPIO.HIGH)

def turn_off_led():
    GPIO.output(EntryLEDPin, GPIO.LOW)
    GPIO.output(ExitLEDPin, GPIO.LOW)

#Dette gøres når max limit reaches
def MaxLimitDo():
    GPIO.output(RelayPin, GPIO.LOW)  # set relay pin to LOW (shut down)
    print("\nRelay is shut down", end = "\r")
    print("\nWarning: Maximum limit reached!", end = "\r")
    turn_on_led()
    
def RegPrint():
    print("\n______________________________________________________", end = "\r")
    print("\nMaximum people allowed in this building:", Maximum, end = "\r")
 

def Get_distance(trig_pin,echo_pin):
    #Send pulse
    GPIO.output (trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output (trig_pin, GPIO.LOW)


    pulse_start = time.time()
    
    #Vent på respons
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()


    #Udregn distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150 #Speed of sound
    distance = round(distance, 2) #Runder til 2 decimaler

    return distance    



def main():

    #entry_counter = 0
    #exit_counter = 0
    total_counter = 0

    Setup()

    try:
        while True:
            # simulate a sensor reading
            entry_sensor_reading = Get_distance(TrigEntry, EchoEntry)
            exit_sensor_reading = Get_distance(TrigExit, EchoExit)

            if entry_sensor_reading < EntryThreshold:
                #entry_counter += 1  # increment the counter
                total_counter += 1  # increment the total counter
                #print("\nPerson detected at entry. Counter:", entry_counter,"\r")
                RegPrint()
                print("\nTotal Counter:", total_counter, end = "\r")

                # check if the counter exceeds 5
                if total_counter >= Maximum:
                    MaxLimitDo()

            if exit_sensor_reading < ExitThrehold:
                #exit_counter += 1  # increment the exit counter
                total_counter -= 1  # decrement the total counter
                #print("\nPerson detected at exit. Exit Counter:", exit_counter,"\r")
                RegPrint()
                print("\nTotal Counter:", total_counter, end = "\r")
            

            #Sluk LED igen hvis den er under max
            if total_counter < Maximum:
                turn_off_led()
                GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)

            time.sleep(1)  # wait for a short duration between readings

    except KeyboardInterrupt:
        GPIO.cleanup()
    time.sleep(1)

if __name__ == '__main__':
    main()