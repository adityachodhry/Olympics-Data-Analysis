import pandas as pd
import numpy as np

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df

    elif year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]

    elif year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]

    elif year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]
        
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x

def medal_telly(df):

    medal_telly = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    medal_telly = medal_telly.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending = False).reset_index()

    medal_telly['total'] = medal_telly['Gold'] + medal_telly['Silver'] + medal_telly['Bronze']

    return medal_telly


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years, country

def data_over_time(df, col):

    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index()
    nations_over_time.columns = ['Year', col] # Rename the columns for clarity
    nations_over_time = nations_over_time.sort_values('Year')
    return nations_over_time

def most_successful(df, Sport):
    temp_df = df.dropna(subset=['Medal'])
    if Sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == Sport]
    
    successful_athletes = temp_df['Name'].value_counts().reset_index().head(15)
    
    # Rename the columns so that 'index' becomes 'Name'
    successful_athletes.columns = ['Name', 'Medal_Count']

    # Merge with the original DataFrame to get additional information
    x = successful_athletes.merge(df, on='Name', how='left')[['Name', 'Medal_Count', 'Sport', 'region']].drop_duplicates(subset='Name')
    return x