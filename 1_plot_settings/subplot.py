import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 5)
y1 = x**2
y2 = x**3
y3 = x**0.5
y4 = np.sin(x**2)

# plt.subplot(2, 2, 1)
# plt.plot(x, y1, 'r')
# plt.title('y1')

# plt.subplot(2, 2, 2)
# plt.plot(x, y2, 'g')
# plt.title('y2')

# plt.subplot(2, 2, 3)
# plt.plot(x, y3, 'y')
# plt.title('y3')

# plt.subplot(2, 2, 4)
# plt.plot(x, y4, 'c')
# plt.title('y4')

# plt.subplot(3, 2, 1)
# plt.plot(x, y1)
# plt.title('First')

# plt.subplot(3, 2, 2)
# plt.plot(x, y1)
# plt.title('Second')

# plt.subplot(3, 3, 4)
# plt.plot(x, y1)
# plt.title('Third')

# plt.subplot(3, 3, 5)
# plt.plot(x, y1)
# plt.title('Fourth')

# plt.subplot(3, 2, 6)
# plt.plot(x, y1)
# plt.title('Fifth')


plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('First')

plt.subplot(3, 2, 4)
plt.plot(x, y1)
plt.title('First')

plt.subplot(4, 3, 12)
plt.plot(x, y1)
plt.title('First')




plt.show()

