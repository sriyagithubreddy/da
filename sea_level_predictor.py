import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1, y1, 'r')
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = res2.intercept + res2.slope * x2
    plt.plot(x2, y2, 'g')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
    import matplotlib.pyplot as plt
    plt.show()
