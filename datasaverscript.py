import csv
import serial
from serial import Serial

SERIAL_PORT = 'COM7'
SERIAL_BAUD = 576000
OUT_FILE = 'test.csv'
FS = 500 # Sample frequency [Hz]
MEAS_DUR_SEC = 1200  #Seconds to record data for

TS = 1.0 / FS  # Sample period [s]
N_SAMPLES = int(MEAS_DUR_SEC * FS)  # Number of samples to record

# Init. serial
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
ser.flush()

with open(OUT_FILE, newline='', mode='w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    for _ in range(N_SAMPLES):
        # Read serial stream and extract data
        dataList = ser.readline().decode('utf-8').strip('\r\n').split(',')

        # Write data to CSV file: gx,gy,gz
        csvwriter.writerow(dataList)