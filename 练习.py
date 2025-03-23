import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = np.arange(0,1.1,0.01)
y1=x**2
y2=x**4
plt.title('quxian')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['y=x^2','y=x^4'])
plt.savefig('../tmp/y=x^2.png')
plt.show()