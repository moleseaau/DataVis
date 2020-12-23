import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Loading in the data, renaming columns, and generally making the data ready for plotting
#https://www.kite.com/python/answers/how-to-drop-empty-rows-from-a-pandas-dataframe-in-python drop NA
df15 = pd.read_csv('2015.csv')
df16 = pd.read_csv('2016.csv')
df17 = pd.read_csv('2017.csv')
df18 = pd.read_csv('2018.csv')
df19 = pd.read_csv('2019.csv')

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







# https://xang1234.github.io/bubbleplot/
def bubble():
    # fig = go.Figure(data=[go.Scatter(
    #     x=df15['Family'],
    #     y=df15['Health (Life Expectancy)'],
    #     mode='markers',
    #     marker=dict(
    #         color=df15['Region'],
    #         showscale=True,
    #         size=df15['Happiness Score'] * 4
    #     )
    # )])

    # https://community.plotly.com/t/multiple-traces-plotly-express/23360
    fig = px.scatter(df15, x='Family', y='Health (Life Expectancy)',
                     color='Region', size='Happiness Score', hover_name='Country')
    #fig.add_trace(px.scatter())
    fig.update_layout(
        updatemenus=[
            dict(
                direction="down",
                x=1.04,
                y=0.3,
                xanchor="left",
                showactive=True,
                buttons=list([
                    dict(label="GDP per Capita",
                         method="update",
                         args=[
                             {"x": df15['Economy (GDP per Capita)']},
                             {"xaxis.title.text": "GDP"}
                         ],),
                    dict(label="Family",
                         method="update",
                         args=[
                             {"x": df15['Family']},
                             {"xaxis.title.text": "Family"}
                         ]),
                    dict(label="Health",
                         method="update",
                         args=[
                             {"x": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text": "Life Expectancy"}
                         ]),
                    dict(label="Freedom",
                         method="update",
                         args=[
                             {"x": df15['Freedom']},
                             {"xaxis.title.text": "Freedom"}
                         ]),
                    dict(label="Trust",
                         method="update",
                         args=[
                             {"x": df15['Trust (Government Corruption)']},
                             {"xaxis.title.text": "Trust"}
                         ]),
                    dict(label="Generosity",
                         method="update",
                         args=[
                             {"x": df15['Generosity']},
                             {"xaxis.title.text": "Generosity"}
                         ])

                ])
            )])
    fig.show()


bubble()

def spatial():
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'choropleth'}, {'type': 'xy'}]])

    fig.add_trace(go.Choropleth(
        locations=df15['Country'],
        z=df15['Happiness Score'].astype(float),
        locationmode='country names',
        colorscale='Viridis',
        colorbar_title='Happiness<br>Score'
    ), row=1, col=1)

    fig.update_layout(
        title_text='Happy'
    )

    fig.show()

#spatial()