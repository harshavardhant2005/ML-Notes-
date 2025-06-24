import matplotlib.pyplot as plt

import random as rd

hist=[]
for i in range(50):
    hist.append(rd.randint(1,100))

plt.hist(hist,bins=10)
plt.show()