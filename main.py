# Libraries 
# pip install control for import control 
import matplotlib.pyplot as plt
import control as ctrl

# systems gain 
num = [10]
# defines the denominator
den = [2, 2, 1]
# constructs the transfer function
G = ctrl.TransferFunction(num, den)


