#Importing required Libraries
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import statistics
import pickle


#Setting page configuration
st.set_page_config(
    page_title="Health Care Analytics",
    layout="wide",
    page_icon="🏥"
)

#Reading the data from the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/karimahamd98/Streamlit-ka/main/diabetes.csv')


#Dividing the page into columns to organize the placement of a picture
col1, col2, col3 = st.columns([5,6,1])


with col1:
    st.write("")

with col2:
    image = "https://static.cdnlogo.com/logos/d/69/diabetes.svg"
    st.image(image, width= 200)

with col3:
    st.write("")


#Creating the navigation bar
selected = option_menu(None, ["Home", "EDA", "Prediction"],
icons=["house", "bar-chart", "forward"],
menu_icon="cast", default_index=0, orientation="horizontal",
styles={
"nav-link-selected": {"background-color": "#89CFF0"},
})


#Intiating each page and its content
if selected == "Home":

    st.markdown(f'<h1 style="color:#89CFF0;font-size:35px;">{"Overview"}</h1>', unsafe_allow_html=True)
    st.markdown("""---""")


    col1, col2, col3 = st.columns([9,6,1])

    #Adding text and an image to the home page
    with col1:
        st.write("")
        txt1 = st.text_area(' ','''Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.

Over time, having too much glucose in your blood can cause health problems. Although diabetes has no cure, you can take steps to manage your diabetes and stay healthy.

Sometimes people call diabetes “a touch of sugar” or “borderline diabetes.” These terms suggest that someone doesn’t really have diabetes or has a less serious case, but every case of diabetes is serious.

What are the different types of diabetes? The most common types of diabetes are type 1, type 2, and gestational diabetes.

Type 1 diabetes If you have type 1 diabetes, your body does not make insulin. Your immune system attacks and destroys the cells in your pancreas that make insulin. Type 1 diabetes is usually diagnosed in children and young adults, although it can appear at any age. People with type 1 diabetes need to take insulin every day to stay alive.

Type 2 diabetes If you have type 2 diabetes, your body does not make or use insulin well. You can develop type 2 diabetes at any age, even during childhood. However, this type of diabetes occurs most often in middle-aged and older people. Type 2 is the most common type of diabetes.

Gestational diabetes Gestational diabetes develops in some women when they are pregnant. Most of the time, this type of diabetes goes away after the baby is born. However, if you’ve had gestational diabetes, you have a greater chance of developing type 2 diabetes later in life. Sometimes diabetes diagnosed during pregnancy is actually type 2 diabetes.

Other types of diabetes Less common types include monogenic diabetes, which is an inherited form of diabetes, and cystic fibrosis-related diabetes ."

    ''', height = 310)

    with col2:
        st.header(" ")
        st.text("")
        image = "https://res.cloudinary.com/grohealth/image/upload/c_fill,f_auto,fl_lossy,h_650,q_auto,w_1085/v1581695681/DCUK/Content/causes-of-diabetes.png"
        st.image(image, width= 521)

    with col3:
        st.write("")


if selected == "EDA":

    st.markdown(f'<h1 style="color:#89CFF0;font-size:35px;">{"Visuals & Exploratory Analysis"}</h1>', unsafe_allow_html=True)
    st.markdown("""---""")
    #Adding metrics (cards) that provide a quick overview (used averages) of certain numbers in the data
    age = statistics.mean(df['Age'])
    bmi_avg= statistics.mean(df['BMI'])
    pressure_avg= statistics.mean(df['BloodPressure'])

    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric(
        label="Average Age  🔢",
        value= "{:.1f}".format(age))


    kpi2.metric(
        label="Average BMI  ⚖️",
        value = "{:.1f}".format(bmi_avg)
    )


    kpi3.metric(
        label="Average Diastolic Blood Pressure  🩸",
        value = "{:.1f}".format(pressure_avg)
    )

    st.markdown("""---""")

    col1, col2 = st.columns([8,8])

    #Plotting a pie chart
    with col1:
        trace = go.Pie(labels = ['Healthy','Diabetic'], values = df['Outcome'].value_counts(),
                   textfont=dict(size=15), opacity = 0.8,
                   marker=dict(colors=['darkturquoise', 'aliceblue'],
                   line=dict(
                       color='#000000', width=1.5)))

        fig = dict(data = [trace])

        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.subheader("Healthy vs Diabetic")
        st.latex("")
        st.caption("65% of the total population are healthy and 35% are diabetic ")
        col1.plotly_chart(fig,use_container_width = True)

        st.markdown(f'<h1 style="color:#89CFF0;font-size:31.5px;">{"Automated visuals"}</h1>', unsafe_allow_html=True)

        st.subheader("Scatter plot")

        #Defining a function that will plot a scatter plot based on input features
        def plot_feat1_feat2(feat1, feat2):
            D = df[(df['Outcome'] != 0)]
            H = df[(df['Outcome'] == 0)]
            trace0 = go.Scatter(
                x = D[feat1],
                y = D[feat2],
                name = 'Diabetic',
                mode = 'markers',
                marker = dict(color = 'red',
                    line = dict(
                        width = 1)))

            trace1 = go.Scatter(
                x = H[feat1],
                y = H[feat2],
                name = 'Healthy',
                mode = 'markers',
                marker = dict(color = 'darkturquoise',
                    line = dict(
                        width = 1)))

            layout = dict(title = feat1 +" "+"vs"+" "+ feat2,
                          yaxis = dict(title = feat2,zeroline = False),
                          xaxis = dict(title = feat1, zeroline = False)
                         )

            plots = [trace0, trace1]

            figz = dict(data = plots, layout=layout)
            fig = go.Figure(figz)

            st.plotly_chart(fig,use_container_width = True)

        #The select boxes to pick out the two inputs to place in the function
        first = st.selectbox("Choose the first variable:",
        ("Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"))

        second = st.selectbox("Choose the second variable:",
        ("Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"))
        #Generating the plot based on the two inputs
        plot_feat1_feat2(first,second)

    with col2:
        #Plotting a correlation map
        correlation = df.corr()
        matrix_cols = correlation.columns.tolist()
        corr_array  = np.array(correlation)
        trace = go.Heatmap(z = corr_array,
                              x = matrix_cols,
                              y = matrix_cols,
                              colorscale='teal',
                              colorbar   = dict(),
                             )
        layout = go.Layout(dict(title = 'Correlation Matrix for variables',
                                margin  = dict(r = 0 ,l = 100,
                                                  t = 0,b = 100,
                                                ),
                                yaxis   = dict(tickfont = dict(size = 12)),
                                xaxis   = dict(tickfont = dict(size = 12)),
                                  )
                             )
        fig = go.Figure(data = [trace],layout = layout)

        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.subheader("Correlation Map")
        st.latex("")
        st.caption("The closer the correlation is to 0, the weaker it is. The closer it is to +/-1, the stronger it is")
        col2.plotly_chart(fig,use_container_width = True)

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

        #Intiating a function to plot a Distribution plot based on a selector input and on input of the number of bins
        def plot_distribution(data_select, size_bin) :
            # 2 datasets
            D = df[(df['Outcome'] != 0)]
            H = df[(df['Outcome'] == 0)]
            tmp1 = D[data_select]
            tmp2 = H[data_select]
            hist_data = [tmp1, tmp2]

            group_labels = ['diabetic', 'healthy']
            colors = ['red', 'darkturquoise']

            fig = ff.create_distplot(hist_data, group_labels, colors = colors, show_hist = True, bin_size = size_bin, curve_type='kde', show_rug= False)

            fig['layout'].update(title = data_select)

            fig = go.Figure(fig)

            st.plotly_chart(fig,use_container_width = True)

        st.subheader("Distribution plot")
        #Setting the inputs selectors for the Distribution plot
        first1 = st.selectbox('''Choose a variable:''',
        ("Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"))

        binz = st.number_input("Number of Bins:")

        plot_distribution(first1, binz)

#Setting the prediction page
if selected == "Prediction":
    # Splitting dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(df[['Pregnancies', 'Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']], df['Outcome'], test_size=0.25, random_state=0)
    # Creating the LogisticRegression model
    model_reg = LogisticRegression(C=1)
    model_reg.fit(X_train, y_train)
    y_pred = model_reg.predict(X_test)

    classifier = model_reg

    st.markdown(f'<h1 style="color:#89CFF0;font-size:35px;">{"Diabetes Prediction (for females)"}</h1>', unsafe_allow_html=True)
    st.markdown("""---""")

    # Setting the inputs and naming them as variables
    name = st.text_input("Name:")
    pregnancy = st.number_input("No. of times pregnant:")
    glucose = st.number_input("Plasma Glucose Concentration (120 avg) :")
    bp =  st.number_input("Diastolic blood pressure (mm Hg, 69 avg):")
    skin = st.number_input("Triceps skin fold thickness (mm, 20 avg):")
    insulin = st.number_input("2-Hour serum insulin (mu U/ml,3-25 normal):")
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2, 32 avg):")
    dpf = st.number_input("Diabetes Pedigree Function(0.47 avg):")
    age = st.number_input("Age:")
    submit = st.button('Predict')
    # Setting an IF statement to predict using the model, if the prediction was 0 then a healthy message will appear else otherwise
    if submit:
            prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
            if prediction == 0:
                st.write('Good news',name,"!",'You are not diabetic. 🎉')
                st.balloons()
            else:
                st.write(name," we are really sorry, but it seems like you are Diabetic. We advise you to visit a doctor ASAP.")
