import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.offline


happydata19 = pd.read_csv('2019.csv')
happydata19 = happydata19.set_index('Overall rank')

countries = gpd.read_file('countries.geojson')
countries = countries[countries['ADMIN'] != 'Antarctica']
countries = countries.rename(columns={'ADMIN': 'Country or region'})
countries.to_crs(epsg=3857, inplace=True)

def spatial():
    fig = go.Figure(data=go.Choropleth(
        locations=happydata19['Country or region'],
        z=happydata19['Score'].astype(float),
        locationmode='country names',
        colorscale='Viridis',
        colorbar_title='Happiness<br>Score'
    ))

    fig.update_layout(
        title_text='Happy'
    )

    fig.show()


#spatial()








def spatial2():

    data = [dict(type='choropleth', colorscale='Viridis',
                 locations=happydata19['Country or region'],
                 z=happydata19['Score'].astype(float),
                 locationmode='country names',
                 autocolorscale=False,
                 reversescale=False,
                 marker=dict(
                     line=dict(
                         color='rgb(180,180,180)',
                         width=0.5)),
                 colorbar=dict(
                     autotick=False,
                     title='Happiness Score'), )]

    layout = dict(
        title='Happy',
        geo = dict(
            showframe = False,
            showcoastlines = True,
            projection = dict(
                type = 'Mercator'
            )

        )
    )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig,validate=False,filename = 'test.html')

spatial2()