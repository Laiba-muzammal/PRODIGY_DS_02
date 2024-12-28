import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('task05.csv')

data.groupby(['Time_of_Day', 'Weather','Road_Condition'])['Accidents'].sum().unstack().plot(kind='bar',stacked=True)
plt.figuresize=((10,6))
plt.title('Accident Contributing Factors')
plt.xlabel('Factors')
plt.ylabel('Number of Accidents')
plt.show()