import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

df['date'] = pd.to_datetime(df['date'])
años = {'Years': [], 'Months': [], 'Days': [], 'date': df['date'], 'value': df['value']}

for fecha in df.date:
    años['Years'].append(fecha.year)
    años['Months'].append(fecha.strftime('%b'))
    años['Days'].append(fecha.day)

df = pd.DataFrame(años)

# Clean data
minimo = df['value'].quantile(0.025)
maximo = df['value'].quantile(0.975)

mask_minimo = df['value'] > (minimo)
mask_maximo = df['value'] < (maximo)

mask_total = (mask_minimo) & (mask_maximo)

df = df[mask_total]

def draw_line_plot():
    # Draw line plot
    fig, axis = plt.subplots(figsize = (16, 8))

    axis.set_xlabel('Date')
    axis.set_ylabel('Page Views')
    axis.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axis.plot(df['date'], df['value'], color = 'red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()

    sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_bar['Months'] = pd.Categorical(df_bar['Months'], categories = sort_order, ordered = True)
    df_bar = df_bar.sort_values('Months')

    # Copy and modify data for monthly bar plot
    

    averages = {'Years': [], 'Months': [], 'Average per month': []}

    for año_actual in df_bar.Years.unique():

        mask_año_actual = (df_bar['Years'] == año_actual)
        df_maskeado_año = df_bar[mask_año_actual]

        for mes_actual in df_maskeado_año['Months'].unique():

            mask_mes_actual = (df_maskeado_año['Months'] == mes_actual)
            df_maskeado_mes = df_maskeado_año[mask_mes_actual]

            promedio_mes = df_maskeado_mes['value'].mean()

            averages['Years'].append(año_actual)
            averages['Months'].append(mes_actual)
            averages['Average per month'].append(promedio_mes)

    averages = pd.DataFrame(averages)

    # Draw bar plot
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']

    fig, axis = plt.subplots(figsize = (12, 6))
    g = sns.barplot(data = averages, x = 'Years', y = 'Average per month', hue = 'Months', ax = axis)
    g.set(xlabel = 'Years', ylabel = 'Average Page Views')
    g.legend(meses)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_box['Months'] = pd.Categorical(df_box['Months'], categories = sort_order, ordered = True)
    df_box = df_box.sort_values('Months')

    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename(columns = {'value': 'Page Views'}, inplace = True)

    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1, 2, figsize = (20, 6))
    a = sns.boxplot(x = df_box['Year'], y = df_box['Page Views'], ax = axis[0])
    b = sns.boxplot(x = df_box['Month'], y = df_box['Page Views'], ax = axis[1])
    a.set_title('Year-wise Box Plot (Trend)')
    b.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
