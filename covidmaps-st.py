import streamlit as st
import pandas as pd
import numpy as np

dfm = pd.read_csv('C:\\Users\\10User\\Documents\\MSBA\\Spring 22\\Data sets\\global_covid19_mortality_rates(cleaned).csv')

st.title("Interactive maps showing Covid-19 (mid-late 2020) deaths globally for each country:")

st.subheader('''Data source: Kaggle
Dataset: COVID-19 Case Mortality Ratios by Country

Link: https://www.kaggle.com/paultimothymooney/coronavirus-covid19-mortality-rate-by-country''')


st.title("Map #1")
st.markdown('''The color scale shows total deaths in thousands and the size of each circle represent the death ratio for each country.

This map was built using plotly Graph Objects and map box''')

lat= dfm.Latitude
lon= dfm.Longitude
loc_name= dfm.Country
loc_code=dfm.Country_Code
loc_deaths= dfm.Deaths
mortality_ratio =dfm["Mortality Ratio"]
loc_cases= dfm.Confirmed
mapbox_access_token = "pk.eyJ1Ijoia2FyaW0tYTk4IiwiYSI6ImNrejlyOXkyNTFscjgybnBrbHpxbTh5MWgifQ.0Y12OCFEmI6fmau9M10Xmg"

data = [
    Scattermapbox(
        lat= lat,
        lon= lon,
        mode='markers',
        marker=dict(
            size=mortality_ratio*3,
            autocolorscale=True,
            showscale=True,
            symbol= "circle",
            opacity=0.5,
            color= loc_deaths,
            colorscale= "reds",
            colorbar=dict(
                title='Total Deaths',
                thickness=15,
                titleside='top',
                outlinecolor='black',
                ticks='outside',
                ticklen=3) ),
        hovertext=loc_deaths,
        hoverinfo = "text",
        legendgroup= "Deaths",

),]


layout = Layout(
    title='Covid-19 Deaths Globally (mid-late 2020)',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=33.8547,
            lon=35.8623
        ),
        pitch=0,
        zoom=2.3,
        style='outdoors'
    ),



)

fig = dict(data=data, layout=layout)

iplot(fig)
st.write(fig)

st.text("")

st.title("Map #2")
st.markdown('''Another interactive map representing deaths at each country.

This choropleth map was built using plotly express''')

fig = px.choropleth(dfm, locations="Country",
                    locationmode="country names",
                    color="Deaths", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    projection="natural earth")
fig.show()
st.write(fig)
