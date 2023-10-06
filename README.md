# MEMS-IMU-noise-analysis

## Calibration and Data Processing for IMU in Telematics

### 1. Introduction:
The calibration and precise processing of IMU data are foundational for determining the insurance premium of car users in telematics. The data from IMUs, when evaluated correctly, gives insights into driving behavior, helping insurance companies implement "Pay As You Drive" and "Pay How You Drive" models.

### 2. Allan Variance: 
Allan Variance is a method that offers an understanding of the underlying noise characteristics in IMUs.
Allan variance measures the frequency stability of oscillations for a sequence of data in the time domain. This makes it especially valuable for IMUs as they're often plagued by different types of noise.

#### Identifying IMU Noise Characteristics:

- **White Noise:** A stochastic process with a constant power density across frequencies. In the context of an Allan Variance plot, it manifests as a flat line, indicating that the noise is evenly distributed across all frequency ranges.

- **Bias Instability:** Represents the stability of a device's bias over time. It is depicted as the minimum variance on the Allan Variance plot, denoting the time interval where the sensor achieves the best stability. This point reflects the most stable state of the gyroscope or accelerometer and helps in determining the optimal averaging time for measurements.

- **Random Walk:** This type of noise is due to the integration of white noise over a given period. In the Allan Variance plot, a slope of -0.5 signifies its presence. It denotes a cumulative effect where errors randomly increase or decrease over time, often seen in rate sensors.

- **Drift:** Refers to systematic errors that can accumulate over time. These are deterministic in nature and can arise from various factors such as temperature changes, aging, or manufacturing imperfections. On the Allan Variance plot, it can manifest as a positive slope, indicating its deterministic nature.
Output:
![Accelerometer Allan Variance](./images/Accel_Allandeviation.png)
![Gyroscope Allan Variance](./images/Gyro _Allandeviation.png)
### 3. Noise Spectral Density: 
Noise Spectral Density offers insights into the distribution of a signal's power over its frequency. It's essential to understand these nuances to eliminate unwanted frequencies from our data.

#### Significance in IMU Calibration
While Allan Variance helps identify the types of noise, Noise Spectral Density aids in identifying the specific frequencies that might be causing them. Once identified, we can employ targeted filtering techniques to remove them, ensuring our IMU readings are as precise as possible.
Output:
![Accelerometer Noise Spectral Density](./images/Accel_noise spectral density.png)
![Gyroscope Noise Spectral Density](./images/Gyro_noise spectral density.png)

### 4. Savitzky-Golay Filter:
When working with MEMS sensors, ensuring the output data is not marred by noise is of utmost importance. Savitzky-Golay filter, a polynomial smoothing filter, stands out in this regard.
The filter works by fitting sub-sets of adjacent data points with a low-degree polynomial. By doing so, it effectively reduces noise, preserving the essential features of the underlying data, making it especially useful for non-stationary signals like those from IMUs.
Output:
![Filtered Accelerometer Data](./images/Accel_data filtered.png)

#### Importance in MEMS Sensors
MEMS sensors are particularly vulnerable to high-frequency noise. Using a filter like Savitzky-Golay helps in retaining the sensor's original signal while getting rid of the noise, ensuring the data's reliability.

### 5. Data Acquisition: Foundation of Calibration
Real-time data acquisition from IMUs is the first step in the calibration process.

#### Implementation Details
Using serial communication, we interface with the IMU to acquire real-time data, which is then saved in CSV format. This data serves as the foundation upon which noise analysis, filtering, and calibration are performed.

### Conclusion
By employing methods like Allan Variance and Noise Spectral Density analysis, and tools like the Savitzky-Golay filter, this project aims to ensure the calibration of IMUs for telematics devices is both rigorous and accurate. This, in turn, ensures that data derived for insurance premium calculations is reliable and representative of actual driving behaviors.
