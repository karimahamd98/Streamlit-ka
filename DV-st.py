import streamlit as st
import pandas as pd
import numpy as np
import scipy as sp
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.graph_objs import *
init_notebook_mode()
import plotly.express as px
from PIL import Image

#image = Image.open('spotify-logo-dark-mode-vector-37694344-removebg-preview.png')
image = "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png"
st.image(image, width= 490)


st.title("Top 50 Spotify Songs - 2019")

df1 = pd.read_csv("https://raw.githubusercontent.com/karimahamd98/Streamlit-ka/main/top50.csv", encoding= 'unicode_escape')

st.text(" ")


sbar = st.sidebar.radio("What do you want to view?",["Glance at the data","Most popular music genres","Danceable songs and popularity","Music genres and acousticness","Music genres and songs length","Songs Energy, Danceability and Acousticness measure","Energy, Danceability and how beats per minute for each song","Length, Popularity, and Danceability for each song","Song genre popularity with respect to song length", "Other", "View All"])


if sbar == "Glance at the data":
  st.subheader("Glance at the data")
  st.subheader('''Data source: Kaggle
  Dataset:Top 50 Spotify Songs - 2019

  Link: https://www.kaggle.com/leonardopena/top50spotify2019''')
  st.write(df1.head(10))


if sbar == "Most popular music genres":
    st.subheader('Bar Graph showing most popular music genres:')
    st.markdown('Dance pop, pop, and Latin were the most popular')
    data = [Bar(x=df1["Genre"],
                y=df1["Popularity"])]
    layout1=Layout(title="Most Popular Music Genres", xaxis_title= "Music Genres", yaxis_title="Popularity Score", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig1 = dict( data=data, layout=layout1 )
    iplot(fig1)
    st.write(fig1)



if sbar == "Danceable songs and popularity":
    st.subheader('A Histogram showing how danceable songs are more popular:')

    data = [Histogram(x=df1["Danceability"],
                y=df1["Popularity"])]
    layout1=Layout(title="Are Danceable Songs More Popular?", xaxis_title= "Danceability Score", yaxis_title="Popularity Score", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)

    st.write(fig)

if sbar =="Music genres and acousticness":
    st.subheader('A Bar Graph showing what music genres are the most acoustic:')
    st.markdown('Dance pop, pop, and DFW rap are the most acoustic')

    data = [Bar(x=df1["Genre"],
                y=df1["Acousticness"])]
    layout1=Layout(title="What Music Genre Is The Most Acoustic?", xaxis_title= "Music Genre", yaxis_title="Acousticness", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)
    st.write(fig)

if sbar == "Music genres and songs length":
    st.subheader('A Bar Graph of what music genres have the longest songs:')
    st.markdown('Dance pop, pop, and Latin are the longest songs')
    data = [Bar(x=df1["Genre"],
                y=df1["Length"])]
    layout1=Layout(title="What Music Genre Have The Longest Songs", xaxis_title= "Music Genre", yaxis_title="Song Length(in seconds)", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)
    st.write(fig)

if sbar == "Songs Energy, Danceability and Acousticness measure":
    st.subheader("Songs Energy, Danceability and Acousticness measure:")
    st.markdown('Using Plotly express, a 3D scatter plot that plot points of different songs while showing their Energy, Danceability, Acousticness')

    fig= px.scatter_3d(df1,x="Energy", y="Danceability", z="Acousticness", color="Artist Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)

if sbar == "Energy, Danceability and how beats per minute for each song":
    st.subheader('Energy, Danceability and how beats per minute for each song:')
    st.markdown('A 3D scatter plot that plot different songs for each artist and song, it shows their Energy, Danceability and how beats per minute for each song')
    fig= px.scatter_3d(df1,x="Energy", y="Danceability", z="Beats Per Minute", color="Artist Name", symbol="Track Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)

if sbar == "Length, Popularity, and Danceability for each song":
    st.subheader('Length, Popularity, and Danceability for each song:')
    st.markdown('A 3D scatter plot that plot different songs for each artist and song, shows their Length, Popularity, and Danceability')

    fig= px.scatter_3d(df1,x="Length", y="Popularity", z="Danceability", color="Artist Name", symbol="Track Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)

if sbar == "Song genre popularity with respect to song length":
    st.subheader('An animated bar graph showing the popularity of each song genre with respect to the song length:')
    fig = px.bar(df1, x="Genre", y="Popularity",color="Genre",
      animation_frame="Length",animation_group="Genre",range_y=[0,400], range_x=[0,20])
    fig.show()
    st.write(fig)
if sbar == "Other":
    
   
    st.header("Covid-19 deaths visualized:")
    dfm = pd.read_csv('https://raw.githubusercontent.com/karimahamd98/Streamlit-ka/main/global_covid19_mortality_rates(cleaned).csv')

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




if sbar == "View All":

    st.subheader('''Data source: Kaggle

    Dataset: Top 50 Spotify Songs - 2019

    Link: https://www.kaggle.com/leonardopena/top50spotify2019''')


    st.text(" ")

    st.subheader("Glance at the data")
    st.write(df1.head(10))

    data = [Bar(x=df1["Genre"],
                y=df1["Popularity"])]
    layout1=Layout(title="Most Popular Music Genres", xaxis_title= "Music Genres", yaxis_title="Popularity Score", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig1 = dict( data=data, layout=layout1 )
    iplot(fig1)

    st.subheader('Bar Graph showing most popular music genres:')
    st.markdown('Dance pop, pop, and Latin were the most popular')

    st.write(fig1)
    st.text(" ")

    st.subheader('A Histogram showing how danceable songs are more popular:')

    data = [Histogram(x=df1["Danceability"],
                y=df1["Popularity"])]
    layout1=Layout(title="Are Danceable Songs More Popular?", xaxis_title= "Danceability Score", yaxis_title="Popularity Score", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)

    st.write(fig)
    st.text(" ")

    st.subheader('A Bar Graph showing what music genres are the most acoustic:')
    st.markdown('Dance pop, pop, and DFW rap are the most acoustic')

    data = [Bar(x=df1["Genre"],
                y=df1["Acousticness"])]
    layout1=Layout(title="What Music Genre Is The Most Acoustic?", xaxis_title= "Music Genre", yaxis_title="Acousticness", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)
    st.write(fig)
    st.text(" ")


    st.subheader('A Bar Graph of what music genres have the longest songs:')
    st.markdown('Dance pop, pop, and Latin are the longest songs')
    data = [Bar(x=df1["Genre"],
                y=df1["Length"])]
    layout1=Layout(title="What Music Genre Have The Longest Songs", xaxis_title= "Music Genre", yaxis_title="Song Length(in seconds)", font=dict(
            family="Courier New, monospace",
            size=15,
            ))
    fig = dict( data=data, layout=layout1 )
    iplot(fig)
    st.write(fig)
    st.text(" ")


    st.subheader("Songs Energy, Danceability and Acousticness measure:")
    st.markdown('Using Plotly express, a 3D scatter plot that plot points of different songs while showing their Energy, Danceability, Acousticness')

    fig= px.scatter_3d(df1,x="Energy", y="Danceability", z="Acousticness", color="Artist Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)
    st.text(" ")


    st.subheader('Energy, Danceability and how beats per minute for each song:')
    st.markdown('A 3D scatter plot that plot different songs for each artist and song, it shows their Energy, Danceability and how beats per minute for each song')
    fig= px.scatter_3d(df1,x="Energy", y="Danceability", z="Beats Per Minute", color="Artist Name", symbol="Track Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)
    st.text(" ")

    st.subheader('Length, Popularity, and Danceability for each song:')
    st.markdown('A 3D scatter plot that plot different songs for each artist and song, shows their Length, Popularity, and Danceability')

    fig= px.scatter_3d(df1,x="Length", y="Popularity", z="Danceability", color="Artist Name", symbol="Track Name")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()
    st.write(fig)

    st.text(" ")

    st.subheader('An animated bar graph showing the popularity of each song genre with respect to the song length:')
    fig = px.bar(df1, x="Genre", y="Popularity",color="Genre",
    animation_frame="Length",animation_group="Genre",range_y=[0,400], range_x=[0,20])
    fig.show()
    st.write(fig)
