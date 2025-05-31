import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit 
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = pd.Series(range(1880, 2051))
    sea_levels1 = res1.slope * years1 + res1.intercept
    ax.plot(years1, sea_levels1, 'r', label='Fit: 1880–2050')

    # Create second line of best fit 
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000, 2051))
    sea_levels2 = res2.slope * years2 + res2.intercept
    ax.plot(years2, sea_levels2, 'g', label='Fit: 2000–2050')

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
