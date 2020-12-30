import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Loading in the data, renaming columns, and generally making the data ready for plotting
df15 = pd.read_csv('2015.csv')
df16 = pd.read_csv('2016.csv')
df17 = pd.read_csv('2017.csv')
df18 = pd.read_csv('2018.csv')
df19 = pd.read_csv('2019.csv')

df15['Country'] = df15['Country'].replace({'Palestinian Territories': 'Palestine',
                                           'Somaliland region': 'Somalia', 'Congo (Kinshasa)': 'Congo'})

df17 = df17.rename(columns={'Happiness.Score': 'Happiness Score', 'Economy..GDP.per.Capita.': 'Economy (GDP per Capita',
                            'Health..Life.Expectancy.': 'Health (Life Expectancy)', 'Happiness.Rank': 'Happiness Rank',
                            'Trust..Government.Corruption.': 'Trust (Government Corruption)'})
df18 = df18.rename(columns={'Country or region': 'Country', 'Score': 'Happiness Score', 'Overall rank': 'Happiness Rank',
                            'GDP per capita': 'Economy (GDP per Capita', 'Social support': 'Family',
                            'Healthy life expectancy': 'Health (Life Expectancy)', 'Freedom to make life choices': 'Freedom',
                            'Perceptions of corruption': 'Trust (Goverment Corruption)'})
df19 = df19.rename(columns={'Country or region': 'Country', 'Score': 'Happiness Score', 'Overall rank': 'Happiness Rank',
                            'GDP per capita': 'Economy (GDP per Capita', 'Social support': 'Family',
                            'Healthy life expectancy': 'Health (Life Expectancy)', 'Freedom to make life choices': 'Freedom',
                            'Perceptions of corruption': 'Trust (Goverment Corruption)'})

df15 = df15.set_index('Country', drop=False)
df16 = df16.set_index('Country', drop=False)
df17 = df17.set_index('Country', drop=False)
df18 = df18.set_index('Country', drop=False)
df19 = df19.set_index('Country', drop=False)

df17['Region'] = ''
df18['Region'] = ''
df19['Region'] = ''
df17['Region'] = df15['Region']
df18['Region'] = df15['Region']
df19['Region'] = df15['Region']

df15 = df15.set_index('Happiness Rank')
df16 = df16.set_index('Happiness Rank')
df17 = df17.set_index('Happiness Rank')
df18 = df18.set_index('Happiness Rank')
df19 = df19.set_index('Happiness Rank')

df15['Year']=2015
df16['Year']=2016
df17['Year']=2017
df18['Year']=2018
df19['Year']=2019

colors = {'Western Europe': 'Blue', 'Central and Eastern Europe': 'Magenta',
          'Australia and New Zealand': 'Purple', 'North America': 'Red',
          'Latin America and Caribbean': 'Orange', 'Southern Asia': 'Black',
          'Southeastern Asia': 'Brown', 'Eastern Asia': 'Grey',
          'Middle East and Northern Africa': 'Green', 'Sub-Saharan Africa': 'LightBlue'}

df15_mean = df15.groupby(['Region']).mean()
df15_mean = df15_mean.drop(columns=['Happiness Score', 'Standard Error', 'Dystopia Residual', 'Year'])
df_new = df15_mean.transpose()
df_new = df_new[['Western Europe', 'North America', 'Australia and New Zealand',
                 'Middle East and Northern Africa', 'Latin America and Caribbean',
                 'Southeastern Asia', 'Central and Eastern Europe', 'Eastern Asia',
                 'Sub-Saharan Africa', 'Southern Asia']]

avg_happy_score15 = round((df15['Happiness Score'].sum(axis = 0, skipna=True)/(len(df15.index))), 2)

def bars():

    fig = make_subplots(rows=2, cols=1, subplot_titles=['', ''])

    for i in df15['Region'].unique():
        dfn = df15[df15['Region']==i]
        fig.add_trace(trace=go.Bar(x=dfn['Country'],
                                   y=dfn['Happiness Score'],
                                   name=i,
                                   marker_color=colors[i],
                                   hovertemplate='<b>Country</b> : %{x}' +
                                                 '<br><b>Happiness Score</b> : %{y:.2f}',
                                   legendgroup=i),
                      row=1, col=1)

    for i in df_new.columns.unique():
        fig.add_trace(trace=go.Bar(x=df_new.index,
                                   y=df_new[i],
                                   name=i,
                                   marker_color=colors[i],
                                   hovertemplate='<b>Variable</b> : %{x}' +
                                                 '<br><b>Average Regional Value</b> : %{y:.2f}',
                                   legendgroup=i,
                                   showlegend=False),
                      row=2, col=1)

    fig.update_layout(barmode='group', legend_title='<b>Different Regions<b>',)

    fig.update_yaxes(showspikes=True,
                     spikemode='across',
                     spikethickness=1,
                     spikecolor='Black',
                     showline=True,
                     showgrid=True,
                     row=1,
                     col=1
                     )

    fig.update_xaxes(title_text="", row=1, col=1)
    fig.update_xaxes(title_text="Explanatory Variables", row=2, col=1)

    fig.update_yaxes(title_text="Happiness Score", row=1, col=1)
    fig.update_yaxes(title_text="", row=2, col=1)

    fig.show()

#bars()

def bubble():

    fig = go.Figure()

    for i in df15['Region'].unique():
        dfn = df15[df15['Region'] == i]
        size=dfn['Happiness Score']
        fig.add_trace(go.Scatter(x=dfn['Economy (GDP per Capita)'],
                                 y=dfn['Health (Life Expectancy)'],
                                 customdata=dfn['Country'],
                                 hovertemplate='<b>Country</b> : %{customdata}'+
                                 '<br><b>Happiness Score</b> : %{marker.size:.2f}<br>'+
                                 'X & Y values : %{x:.2f} , %{y:.2f}',
                                 mode='markers',
                                 name=i,
                                 marker=dict(
                                     size=size,
                                     sizeref=2.*max(size)/(6.**2),
                                     opacity=0.8)
                                 ))

    fig.update_layout(
        title='Bubble Chart and Happiness Data',
        xaxis_title='Country GDP',
        yaxis_title='Life Expectancy',
        legend_title='<b>Different Regions<b>',

        legend={'itemsizing': 'constant'},

        yaxis=dict(
            tickmode='linear',
            tick0=0.6,
            dtick=0.1
        ),

        xaxis=dict(
            rangeslider=dict(
                visible=True
            )
        )
    )

    fig.add_annotation(dict(x=0.8,
                            y=1.1,
                            showarrow=False,
                            text='Size of Bubbles Corresponds to Happiness Score of the Country',
                            xref="x",
                            yref="paper"
                            ))

    fig.show()


#bubble()


def spatial():

    fig = go.Figure()

    fig.add_trace(go.Choropleth(
        locations=df15['Country'],
        z=df15['Happiness Score'].astype(float),
        locationmode='country names',
        #Måske udregn average happiness score og brug den som midtpunkt for colorscale
        #https://plotly.com/python/colorscales/
        colorscale='Viridis',
        zauto=True,
        zmid=avg_happy_score15,
        colorbar_title='Happiness<br>Score'
    ))

    fig.update_layout(
        title_text='World Map Showing Each Countries Happiness Score'
    )

    fig.show()

spatial()