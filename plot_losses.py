#Plotting losses

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


loss1 = pd.read_csv('loss.csv_0.1')
loss2 = pd.read_csv('loss.csv_0.01')
loss3 = pd.read_csv('loss.csv_0.001')
loss4 = pd.read_csv('loss.csv_0.0001')


Epoch = np.arange(0,15)
plt.plot(Epoch, loss1,label = 'lr = 0.1')
plt.plot(Epoch, loss2, label = 'lr = 0.01')
plt.plot(Epoch,loss3, label = 'lr = 0.001')
plt.plot(Epoch,loss4, label = 'lr = 0.0001')
plt.xlabel('Epoch')
plt.ylabel('Test loss')
plt.legend()
plt.show()


# Epoch = np.arange(1,5)
# plt.plot(Epoch, loss1.iloc[0:4],label = 'lr = 0.1')
# plt.plot(Epoch, loss2.iloc[0:4], label = 'lr = 0.01')
# plt.plot(Epoch,loss3.iloc[0:4], label = 'lr = 0.001')
# plt.plot(Epoch,loss4.iloc[0:4], label = 'lr = 0.0001')
# plt.legend()
# plt.show()