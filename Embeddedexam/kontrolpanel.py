import RPi.GPIO as GPIO
import time

# set GPIO 17 to relay
RelayPin = 17

# Maximum allowed
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

# function to print a warning when maximum limit is exceeded
def print_warning():
    print("Warning: Maximum occupancy limit exceeded!")

# main program loop
def main():
    # Counter variables
    entry_counter = 0
    exit_counter = 0
    total_counter = 6
    max_exceeded = False

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
                print("\nPerson arrived. Counter:", entry_counter)

                if total_counter > Maximum and not max_exceeded:
                    ShutdownRelay()  # shut down the relay
                    print_warning()
                    max_exceeded = True

            if exit_sensor_reading:
                exit_counter += 1  # increment the exit counter
                total_counter -= 1  # decrement the total counter
                print("\nPerson detected at exit. Exit Counter:", exit_counter)

                if total_counter <= Maximum and max_exceeded:
                    max_exceeded = False

            if max_exceeded:
                print("\nTotal Counter:", total_counter)

            time.sleep(1)  # wait for a short duration between readings

    except KeyboardInterrupt:
        GPIO.cleanup()  # clean up GPIO on keyboard interrupt

# function to simulate an entry sensor reading (replace this with your actual sensor code)
def get_entry_sensor_reading():
    # Simulate the entry sensor reading
    # Replace this with your actual entry sensor reading code
    return False  # returning True to simulate a person detected at the entry

# function to simulate an exit sensor reading (replace this with your actual sensor code)
def get_exit_sensor_reading():
    # Simulate the exit sensor reading
    # Replace this with your actual exit sensor reading code
    return False  # returning True to simulate a person detected at the exit

if __name__ == '__main__':
    main()
