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

colors = {'Western Europe': 0, 'North America': 1, 'Australia and New Zealand': 2,
          'Middle East and Northern Africa': 3, 'Latin America and Caribbean': 4,
          'Southeastern Asia': 5, 'Central and Eastern Europe': 6, 'Eastern Asia': 7,
          'Sub-Saharan Africa': 8, 'Southern Asia': 9}

df15_mean = df15.groupby(['Region']).mean()

def bars():

    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=['Each Countries Happiness Score Seperated in Regions', 'Hej'])

    for i in df15['Region'].unique():
        dfn = df15[df15['Region']==i]
        fig.add_trace(trace=go.Bar(x=dfn['Country'],
                                   y=dfn['Happiness Score'],
                                   name=i,
                                   marker_color=colors[i]),
                      row=1, col=1)

    #KeyError: Happiness Score??
    # for columns in df15_mean:
    #     df15_m = df15_mean.drop(columns=['Happiness Score', 'Standard Error', 'Dystopia Residual', 'Year'])
    #     print(df15_m.columns)
    #     fig.add_trace(trace=go.Bar(x=df15_m[columns],
    #                                y=df15_m[columns],
    #                                name=df15_m.index,
    #                                marker_color=colors[df15_m.index]),
    #                   row=2, col=1)

    for j in df15_mean.index:
        dfm = df15_mean[df15_mean.index==j]
        dfm = dfm.drop(columns=['Happiness Score', 'Standard Error', 'Dystopia Residual', 'Year'])
        print(dfm.columns)
        for columns in dfm:
            fig.add_trace(trace=go.Bar(x=dfm.index,
                                       y=dfm[columns],
                                       name=columns,
                                       marker_color=colors[j]),
                          row=2, col=1)




    # for i in df15_mean.index:
    #     fig.add_trace(trace=go.Scatter(
    #         x=df15_mean.index, y=df15_mean['Economy (GDP per Capita)'],
    #         mode='markers', name=i, marker_color=colors[i]), row=2, col=1)

    #https://stackoverflow.com/questions/56289777/coloring-scatter-plot-points-differently-based-on-certain-conditions
    #https://stackoverflow.com/questions/51181729/custom-plotly-markers-based-on-variable-value
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Economy (GDP per Capita)'],
    #                          mode='markers', showlegend=False, name="GDP"), row=2, col=1)
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Family'],
    #                          mode='markers', showlegend=False, name="Family"), row=2, col=1)
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Health (Life Expectancy)'],
    #                          mode='markers', showlegend=False, name="Life Expectancy"), row=2, col=1)
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Freedom'],
    #                          mode='markers', showlegend=False, name="Freedom"), row=2, col=1)
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Trust (Government Corruption)'],
    #                          mode='markers', showlegend=False, name="Trust"), row=2, col=1)
    # fig.add_trace(go.Scatter(x=df15_mean.index, y=df15_mean['Generosity'],
    #                          mode='markers', showlegend=False, name="Generosity"), row=2, col=1)

    fig.update_layout(barmode='stack', xaxis2={'categoryorder': 'category ascending'})

    fig.update_xaxes(title_text="Country", row=1, col=1)
    fig.update_xaxes(title_text="Regions", row=2, col=1)

    fig.update_yaxes(title_text="Happiness Score", row=1, col=1)
    fig.update_yaxes(title_text="Explanotory Variables", row=2, col=1)

    fig.show()

bars()

#https://xang1234.github.io/bubbleplot/
#https://www.youtube.com/watch?v=Uu2mfzWajQY&list=PLH6mU1kedUy9HTC1n9QYtVHmJRHQ97DBa&index=16
def bubble():

    fig = go.Figure()

    for i in df15['Region'].unique():
        dfn = df15[df15['Region'] == i]
        fig.add_trace(go.Scatter(x=dfn['Economy (GDP per Capita)'],
                                 y=dfn['Health (Life Expectancy)'],
                                 text=dfn['Country'],
                                 mode='markers',
                                 name=i,
                                 marker=dict(
                                     size=3 * dfn['Happiness Score'],
                                     opacity=0.8)
                                 ))

    fig.update_layout(
        title='Bubble Chart and Happiness Data',
        xaxis_title='Country GDP',
        yaxis_title='Life Expectancy',
        legend_title='Different Regions',

        yaxis=dict(
            tickmode='linear',
            tick0=0.6,
            dtick=0.1
        ),

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
                             {"x": df15['Economy (GDP per Capita)'],
                              "y": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text": "GDP"}
                         ],),
                    dict(label="Family",
                         method="update",
                         args=[
                             {"x": df15['Family'],
                              "y": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text": "Family"}
                         ]),
                    dict(label="Freedom",
                         method="update",
                         args=[
                             {"x": df15['Freedom'],
                              "y": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text.text": "Freedom"}
                         ]),
                    dict(label="Trust",
                         method="update",
                         args=[
                             {"x": df15['Trust (Government Corruption)'],
                              "y": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text": "Trust"}
                         ]),
                    dict(label="Generosity",
                         method="update",
                         args=[
                             {"x": df15['Generosity'],
                              "y": df15['Health (Life Expectancy)']},
                             {"xaxis.title.text": "Generosity"}
                         ])

                ])
            )])
    fig.show()


#bubble()

def spatial():
    fig = make_subplots(rows=2, cols=1, specs=[[{'type': 'choropleth'}, {'type': 'xy'}]])

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