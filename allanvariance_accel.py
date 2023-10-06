import numpy as np
import matplotlib.pyplot as plt


# Config. params
DATA_FILE = 'accel-gyro-data2.csv'  # CSV data file "gx,gy,gz"
fs = 500  # Sample rate [Hz]
def AllanDeviation(dataArr: np.ndarray, fs: float, maxNumM: int=100):

    ts = 1.0 / fs
    N = len(dataArr)
    Mmax = 2**np.floor(np.log2(N / 2))
    M = np.logspace(np.log10(1), np.log10(Mmax), num=maxNumM)
    M = np.ceil(M)  # Round up to integer
    M = np.unique(M)  # Remove duplicates
    taus = M * ts  # Compute 'cluster durations' tau

    # Compute Allan variance
    allanVar = np.zeros(len(M))
    for i, mi in enumerate(M):
        twoMi = int(2 * mi)
        mi = int(mi)
        allanVar[i] = np.sum(
            (dataArr[twoMi:N] - (2.0 * dataArr[mi:N-mi]) + dataArr[0:N-twoMi])**2
        )
    
    allanVar /= (2.0 * taus**2) * (N - (2.0 * M))
    return (taus, np.sqrt(allanVar))  # Return deviation (dev = sqrt(var))
dataArr = np.genfromtxt(DATA_FILE, delimiter=',')
ts = 1.0 / fs

# Separate into arrays
ax = dataArr[:, 0] * 9.80665  # m/s/s
ay = dataArr[:, 1] * 9.80665  
az = dataArr[:, 2] * 9.80665  


thetax = np.cumsum(ax) * ts # [deg]
thetay = np.cumsum(ay) * ts 
thetaz = np.cumsum(az) * ts 

# Compute Allan deviations
(taux, adx) = AllanDeviation(thetax, fs, maxNumM=200)
(tauy, ady) = AllanDeviation(thetay, fs, maxNumM=200)
(tauz, adz) = AllanDeviation(thetaz, fs, maxNumM=200)

# Plot data on log-scale
plt.figure()
plt.title('Accel Allan Deviations')
plt.plot(taux, adx, label='ax')
plt.plot(tauy, ady, label='ay')
plt.plot(tauz, adz, label='az')
plt.xlabel(r'$\tau$ [sec]')
plt.ylabel('Deviation [m/s2]')
plt.grid(True, which="both", ls="-", color='0.65')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show()

slope_intercept = np.polyfit(taux,adx,1)

print(slope_intercept)