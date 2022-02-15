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
    st.subheader("Also check:")
    st.markdown('''Covid-19 deaths visualized

    Link ''')

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
