# -*- coding: utf-8 -*-
"""2025메카실습1_Low_Pass_Filter_IIR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oaunc-yEYhClBSP3KKbjXCcU8qXStEMe
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
fs = 10000  # Sampling frequency (10 kHz)
T = 0.1    # Simulation time (s)
t = np.linspace(0, T, int(fs * T))  # Time vector

# PWM signal generation
PWM_freq = 1000  # PWM frequency (Hz)
duty_cycle = 50  # Duty cycle in percentage
PWM_signal = np.where((t % (1/PWM_freq)) < (duty_cycle / 100) * (1/PWM_freq), 1, 0)

# RC Low-Pass Filter parameters
R = 10e3  # 10kΩ
C = 1e-6  # 1µF
tau = R * C  # Time constant
alpha = 1 / (R*C*fs + 1)
# alpha = (1 / fs) / (tau + (1 / fs))

# Apply RC low-pass filter using a simple IIR filter approach
filtered_signal = np.zeros_like(PWM_signal,dtype='float')

for i in range(1, len(PWM_signal)):
    filtered_signal[i] = alpha * PWM_signal[i] + (1 - alpha) * filtered_signal[i - 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, PWM_signal, label="PWM Input", linestyle="--", alpha=0.7)
plt.plot(t, filtered_signal, label="Filtered Output", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("RC Low-Pass Filter Response to PWM Input")
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
fs = 10000  # Sampling frequency (10 kHz)
T = 0.1   # Simulation time (s)
t = np.linspace(0, T, int(fs * T))  # Time vector

# PWM signal generation
PWM_freq = 1000  # PWM frequency (Hz)
duty_cycle = 50  # Duty cycle in percentage
PWM_signal = np.where((t % (1/PWM_freq)) < (duty_cycle / 100) * (1/PWM_freq), 1, 0)

# RC Low-Pass Filter parameters
R = 2e3  # 2kΩ
C = 1e-6  # 1µF
tau = R * C  # Time constant
alpha = 1 / (R*C*fs + 1)
# alpha = (1 / fs) / (tau + (1 / fs))

# Apply RC low-pass filter using a simple IIR filter approach
filtered_signal = np.zeros_like(PWM_signal,dtype='float')

for i in range(1, len(PWM_signal)):
    filtered_signal[i] = alpha * PWM_signal[i] + (1 - alpha) * filtered_signal[i - 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, PWM_signal, label="PWM Input", linestyle="--", alpha=0.7)
plt.plot(t, filtered_signal, label="Filtered Output", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("RC Low-Pass Filter Response to PWM Input")
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
fs = 10000  # Sampling frequency (10 kHz)
T = 0.02    # Simulation time (s)
t = np.linspace(0, T, int(fs * T))  # Time vector

# PWM signal generation
PWM_freq = 1000  # PWM frequency (Hz)
duty_cycle = 80  # Duty cycle in percentage
PWM_signal = np.where((t % (1/PWM_freq)) < (duty_cycle / 100) * (1/PWM_freq), 1, 0)

# RC Low-Pass Filter parameters
R = 2e3  # 10kΩ
C = 0.5e-6  # 1µF
tau = R * C  # Time constant
alpha = 1 / (R*C*fs + 1)
# alpha = (1 / fs) / (tau + (1 / fs))

# Apply RC low-pass filter using a simple IIR filter approach
stage1_signal = np.zeros_like(PWM_signal,dtype='float')
stage2_signal = np.zeros_like(PWM_signal,dtype='float')

for i in range(1, len(PWM_signal)):
    stage1_signal[i] = alpha * PWM_signal[i] + (1 - alpha) * stage1_signal[i - 1]

for i in range(1, len(PWM_signal)):
    stage2_signal[i] = alpha * stage1_signal[i] + (1 - alpha) * stage2_signal[i - 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, PWM_signal, label="PWM Input", linestyle="--", alpha=0.7)
plt.plot(t, stage2_signal, label="Filtered Output", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("RC Low-Pass Filter Response to PWM Input")
plt.legend()
plt.grid()
plt.show()

# prompt: modify the code to change duty from 0.3 to 0.8 at 0.015 sec

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
fs = 10000  # Sampling frequency (10 kHz)
T = 0.06    # Simulation time (s)
t = np.linspace(0, T, int(fs * T))  # Time vector

# PWM signal generation
PWM_freq = 1000  # PWM frequency (Hz)
duty_cycle_initial = 0.3  # Initial duty cycle
duty_cycle = duty_cycle_initial
PWM_signal = np.zeros_like(t)

for i in range(len(t)):
    if t[i] >= 0.015:
        duty_cycle = 0.8

    if (t[i] % (1/PWM_freq)) < duty_cycle * (1/PWM_freq):
        PWM_signal[i] = 1

# RC Low-Pass Filter parameters
R = 2e3  # 10kΩ
C = 0.5e-6  # 1µF
tau = R * C  # Time constant
alpha = 1 / (R*C*fs + 1)
# alpha = (1 / fs) / (tau + (1 / fs))

# Apply RC low-pass filter using a simple IIR filter approach
stage1_signal = np.zeros_like(PWM_signal,dtype='float')
stage2_signal = np.zeros_like(PWM_signal,dtype='float')

for i in range(1, len(PWM_signal)):
    stage1_signal[i] = alpha * PWM_signal[i] + (1 - alpha) * stage1_signal[i - 1]

for i in range(1, len(PWM_signal)):
    stage2_signal[i] = alpha * stage1_signal[i] + (1 - alpha) * stage2_signal[i - 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, PWM_signal, label="PWM Input", linestyle="--", alpha=0.7)
plt.plot(t, stage2_signal, label="Filtered Output", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("RC Low-Pass Filter Response to PWM Input")
plt.legend()
plt.grid()
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
fs = 10000  # Sampling frequency (10 kHz)
T = 0.02    # Simulation time (s)
t = np.linspace(0, T, int(fs * T))  # Time vector

# PWM signal generation
PWM_freq = 1000  # PWM frequency (Hz)
duty_cycle = 50  # Duty cycle in percentage
PWM_signal = np.where((t % (1/PWM_freq)) < (duty_cycle / 100) * (1/PWM_freq), 1, 0)

# RC Low-Pass Filter parameters
R = 10e3  # 10kΩ
C = 1e-6  # 1µF
tau = R * C  # Time constant
alpha = 1 / (R*C*fs + 1)
# alpha = (1 / fs) / (tau + (1 / fs))

# Apply RC low-pass filter using a simple IIR filter approach
filtered_signal = np.zeros_like(PWM_signal,dtype='float')

for i in range(1, len(PWM_signal)):
    filtered_signal[i] = alpha * PWM_signal[i] + (1 - alpha) * filtered_signal[i - 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, PWM_signal, label="PWM Input", linestyle="--", alpha=0.7)
plt.plot(t, filtered_signal, label="Filtered Output", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("RC Low-Pass Filter Response to PWM Input")
plt.legend()
plt.grid()
plt.show()

1-alpha

i = 0
alpha * PWM_signal[i] + (1 - alpha) * filtered_signal[i - 1]

alpha, filtered_signal, PWM_signal

filtered_signal[0]