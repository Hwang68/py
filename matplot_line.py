import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from google.colab import files
#uploaded = files.upload()

file = '/content/drive/MyDrive/imsi.xlsx'

df = pd.read_excel(file, sheet_name = 0, usecols='A:E',  skiprows=1, skipfooter=1)

x =df.loc[:, 'subject']
y1=df.loc[:,'Accuracy']
y2=df.loc[:,'Kappa']
y3=df.loc[:,'Precision']
y4=df.loc[:,'Recall']

plt.figure(figsize=(10, 5))
plt.plot(x, y1,  color= 'r', marker='o', label='Accuracy')

plt.plot(x, y2, color= 'g', marker='o', label='Kappa')
plt.plot(x, y3, color= 'b', marker='o', label='Precision')
plt.plot(x, y4, c= 'aqua', marker='o', label='Recall')
plt.ylim([0.8, 1.0])
plt.legend(loc='upper right')
plt.grid(True, axis='y', alpha = 0.5, linestyle="--")
plt.show()