import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date')

# Clean data
minimo = df['value'].min()
maximo = df['value'].max()

# O sea, hay que dejar todos los datos que estén sobre el 2.5% del mínimo, y bajo el 2.5% del maximo
valor_minimo = minimo + (minimo * 0.025)
valor_maximo = maximo - (maximo * 0.025)

mask_minimo = df['value'] > (valor_minimo)
mask_maximo = df['value'] < (valor_maximo)

mask_total = (mask_minimo) & (mask_maximo)

df = df[mask_total]


def draw_line_plot():
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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
