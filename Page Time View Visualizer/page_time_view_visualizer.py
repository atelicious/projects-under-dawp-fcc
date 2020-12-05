#This is my solution to the Page View Time Series Visualizer Problem in FCC's Data Analysis with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-page-view-time-series-visualizer



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(1.0-0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df)
    ax.set(xlabel='Date', ylabel='Page Views', title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index(level=['date'])

    year_list = []
    month_list = []
    months = {'01' : 'January',
          '02' : 'February',
          '03' : 'March',
          '04' : 'April',
          '05' : 'May',
          '06' : 'June',
          '07' : 'July',
          '08' : 'August',
          '09' : 'September',
          '10' : 'October',
          '11' : 'November',
          '12' : 'December'}
    #Because we can only get values from .strftime in either first three characters of each month or the number corresponding to the month itself, we need to have a dictionary where we can compare these values and get their complete names.
    for rows in df_bar['date']:
        year_list.append(rows.strftime('%Y'))
        y = rows.strftime('%m')
        month_list.append(months[y])

    df_bar['year'] = pd.Series(year_list)
    df_bar['month'] = pd.Series(month_list)
    df_bar = df_bar.drop(columns=['date'])
    
    total = 0
    days = 0
    years = []
    months = []
    average = []
    #This is where we create a new dataframe with three columns: years, months and the average views.
    #We need to count the views for each day and compile them to their specific year and month.
    #We can do that by checking the current row in df_bar and the next row in the df_bar. If the year and month is equal, it means the current line and the next line is still in the same year and month. If not equal, then the entry will be the last line for that month and year and the average will be calculated and added to the list.

    for i in range(0, (len(df_bar['year'])-1)):
        if i == (len(df_bar['year'])-1):
            total += df_bar['value'][i]
            days += 1
            ave = round(total/days, 1)
            years.append(df_bar['year'][i])
            months.append(df_bar['month'][i])
            average.append(ave)
            total = 0
            days = 0
        elif df_bar['year'][i] == df_bar['year'][i + 1] and df_bar['month'][i] == df_bar['month'][i + 1]:
            total += df_bar['value'][i]
            days +=1
        else:
            total += df_bar['value'][i]
            days += 1
            ave = round(total/days, 1)
            years.append(df_bar['year'][i])
            months.append(df_bar['month'][i])
            average.append(ave)
            total = 0
            days = 0

    new_df = pd.DataFrame(columns = ['year', 'month', 'average'])
    new_df['year'] = pd.Series(years)
    new_df['month'] = pd.Series(months)
    new_df['average'] = pd.Series(average)

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig = sns.catplot(x="year", y="average", hue="month", kind="bar", data=new_df,
                      hue_order=month_list).fig
    plt.legend(labels=month_list,
                loc='upper left', bbox_to_anchor=(0, 1))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    y = []
    m = []

    for dates in df_box['date']:
        y.append(dates.strftime('%Y'))
        m.append(dates.strftime('%b'))
    
    df_box['year'] = pd.Series(y)
    df_box['month'] = pd.Series(m)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(12, 7), ncols=2, sharex=False)

    ax1 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    ax2 = sns.boxplot (x='month', y='value', data=df_box, ax=axes[1],
                       order=month_order)                  
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig