import numpy as np
import pandas as pd
import streamlit as st
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.graph_objs import *
init_notebook_mode()
import plotly.express as px
from PIL import Image
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor



st.set_page_config(
    page_title="MS42",
    page_icon="📈",
    layout="wide",
)

st.markdown(f'<h1 style="color:#494949;font-size:50px;">{"📈   The Ultimate Tool"}</h1>', unsafe_allow_html=True)


optionz = st.selectbox('What do you want to view?',('Home Page','EDA Report', 'Visualizations', 'Sales Prediction'))

# Upload CSV data
with st.sidebar.subheader('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload Here", type=["csv"])


# Pandas Profiling Report


if optionz == "Home Page":
    image = "https://63ckz2pq4g240d5ni28x09ke-wpengine.netdna-ssl.com/wp-content/uploads/2021/11/banner-4-3.png"
    st.image(image, width= 1200)
    st.text_area("Overview",'''The ultimate tool is a data analytics tool that utilizes machine learning to predict how much a customer would spend on big sales periods such as Black Friday based on factors that the user input such as the customer's gender, marital status, age, city, number of years they lived in a certain city and product category. The tool also produces exploratory data analysis report for a quick general look. For further analysis, there are visualizations for more insights.
    ''')



    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")




if optionz == "EDA Report":
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file, encoding = 'ISO-8859-1')
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True, dark_mode=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
    else:
        st.info('Awaiting for CSV file to be uploaded.')



csv = pd.read_csv(uploaded_file, encoding = 'ISO-8859-1')

if optionz == "Visualizations":


    kpi1, kpi2, kpi3 = st.columns(3)
    value= csv['Purchase'].mean()
    value=round(value)


    kpi1.metric(
        label="Average️ Amount Spent per Purchase  💲",
        value= "$ {:,}".format(value)

    )


    value=csv["Purchase"].max()

    kpi2.metric(
    label="Maximum Amount spent on a Purchase    ↗️",
    value= "$ {:,}".format(value)
    )


    value= csv["Purchase"].min()


    kpi3.metric(
    label="Minimum Amount spent on a Purchase     ↘️",
    value= "$ {:,}".format(value)
    )


    col1, col2 = st.columns([8,8])

    with col1:

        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Products Sold by Age"}</h1>', unsafe_allow_html=True)

        ageData = sorted(list(zip(csv.Age.value_counts().index, csv.Age.value_counts().values)))
        age, productBuy = zip(*ageData)
        age, productBuy = list(age), list(productBuy)
        ageSeries = pd.Series((i for i in age))



        data = [Bar(x=age,
                       y=productBuy,
                       name="products sold",
                       marker = dict(color=['#00A6EE','#00A6EE' ,'#00A6EE', '#00A6EE', '#00A6EE', '#00A6EE', '#00A6EE'],
                                    line = dict(color='black ', width = 1)))]


        fig1 = Figure(data=data)
        fig1.update_layout(
        xaxis_title="Age Range",
        yaxis_title="Number of Items")
        fig1.update_yaxes(showgrid=False, zeroline=False)

        col1.plotly_chart(fig1,use_container_width = True)


        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Purchases by Occupation"}</h1>', unsafe_allow_html=True)
        fig3 = px.bar(csv, x="Occupation", y="Purchase", color_discrete_sequence =['#00A6EE ']*len(csv))
        fig3.update_yaxes(showgrid=False, zeroline=False, title_text='Purchases')

        col1.plotly_chart(fig3,use_container_width = True)




        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Purchases: Product Category 1"}</h1>', unsafe_allow_html=True)
        fig5= px.bar(csv, x="Product_Category_1", y="Purchase", color_discrete_sequence =['#00A6EE ']*len(csv))
        fig5.update_xaxes(showgrid=False, zeroline=False, title_text='Product Category 1')
        fig5.update_yaxes(showgrid=False, zeroline=False,title_text='Purchases')
        col1.plotly_chart(fig5,use_container_width = True)


    with col2:
        colors = ['#974672 ', '#00A6EE  ']
        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Purchases by Gender"}</h1>', unsafe_allow_html=True)
        fig2 = Figure(data=[Pie(labels=csv["Gender"].unique(), values=csv['Purchase'], hole=.3)])
        fig2.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=1)))
        col2.plotly_chart(fig2,use_container_width = True)


        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Purchases by City Category"}</h1>', unsafe_allow_html=True)
        fig4= px.bar(csv, x="Purchase", y="City_Category", color_discrete_sequence =['#00A6EE ']*len(csv))
        fig4.update_xaxes(showgrid=False, zeroline=False,  title_text='Purchases')
        fig4.update_yaxes(showgrid=False, zeroline=False,  title_text='City Category')
        col2.plotly_chart(fig4,use_container_width = True)

        st.markdown(f'<h1 style="color:#494949;font-size:25px;">{"Purchases: Product Category 2"}</h1>', unsafe_allow_html=True)
        fig6= px.bar(csv, x="Product_Category_2", y="Purchase", color_discrete_sequence =['#00A6EE ']*len(csv))
        fig6.update_xaxes(showgrid=False, zeroline=False, title_text='Product Category 2')
        fig6.update_yaxes(showgrid=False, zeroline=False, title_text='Purchases')
        col2.plotly_chart(fig6,use_container_width = True)









if optionz == "Sales Prediction":

    age_dict = {'0-17': 1,
     '55+': 7,
     '26-35': 3,
     '46-50': 5,
     '51-55': 6,
     '36-45': 4,
     '18-25': 2}

    city_dict = {'A': 0, 'C': 2, 'B': 1}

    csv['Stay_In_Current_City_Years'].replace('4+',4,inplace=True)

    csv['Product_Category_2'].fillna(csv['Product_Category_2'].value_counts().idxmax(),inplace=True)

    csv['Product_Category_3'].fillna(csv['Product_Category_3'].value_counts().idxmax(),inplace=True)


    csv['Gender'] = csv['Gender'].map({"F":0,"M":1})

    csv['Age'] = csv['Age'].map(age_dict)

    csv['City_Category'] = csv['City_Category'].map(city_dict)

    csv['Stay_In_Current_City_Years'] = csv['Stay_In_Current_City_Years'].astype(int)

    Xfeatures = csv[['Gender', 'Age', 'Occupation', 'City_Category',
       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       'Product_Category_2', 'Product_Category_3']]


    scaler = StandardScaler()

    X = scaler.fit_transform(Xfeatures)



    X2 = pd.DataFrame(X,columns=Xfeatures.columns)

    y = csv['Purchase']

    X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.2, random_state=42)

    dtree = DecisionTreeRegressor()

    dtree.fit(X_train,y_train)

    st.subheader("Black Friday Sales Predictor")

    col1,col2 = st.columns(2)

    with col1:

    	gender = st.radio("Gender",("Female","Male"))
    	age = st.selectbox("Age",["0-17","18-25","26-35","36-45","46-50","51-55", "55+"])
    	occupation = st.number_input("Occupation",1,20)
    	city_category = st.selectbox("City Category",["A","B","C"])
    	stay_in_current_city = st.number_input("No of Years of Stay in Current City (1 to 4)",1,4)


    with col2:
        marital_status = st.radio("Marital Status",("Single","Married"))
        product_category_1 = st.number_input("Product 1",1,20)
        product_category_2 = st.number_input("Product 2",1,20)
        product_category_3 = st.number_input("Product 3",1,20)


        age_dict = {'0-17': 1,'55+': 7,'26-35': 3,'46-50': 5,'51-55': 6,'36-45': 4,'18-25': 2}
        gender_dict = {"Female":0,"Male":1}
        marital_status_dict = {"Single":0,"Married":1}
        city_dict = {'A': 0,'B': 1,'C': 2}

        selected_options = {'Gender':gender,'Age':age,'Occupation':occupation, 'City_Category':city_category,
        'Stay_In_Current_City_Years':stay_in_current_city, 'Marital_Status':marital_status, 'Product_Category_1':product_category_1,
        'Product_Category_2':product_category_2, 'Product_Category_3':product_category_3}

        def get_value(val,my_dict):
        	for key,value in my_dict.items():
        		if val == key:
        			return value



        age = get_value(age,age_dict)
        gender_en = get_value(gender,gender_dict)
        city_category_en = get_value(city_category,city_dict)
        marital_status_en = get_value(marital_status,marital_status_dict)
        single_sample = [gender_en,age,occupation,city_category_en,stay_in_current_city,marital_status_en,product_category_1,product_category_2,product_category_2]
        st.write(selected_options)



        if st.button("Predict"):
            sample = np.array(single_sample).reshape(1,-1)
            prediction = dtree.predict(sample)
            st.info("Predicted Purchase")
            st.header("${}".format(prediction[0]))
