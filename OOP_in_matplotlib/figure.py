import numpy as np 
import matplotlib.pyplot as plt

# plt.figure(figsize=(10,8), dpi=150, facecolor='olive')
# ax1 = plt.axes([0.1, 0.1, 0.4, 0.4])
# ax2 = plt.axes([0.5, 0.6, 0.4, 0.3])


# plt.show()
x = np.linspace(-np.pi, np.pi, 20)
cos_x = np.cos(x) 
sin_x = np.sin(x) 

# fig = plt.figure(figsize=(10, 8), dpi=150)
# ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, cos_x)
# ax.plot(x, sin_x)
# plt.xlim(0, 3)
# plt.show()

# fig = plt.figure(figsize=(8, 6), dpi=200)
# ax_sin = fig.add_axes([0.1, 0.1, 0.6, 0.35])
# ax_cos = fig.add_axes([0.3, 0.5, 0.6, 0.4])

# ax_sin.plot(x, sin_x, marker='o', c='green', linewidth = 3)
# ax_cos.plot(x, cos_x, marker='o', c='blue', linewidth = 3)

# ax_sin.legend(labels = ['sin'], loc='upper left')
# ax_sin.grid(alpha=0.2, c='blue', linestyle='-.')
# ax_cos.set_facecolor(color='#FAF7E3')

from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10,8), dpi=150)

gs = GridSpec(3, 3, figure=fig, width_ratios=[1, 2, 1], height_ratios=[2, 4, 2])

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[:, 2])
ax6 = fig.add_subplot(gs[2, 0:2])


plt.show()