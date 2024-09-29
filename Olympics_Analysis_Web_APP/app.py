import streamlit as st
import pandas as pd
import preprocessor, helper

df = pd.read_csv('athlete_events1.csv')
region_df = pd.read_csv('noc_regions1.csv')

df = preprocessor.preprocess(region_df, df)

st.sidebar.header('Olympics Analysis !')
user_manu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')
)

# st.header('Overall Data !')
# st.dataframe(df)

if user_manu == 'Medal Tally':
    st.sidebar.header('Medal Tally')

    years, country = helper.country_year_list(df)
    st.title("This is the Olympics Data Analysis Dashboard !")
    selected_year = st.sidebar.selectbox('Select Year', years)
    selected_country = st.sidebar.selectbox('Select Country', country)
    
    medal_telly = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == "Overall" and selected_country == "Overall":
        st.header("Overall Tally !")

    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.header("Medal Tally in " + str(selected_year) + " Olympics")

    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.header(selected_country + " overall performance")

    elif selected_year != 'Overall' and selected_country != 'Overall':
        st.header(selected_country + " performance in " + str(selected_year) + " Olympics")

    st.table(medal_telly)

if user_manu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.header("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)