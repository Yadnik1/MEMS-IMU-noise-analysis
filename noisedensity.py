import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

DATA_FILE = 'accel-gyro-data2.csv'
FS = 31.25 # Sample frequency [Hz]
MEAS_DUR_SEC =37500  # Seconds to record data for
TS = 1.0 / FS  # Sample period [s]

# Load into arrays, convert units
dataArr = np.genfromtxt(DATA_FILE, delimiter=',')
ax = dataArr[:, 0] * 9.80665  # m/s/s
ay = dataArr[:, 1] * 9.80665
az = dataArr[:, 2] * 9.80665
gx = dataArr[:, 3] * (180 / np.pi)  # deg/s
gy = dataArr[:, 4] * (180 / np.pi)
gz = dataArr[:, 5] * (180 / np.pi)

# Conversion factor: m/s/s -> ug (micro G's)
accel2ug = 1e6 / 9.80665

# Compute PSD via Welch algorithm
freqax, psdax = signal.welch(ax, FS, scaling='density')  # ax
freqay, psday = signal.welch(ay, FS, scaling='density')  # ay
freqaz, psdaz = signal.welch(az, FS, scaling='density')  # az

freqgx, psdgx = signal.welch(gx, FS,nperseg=1024,  scaling='density')  # gx
freqgy, psdgy = signal.welch(gy, FS,nperseg=1024, scaling='density')  # gy
freqgz, psdgz = signal.welch(gz, FS,nperseg=1024, scaling='density')  # gz

# Convert to [ug / sqrt(Hz)]
psdax = np.sqrt(psdax) * accel2ug
psday = np.sqrt(psday) * accel2ug
psdaz = np.sqrt(psdaz) * accel2ug

psdgx = np.sqrt(psdgx)
psdgy = np.sqrt(psdgy)
psdgz = np.sqrt(psdgz)

# Compute noise spectral densities
ndax = np.mean(psdax)
nday = np.mean(psday)
ndaz = np.mean(psdaz)
print('AX Noise Density: %f ug/sqrt(Hz)' % (ndax))
print('AY Noise Density: %f ug/sqrt(Hz)' % (nday))
print('AZ Noise Density: %f ug/sqrt(Hz)' % (ndaz))

ndgx = np.mean(psdgx)
ndgy = np.mean(psdgy)
ndgz = np.mean(psdgz)
print('GX Noise Density: %f dps/sqrt(Hz)' % (ndgx))
print('GY Noise Density: %f dps/sqrt(Hz)' % (ndgy))
print('GZ Noise Density: %f dps/sqrt(Hz)' % (ndgz))


# Plot accel. data
plt.figure()
plt.plot(freqax, psdax, label='ax')
plt.plot(freqay, psday, label='ay')
plt.plot(freqaz, psdaz, label='az')
plt.title('Accelerometer Noise Spectral Density')
plt.xlabel('Frequency [Hz]')
plt.ylabel(r'Spectral Density  $\mu g / \sqrt{Hz}$')
plt.legend()
plt.grid()

# Plot gyro data
plt.figure()
plt.plot(freqgx, psdgx, label='gx')
plt.plot(freqgy, psdgy, label='gy')
plt.plot(freqgz, psdgz, label='gz')
plt.title('Gyroscope Noise Spectral Density')
plt.xlabel('Frequency [Hz]')
plt.ylabel(r'Spectral Density  $dps / \sqrt{Hz}$')
plt.legend()
plt.grid()
plt.show()