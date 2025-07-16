import matplotlib.pyplot as plt
import pandas as pd

def plot_accident_factors(file_path):
    data = pd.read_csv(file_path)
    grouped_data = data.groupby(['Time_of_Day', 'Weather','Road_Condition'])['Accidents'].sum().unstack()

    ax = grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_title('Accident Contributing Factors')
    ax.set_xlabel('Factors')
    ax.set_ylabel('Number of Accidents')
    plt.tight_layout()
    plt.show()
