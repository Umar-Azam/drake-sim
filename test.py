# Author : Umar Azam
# Date   : 7th June 2023
# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# Testing plotting functionality with a simple parabola
x = np.linspace(-5, 5, 1000)
y = x**2
plt.plot(x, y)
