import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
np.float= float
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)


# Clean data
df = df[(df["value"]<df["value"].quantile(0.975))&(df["value"]>df["value"].quantile(0.025))]



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 8))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(df)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    fig, ax = plt.subplots(figsize=(8, 8))
    
    df_bar=df.copy()
    df_bar["date"]=df_bar.index
    df_bar["day"]=df_bar["date"].dt.day
    df_bar["month"]=df_bar["date"].dt.month_name()
    df_bar["year"]=df_bar["date"].dt.year
    hue_order=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    sns.set_palette("Paired")
    # Draw bar plot
    ax = sns.barplot(data=df_bar, x='year', y='value', hue='month', hue_order=hue_order)
    ax.set(xlabel='Years', ylabel='Average Page Views', title='some title')
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
