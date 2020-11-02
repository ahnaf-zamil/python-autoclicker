from win32api import GetKeyState
from pynput.mouse import Button, Controller
import ctypes
import time
import threading
import sys
import logging

input("Press enter to start....")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:: %(levelname)s:: %(message)s')

# Accessing system info
user32 = ctypes.windll.user32

# Getting the monitor resolution
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Instantiating a mouse controller
logging.info("Instantiated mouse controller")
mouse = Controller()

# Checking keyboard input on all windows


def key_down():
    # Getting key state
    state = GetKeyState(113)  # 81 is the ASCII number for 'q'
    if (state != 0) and (state != 1):  # If the state is any number other than 0 and 1
        return True
    else:
        return False

# Main loop


def main():
    while True:
        # Pressing left key on mouse
        mouse.press(Button.left)
        # Sleeping for half second
        time.sleep(0.5)

# Main thread


def start_thread():
    # Making a thread instance
    logging.info("Creating main thread")
    th = threading.Thread(target=main)
    # Setting thread daemon mode
    logging.info("Setting thread daemon to 'true'")
    th.daemon = True
    # Starting thread
    logging.info("Starting thread")
    th.start()


# Starting thread
start_thread()
logging.info("Started thread")

# Making a while loop so that the thread stays active
while True:
    # Checking if 'q' is pressed on the keyboard
    if key_down():
        logging.info("Pressed 'q' on the keyboard")
        logging.info("Stopping all threads...")
        # Exiting program
        logging.info("Exiting program")
        sys.exit()
    # Sleeping for 1 second so that while loop doesn't consume a lot of cpu
    time.sleep(1)
