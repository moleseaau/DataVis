import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.offline

happydata = pd.read_csv('2019.csv')
happydata = happydata.set_index('Overall rank')

countries = gpd.read_file('countries.geojson')
countries = countries[countries['ADMIN'] != 'Antarctica']
countries = countries.rename(columns={'ADMIN': 'Country or region'})
countries.to_crs(epsg=3857, inplace=True)


def spatial():

    data = [dict(type='choropleth', colorscale='Viridis',
                 locations=happydata['Country or region'],
                 z=happydata['Score'].astype(float),
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

spatial()
