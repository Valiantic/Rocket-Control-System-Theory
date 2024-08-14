# Libraries 
# pip install control for import control 
import matplotlib.pyplot as plt
import control as ctrl

# systems gain 
num = [10]
# defines the denominator
den = [2, 2, 1]
# constructs the rocket transfer function
G = ctrl.TransferFunction(num, den)

# PID controller (proportional, integral, derivative)

Kp = 5 # sets proportiinal gain to 5
Ki = 2 # sets integral gain to 2 
Kd = 1 # sets derivative gain to 1 
C = ctrl.TransferFunction([Kd, Kp, Ki], [1,0])

# Applying pid controller to rocket transfer function
CL = ctrl.feedback(C * G, 1)

# root locus for gain analysis 

plt.figure(figsize=(10, 6))
ctrl.root_locus(C * G, grid=True)
plt.title("Root Locus Plot (Closed-Loop)")
plt.show()

# bode plot for stability analysis

plt.figure(figsize=(10, 6))
ctrl.bode_plot(CL, dB=True, Hz=False, deg=True)
plt.suptitle("Bode Plot (Closed-Loop)", fontsize=16)
plt.show()

# nyquist Plot for Stability Analysis

plt.figure(figsize=(10, 6))
ctrl.nyquist_plot(CL)
plt.title("Nyquist Plot (Closed-Loop)")
plt.show()