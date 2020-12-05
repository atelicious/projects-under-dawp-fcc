#This is my solution to the Sea Level Predictor Problem in FCC's Data Analysis with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-sea-level-predictor


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x_ticks = []
    x_ticks_labels = []

    for i in range(1850, 2076, 25):
        x_ticks.append(round(float(i), 1))
    for i in x_ticks:
        x_ticks_labels.append(str(i))
    
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_xbound(lower=1850, upper=2050)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks_labels)

    # Create first line of best fit
    #According to the problem, we have to plot a best line of fit up to year 2050.
    #Using scypy.stats.lingress gives us 5 values: slope of regression, intercept of the regression line,
    #correlation coefficient, p-value, and standard error of estimated gradient.
    #To plot the best line, we need the slope and the intercept of the regression line.

    slope, intercept, rvalue, pvalue, std_error = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #We can now delete the corr_coeff, p-value, and std_error because we are only going to use slope and regression_intercept.

    del rvalue, pvalue, std_error

    x_values = list((range(1880, 2050, 1)))
    y_values = []

    for values in x_values:
        y_values.append(intercept + values*slope)
    
    ax.plot(x_values, y_values, color = 'red')


    # Create second line of best fit
    #For this second line of best fit, we need the linear regression of values from year 2000 up to year 2050.
    #We need to slice our data so that data from 2000 onwards are the ones that we are analyzing.

    df_from_2000_up = df[df['Year'] >= 2000].copy()

    #Then we proceed from what we did from the first best line of fit
    slope, intercept, rvalue, pvalue, std_error = linregress(df_from_2000_up['Year'], df_from_2000_up['CSIRO Adjusted Sea Level'])

    del rvalue, pvalue, std_error

    x_values = list((range(2000, 2050, 1)))
    y_values = []

    for values in x_values:
        y_values.append(intercept + values*slope)
    
    ax.plot(x_values, y_values, color = 'blue')

    # Add labels and title

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')    
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()