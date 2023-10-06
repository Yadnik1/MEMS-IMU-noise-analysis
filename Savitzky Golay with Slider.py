import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from matplotlib.widgets import Slider

# Dummy variable for the initial window size of the Savitzky-Golay filter
dummy_variable = 25

csv_file_path = 'accel-gyro-data2.csv'
# Read the CSV file without column names
data = pd.read_csv(csv_file_path, header=None)

# Get the first column and the first 200 rows
y = data.iloc[:200, 0]

def my_filter(z):
    return savgol_filter(z, dummy_variable, 2)

y_filtered = my_filter(y)

fig, ax = plt.subplots()
ax.plot(y, label="Original")
ax.plot(y_filtered, color='red', label="Filtered")
plt.subplots_adjust(bottom=0.25)
ax.legend()

ax_slide = plt.axes([0.25, 0.1, 0.65, 0.03]) 
win_size = Slider(ax_slide, 'Window size', valmin=5, valmax=605, valinit=27, valstep=2)

def update(val):
    global dummy_variable
    dummy_variable = int(win_size.val)
    new_y = my_filter(y)
    ax.clear()
    ax.plot(y, label="Original")
    ax.plot(new_y, color='red', label="Filtered")
    ax.legend()
    fig.canvas.draw()

win_size.on_changed(update)
plt.show()
