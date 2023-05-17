import RPi.GPIO as GPIO
import time

#TEST#
#TEST#
#hashhas
#sda

RelayPin = 22 # set GPIO 17 to relay
EntryLEDPin = 14 # set GPIO led pins
ExitLEDPin = 23

#Entry sensor
TrigEntry = 4
EchoEntry = 27

#Exit sensor
TrigExit = 18
EchoEntry = 24

#Maximum people allowed
Maximum = 5

# setup function for initialization
def Setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # set the GPIO modes to BCM numbering
    GPIO.setup(EntryLEDPin, GPIO.OUT, initial=GPIO.LOW)  # setup entry LED pin
    GPIO.setup(ExitLEDPin, GPIO.OUT, initial=GPIO.LOW)  # setup exit LED pin
    GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)  # setup relay pin

def turn_on_led():
    GPIO.output(EntryLEDPin, GPIO.HIGH)
    GPIO.output(ExitLEDPin, GPIO.HIGH)

def turn_off_led():
    GPIO.output(EntryLEDPin, GPIO.LOW)
    GPIO.output(ExitLEDPin, GPIO.LOW)

#Dette gøres når max limit reaches
def MaxLimitDo():
    GPIO.output(RelayPin, GPIO.LOW)  # set relay pin to LOW (shut down)
    print("\nRelay is shut down")
    print("\nWarning: Maximum limit reached!")
    turn_on_led()
    

def main():

    entry_counter = 0
    exit_counter = 0
    total_counter = 0

    Setup()

    try:
        while True:
            # simulate a sensor reading
            entry_sensor_reading = get_entry_sensor_reading()
            exit_sensor_reading = get_exit_sensor_reading()

            print("______________________________________________________")
    
            print("\nMaximum people allowed in this building:", Maximum)

            if entry_sensor_reading:
                entry_counter += 1  # increment the counter
                total_counter += 1  # increment the total counter
                print("\nPerson detected at entry. Counter:", entry_counter)

                # check if the counter exceeds 5
                if total_counter >= Maximum:
                    MaxLimitDo()

            if exit_sensor_reading:
               exit_counter += 1  # increment the exit counter
#               total_counter -= 1  # decrement the total counter
#               print("\nPerson detected at exit. Exit Counter:", exit_counter)

            print("\nTotal Counter:", total_counter)

            #Sluk LED igen hvis den er under max
            if total_counter < Maximum:
                turn_off_led()
                GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)

            time.sleep(1)  # wait for a short duration between readings

    except KeyboardInterrupt:
        GPIO.cleanup()

# function to simulate an entry sensor reading (replace this with your actual sensor code)
def get_entry_sensor_reading():
    # Simulate the entry sensor reading
    # Replace this with your actual entry sensor reading code
    return True  # returning True to simulate a person detected at the entry

# function to simulate an exit sensor reading (replace this with your actual sensor code)
def get_exit_sensor_reading():
    # Simulate the exit sensor reading
    # Replace this with your actual exit sensor reading code
    return True  # returning True to simulate a person detected at the exit

if __name__ == '__main__':
    main()