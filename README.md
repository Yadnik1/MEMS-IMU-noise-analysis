# MEMS-IMU-noise-analysis

## Calibration and Data Processing for IMU in Telematics

## Getting Started
1. Please clone the Repository.
2. Run the .py files individually.

Allan Variance, Noise Spectral Density, and Savitzky-Golay Filter are fundamental methods employed in this project to analyze and process data from IMUs in telematics. This is crucial for determining the insurance premium of car users. 

### Allan Variance
Allan Variance provides insights into the underlying noise characteristics of IMUs. It measures the frequency stability of oscillations in a time sequence, which is invaluable given the various noise types affecting IMUs.

#### Identifying IMU Noise Characteristics:
- **White Noise:** Manifests as a flat line on an Allan Variance plot.
- **Bias Instability:** Represents the point of optimal stability on the plot.
- **Random Walk:** A slope of -0.5 on the plot indicates its presence.
- **Drift:** Appears as a positive slope on the plot.

Output:
![Accelerometer Allan Variance](https://github.com/Yadnik1/MEMS-IMU-noise-analysis/blob/master/Images/Accel_Allandeviation.png?raw=true)
![Gyroscope Allan Variance](https://github.com/Yadnik1/MEMS-IMU-noise-analysis/blob/master/Images/Gyro%20_Allandeviation.png?raw=true)

### Noise Spectral Density
Noise Spectral Density reveals the distribution of a signal's power over its frequency. Recognizing these details allows for the elimination of undesirable frequencies.

#### Significance in IMU Calibration
Noise Spectral Density helps pinpoint frequencies causing noise, enabling the use of filtering techniques to enhance IMU reading precision.

Output:
![Accelerometer Noise Spectral Density](https://github.com/Yadnik1/MEMS-IMU-noise-analysis/blob/master/Images/Accel_noise%20spectral%20density.png?raw=true)
![Gyroscope Noise Spectral Density](https://github.com/Yadnik1/MEMS-IMU-noise-analysis/blob/master/Images/Gyro_noise%20spectral%20density.png?raw=true)

### Savitzky-Golay Filter
The Savitzky-Golay filter, a polynomial smoothing filter, reduces noise while preserving vital data features. It's ideal for non-stationary signals, such as those from IMUs.

#### Importance in MEMS Sensors
The Savitzky-Golay filter is crucial for MEMS sensors as it retains the sensor's original signal while eliminating noise, ensuring data reliability.

Output:
![Filtered Accelerometer Data](https://github.com/Yadnik1/MEMS-IMU-noise-analysis/blob/master/Images/Accel_data%20filtered.png?raw=true)

### Data Acquisition: Foundation of Calibration
Acquiring real-time data from IMUs is crucial for calibration.

#### Implementation Details
Serial communication interfaces with the IMU to collect real-time data saved in CSV format. This data is foundational for noise analysis, filtering, and calibration.

## Project Overview
This project utilizes methods like Allan Variance, Noise Spectral Density analysis, and tools such as the Savitzky-Golay filter to ensure rigorous and accurate IMU calibration for telematics devices. Consequently, the data used for insurance premium calculations is reliable and truly representative of driving behaviors.

