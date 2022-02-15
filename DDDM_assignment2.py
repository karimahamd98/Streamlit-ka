import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
import io


st.set_page_config(layout="wide")


col1, col2 = st.columns([8,1])

with col1:
    st.header("Exercise 1. Let's take a look at Nobel prize Laureats")
    st.markdown('''In this exercise we will dive into the Nobel prize
    Laureats dataset by the Nobel Prize Foundation.
    This dataset lists all prize winners from the start
    of the prize in 1901 till 2016''')
    st.text("")
    st.markdown('''The Nobel prize is one of the most famous and prestigious intellectual awards. It is awarded annually for 6
    different categories. From Stockholm, the Royal Swedish Academy of Sciences confers the prizes for physics, chemistry, and economics,
    the Karolinska Institute confers the prize for physiology or medicine, and the Swedish Academy confers the prize for literature. The Norwegian Nobel Committee based in Oslo confers the prize for peace. ''')
    st.write("##")
    st.markdown('''A person or organization awarded the Nobel Prize is called a Nobel Laureate. The word "laureate" refers to the
    laurel wreath (إكليل الغار) that was considered as "a trophy" in ancient greek, given to victors of competitions (image to the right). ''')
    st.write("")
    st.markdown('''The aim of this exercise is to train you on handling dataframes with Pandas. Main visualization library used will be Seaborn (don't stick to it, focus later on Plotly please).''')
    st.write("#")
    st.subheader("Part 1 - Setting up the environment and loading required libraries")
    st.markdown(''' 1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np)

    1.2- Read in the dataset

    1.3- Take a look at the first 10 laureats ''')

    st.text('''
    # 1.2- Read in the dataset
    # Hint: Use pd.read_csv to read in datasets/nobel.csv and save it into a dataframe "nobel"
    nobel = pd.read_csv("C:\\Users\\10User\\Documents\\MSBA\\Spring 22\\MSBA370 - Data Driven Digital Marketing\\DDDM - Pre-Streamlit Exercise Part 1\\datasets\\nobel.csv")
    # 1.3- Take a look at the first 10 laureats
    # Hint: use the method head()
    nobel.head(10)''')
    #nobel = pd.read_csv("C:\\Users\\10User\\Documents\\MSBA\\Spring 22\\MSBA370 - Data Driven Digital Marketing\\DDDM - Pre-Streamlit Exercise Part 1\\datasets\\nobel.csv")
    #st.write(nobel.head(10))
    
    url = 'https://raw.githubusercontent.com/karimahamd98/Streamlit-ka/main/nobel.csv'
    nobel1 = pd.read_csv(url)
    st.write(nobel1.head(10))
    

    st.subheader("Part 2 - Which country had most laureats?")
    st.markdown('''
    Just looking at the first couple of prize winners, or Nobel laureates as they are also called, we already see a celebrity: Wilhelm Conrad Röntgen, the guy who
    discovered X-rays. And actually, we see that all of the winners in 1901 were guys that came from Europe. But that was back in 1901, looking at all winners in
     the dataset, from 1901 to 2016, which country is the most commonly represented? Also, when did it start to dominate the prize?

    (For country, we will use the column birth_country of the winner)''')
    st.text('''
    # Display the number of (possibly shared) Nobel Prizes handed between 1901 and 2016.
    # Hint: Count the number of rows/prizes using the len() function. Use the display() function to display the result.

        display(len(nobel.prize)) ''')
    st.write(len(nobel.prize))
    st.text('''# Count the number of prizes for each birth_country using value_counts() and show the top 10. Do not use display().

    pd.value_counts(nobel.birth_country).head(10)''')
    st.write(pd.value_counts(nobel.birth_country).head(10))

    st.subheader("Part 3 - USA-born laureats by decade")
    st.markdown('''
    3.1 - Calculate the proportion of USA born winners per decade

    3.2 - Display the proportions of USA born winners per decade
    ''')
    st.text('''# 3.1 - Add a usa_born_winner column to nobel, where the value is True when birth_country is "United States of America".

        nobel['usa_born_winner'] = nobel.birth_country == "United States of America"
    ''')
    usa = nobel['usa_born_winner'] = nobel.birth_country == "United States of America"

    st.write(usa)

    st.text('''
    # Add a decade column to nobel for the decade each prize was awarded. Here, np.floor() will come in handy. Ensure the decade column is of type int64.
    # Hint: astype(int)
    # check this example:
    ## year = pd.Series([1843, 1877, 1923])
    ## decade = (np.floor(year / 10) * 10).astype(int)
    ## decade is now 1840, 1870, 1920

      nobel['decade'] = (np.floor(nobel.year/10)*10).astype(int)
    ''')
    nobel['decade'] = (np.floor(nobel.year/10)*10).astype(int)

    st.text('''
    # 3.2- Display the proportions of USA born winners per decade
    # Hint: Use groupby to group by decade, setting as_index=False. Then isolate the usa_born_winner column and take the mean(). Assign the resulting DataFrame to prop_usa_winners.

      prop_usa_winners= nobel.groupby("decade", as_index= False)["usa_born_winner"].mean()
      prop_usa_winners
    ''')
    prop_usa_winners= nobel.groupby("decade", as_index= False)["usa_born_winner"].mean()
    st.write(prop_usa_winners)

    st.subheader("Part 4 - USA laureats, visualized")
    st.markdown('''
    A table is OK, but to see when the USA started to dominate the Nobel charts we need a plot!

    Plot the proportion of USA born winners per decade.

    4.1 - Use seaborn to plot prop_usa_winners with decade on the x-axis and usa_born_winner on the y-axis as an sns.lineplot. Assign the plot to ax.


    4.2 - Fix the y-scale so that it shows percentages using PercentFormatter.
    ''')

    st.text('''
    # Setting the plotting theme (done for you)
     sns.set()
    # and setting the size of all plots. (done for you)
     import matplotlib.pyplot as plt
     plt.rcParams['figure.figsize'] = [20, 9]  # try different numbers once you have the plot

    # Plotting USA born winners
     ax = sns.lineplot(data = nobel,x="decade", y="usa_born_winner")

    # Adding %-formatting to the y-axis (done for you)
     import matplotlib.ticker as mtick
     from matplotlib.ticker import PercentFormatter

    # Use Percent formatter method here
    #Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
     ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ''')
    sns.set()
    plt.rcParams['figure.figsize'] = [20, 9]
    ax = sns.lineplot(data = nobel,x="decade", y="usa_born_winner")
    ax_1 = ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig=ax_1)

    st.subheader("Part 5 - What is the gender of a typical Nobel Prize winner?")
    st.markdown('''
    So the USA became the dominating winner of the Nobel Prize first in the 1930s and had remained since. If we look at the gender of laureats, we see a clear
    imbalande. How significant is this imbalance? And is it better or worse within specific prize categories like physics, medicine, literature, etc.? Let's find out.
    We have to plot the proportions of female laureats by decade split by prize category.

    5.1 - Add the female_winner column to nobel, where the value is True when sex is "Female".


    5.2 - Use groupby to group by both decade and category, setting as_index=False. Then isolate the female_winner column and take the mean(). Assign the resulting DataFrame to prop_female_winners.


    5.3 - Copy and paste your seaborn plot from part 4 (including axis formatting code), but plot prop_female_winners and map the category variable to the "hue" parameter.
    ''')

    st.text('''
      sns.set()
    # and setting the size of all plots. (done for you)
    import matplotlib.pyplot as plt
      plt.rcParams['figure.figsize'] = [11, 9]  # try different numbers once you have the plot

    # 5.1 - Calculating the proportion of female laureates per decade
      nobel['female_winner'] = nobel.sex == "Female"

    # 5.2 - Grouping by both decade and category
    #Hint_link: https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts
      prop_female_winners= nobel.groupby(["decade", "category"],as_index = False)["female_winner"].mean()
    # and not nobel.prop_female_winners because we said "dataframe"

    # 5.3 - Plotting USA born winners with % winners on the y-axis (refer to what you did in part 4)
      f_winners = sns.lineplot(data = nobel,x="decade", y="female_winner",hue = "category", ci = None)
    ''')
    sns.set()
    plt.rcParams['figure.figsize'] = [11, 9]
    nobel['female_winner'] = nobel.sex == "Female"
    prop_female_winners= nobel.groupby(["decade", "category"],as_index = False)["female_winner"].mean()
    f_winners = sns.lineplot(data = nobel,x="decade", y="female_winner",hue = "category", ci = None)
    ax_2 = f_winners.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    st.pyplot(fig=ax_2)

    st.subheader("Part 6 - The first woman to win the Nobel Prize")
    st.markdown('''
    Who was the first woman to receive a Nobel Prize? And in which category?

    6.1 - Select only the rows of 'Female' winners in nobel.


    6.2 -Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
    ''')

    st.text('''
    # 6.1 - Select only the rows of 'Female' winners in nobel.

      nobel[nobel["sex"]=="Female"]

    ''')
    nobel[nobel["sex"]=="Female"]


    st.text('''
    #6.2 - Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
    # Hint: DataFrame.nsmallest(self, n, columns, keep='first')
    # Hint_link: https://www.w3resource.com/pandas/dataframe/dataframe-nsmallest.php
    #Another Hint_link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nsmallest.html

      nobel[nobel.sex == 'Female'].nsmallest(n=1, columns='year', keep="first")
    ''')
    first_women =nobel[nobel.sex == 'Female'].nsmallest(n=1, columns='year', keep="first")
    st.write(first_women)

    st.subheader("Part 7 - Some won more than 1 !")
    st.markdown('''
    Who are these few?

    Extract and display the rows of repeat Nobel Prize winners. Use 'groupby' to group nobel by 'full_name'.
    Use the 'filter' method to keep only those rows in nobel with winners with 2 or more prizes.
    ''')

    st.text('''
    # Selecting the laureates that have received 2 or more prizes.
    nobel.groupby('full_name').filter( lambda two_ormore: len(two_ormore)>1/1)
    # Hint: Here is an example of how to use groupby together with filter. This would keep only those rows with
    birth countries that have had 50 or more winners:
    # nobel.groupby('birth_country').filter(lambda group: len(group) >= 50)
    ''')
    st.write(nobel.groupby('full_name').filter( lambda two_ormore: len(two_ormore)>1/1))


    st.subheader('''
    Part 8 - How old are you when you get the prize?
    Several laureats have received the Nobel prize twice. Marie Curie got the prize in physics for discovering radiation and in chemistry for isolating radium and polonium. John Bardeen got it twice in physics for transistors and superconductivity, Frederick Sanger got it twice in chemistry, and Linus Carl Pauling got it first in chemistry and later in peace for his work in promoting nuclear disarmament. Two organizations also got the prize twice : the Red Cross and the UNHCR.

    But how old are Laureats generally when they get the prize?

    Calculate and plot the age of each winner when they won their Nobel Prize.

    8.1 - Convert the nobel['birth_date'] column to datetime using pd.to_datetime.

    8.2 - Add a new column nobel['age'] that contains the age of each winner when they got the prize. That is, year of prize win minus birth year.

    8.3 - Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.
    ''')
    st.text('''
        # 8.1 - Converting birth_date from String to datetime
            nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
            nobel.info()
        # Hint: https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime

        # 8.2 - Calculating the age of Nobel Prize winners
            nobel['age'] = nobel["year"] - nobel["birth_date"].dt.year

        # 8.3 - Plotting the age of Nobel Prize winners: Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.
        # To make the plot prettier, add the arguments lowess=True, aspect=2, and line_kws={'color' : 'black'}.
            sns.lmplot(data= nobel, x = "year", y="age", lowess=True, aspect=2,line_kws={'color' : 'purple'})
        # Hint_link: https://seaborn.pydata.org/generated/seaborn.lmplot.html
    ''')
    nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
    buffer = io.StringIO()
    nobel.info(buf=buffer)
    val =buffer.getvalue()
    st.text(val)

    nobel['age'] = nobel["year"] - nobel["birth_date"].dt.year
    plt.figure()
    lm = sns.lmplot(data= nobel, x = "year", y="age", lowess=True, aspect=2,line_kws={'color' : 'purple'})
    st.pyplot(lm)

    st.subheader("Part 9 - Age differences between prize categories")
    st.markdown('''
    From the plot above, we can see that people used to be around 55 when they received the prize, but nowadays the average is closer to 65.

    We can also see that the density of points is much high nowadays than befor, and since the number of prizes is still the same (+1), then this means that nowadays many more of the prizes are shared between several people. We can also see the small gap in prizes around the Second World War (1939 - 1945).

    Let's look at age trends within different prize categories (use sns.lmplot).

    You have to Plot how old tha laureats are, within the different price categories.
    ''')

    st.text('''
    # As before, use sns.lmplot to make a plot with year on the x-axis and age on the y-axis. But this time, make one plot per prize category by setting the row argument to 'category'
    # Hint: Copy and paste your solution from task 8 and then add the argument row='category' to the function call..
      sns.lmplot(data= nobel, x = "year", y="age",row = "category" ,lowess=True, aspect=2,line_kws={'color' : 'purple'})
    # Scroll down to see the several plots. One by category. Beautiful!
    ''')
    plt.figure(figsize=(8, 4))
    m_lm = sns.lmplot(data= nobel, x = "year", y="age",row = "category" ,lowess=True, aspect=2,line_kws={'color' : 'purple'})
    st.pyplot(m_lm)

    st.subheader("Part 10 - Oldest and youngest winners")
    st.markdown('''
    Who are the oldest and youngest people ever to have won a Nobel Prize? Pick out the rows of the oldest and the youngest winner of a Nobel Prize.
    ''')
    st.text('''
    # The oldest winner of a Nobel Prize as of 2016
    # Hint: Use nlargest() to pick out and display the row of the oldest winner.
      nobel.nlargest(n=1, columns = "age")''')
    st.write(nobel.nlargest(n=1, columns = "age"))

    st.text('''# The youngest winner of a Nobel Prize as of 2016
    # Hint: Use nsmallest() to pick out and display the row of the youngest winner.
      nobel.nsmallest(n=1, columns='age')

    ''')

    st.write(nobel.nsmallest(n=1, columns='age'))

    st.title("Done. Nobel Prize in Analytics !")

    image = Image.open('laurel-wreath-psd37402-laurel-wreath.png')
    st.image(image, width = 300)


    with col2:
        st.write("##")
        st.write("##")
        st.write("#")
        image = Image.open('laurel-wreath-psd37402-laurel-wreath.png')
        st.image(image, width = 220)
