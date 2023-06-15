import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
    
    # Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Clean data
top_cutoff = df['value'].quantile(0.975)
bottom_cutoff = df['value'].quantile(0.025)

# Filter out the days above the top cutoff and below the bottom cutoff
df = df[(df['value'] <= top_cutoff) & (df['value'] >= bottom_cutoff)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df['date'], df['value'], color='r', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Format the x-axis ticks
    ax.set_xticks(pd.date_range(start='2016-06-01', end='2020-01-01', freq='6M'))
    ax.set_xticklabels(['2016-06', '2016-12', '2017-06', '2017-12', '2018-06', '2018-12', '2019-06', '2019-12'])

        # Format the y-axis ticks
    ax.set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000])
    ax.set_yticklabels(['0', '20000', '40000', '60000', '80000', '100000', '120000', '140000','160000', '180000'])

        # Save the plot as a PNG image
    plt.savefig('line_plot.png')

        # Show the plot
    fig = plt.show()


    # Save image and return fig (don't change this part)
    # fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).strftime('%B')

    # Group the data by year and month, and calculate the average page views
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig, ax = plt.subplots(figsize=(10, 6))
    df_grouped.plot(kind='bar', ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily freeCodeCamp Forum Page Views\n(Yearly Breakdown)')

    # Create the legend
    ax.legend(title='Months', loc='upper left')

    # Save the plot as a PNG image
    plt.savefig('bar_plot.png')

    # Show the plot
    fig = plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).strftime('%b')

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Adjust the spacing between subplots
    plt.subplots_adjust(wspace=0.4)

    # Save the plot as a PNG image
    # Show the plot
    fig = plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig