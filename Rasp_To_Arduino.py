import serial
import time
import subprocess

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_signal():
    ser.write(b'O')

try:
    arduino_script = "path/to/your/arduino_script.ino"
    arduino_process = subprocess.Popen(["arduino", "--upload", arduino_script])

    time.sleep(10)

    send_signal()

finally:
    ser.close()
