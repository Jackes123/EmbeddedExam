import RPi.GPIO as GPIO
import time

# set GPIO 17 to relay
RelayPin = 17

#Maximum allowed
Maximum = 5

# setup function for initialization
def RelaySetup():
    GPIO.setwarnings(False)
    # set the GPIO modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    # set RelayPin's mode to output and initial level to HIGH (5V)
    GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.LOW)

# function to shutdown the relay
def ShutdownRelay():
    GPIO.output(RelayPin, GPIO.HIGH)  # set relay pin to LOW (shut down)
    print("Relay is shut down")

# main program loop
def main():
    # Counter variable
    entry_counter = 0
    exit_counter = 0
    total_counter = 0

    # perform the setup
    RelaySetup()


    try:
        while True:
            # simulate a sensor reading
            entry_sensor_reading = get_entry_sensor_reading()
            exit_sensor_reading = get_exit_sensor_reading()


            if entry_sensor_reading:
                entry_counter += 1  # increment the counter
                total_counter += 1  # increment the total counter
                print("Person arrived. Counter:", entry_counter, "Maximum allowed:", Maximum)

                # check if the counter exceeds 5
                if entry_counter > Maximum:
                    ShutdownRelay()  # shut down the relay

            if exit_sensor_reading:
                exit_counter += 1  # increment the exit counter
                total_counter -= 1  # decrement the total counter
                print("Person detected at exit. Exit Counter:", exit_counter)

            print("Total Counter:", total_counter)


            time.sleep(1)  # wait for a short duration between readings

    except KeyboardInterrupt:
        GPIO.cleanup()  # clean up GPIO on keyboard interrupt

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