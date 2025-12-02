
# Bikeshare Project - Refactoring Stage
# Author: Doua Nemier
# Description: Script rewritten and cleaned as part of refactoring branch

"""
Bikeshare Data Analysis Script

This script analyzes bikeshare data for three cities in the United States:
    - Chicago
    - New York City
    - Washington

The user can filter the data by:
    - City
    - Month
    - Day of the week

The program then calculates:
    - Popular travel times
    - Station usage
    - Trip durations
    - User statistics

This file was created as part of the PDSND GitHub project.
"""

# ---------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------
import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_user_input(prompt, valid_options):
    """Simplifies repeated input validation loops."""
    valid_lower = [str(x).lower() for x in valid_options]
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_lower:
            return user_input
        else:
            print("Invalid input. Please try again.\n")

def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print("Hello! Let's explore some US bikeshare data!\n")
    valid_cities = list(CITY_DATA.keys())
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    city = get_user_input("Choose a city (Chicago, New York City, Washington): ", valid_cities)
    month = get_user_input("Choose a month (all, january, ... , june): ", valid_months)
    day = get_user_input("Choose a day (all, monday, ... sunday): ", valid_days)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def most_common(df, column_name):
    """Returns the most common value in a DataFrame column."""
    return df[column_name].mode()[0]

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start = time.time()

    if 'month' in df.columns and not df['month'].empty:
        print("Most Common Month:", df['month'].mode()[0])
    else:
        print("Month data not available.")

    if 'day_of_week' in df.columns and not df['day_of_week'].empty:
        print("Most Common Day:", df['day_of_week'].mode()[0])
    else:
        print("Day of week data not available.")

    if 'hour' in df.columns and not df['hour'].empty:
        print("Most Common Start Hour:", df['hour'].mode()[0])
    else:
        print("Hour data not available.")

    print("Time:", time.time() - start)
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start = time.time()

    if 'Start Station' in df.columns:
        print("Most Common Start Station:", df['Start Station'].mode()[0])
    else:
        print("Start Station data not available.")

    if 'End Station' in df.columns:
        print("Most Common End Station:", df['End Station'].mode()[0])
    else:
        print("End Station data not available.")

    if 'Start Station' in df.columns and 'End Station' in df.columns:
        df['trip'] = df['Start Station'] + " to " + df['End Station']
        print("Most Common Trip:", df['trip'].mode()[0])
    else:
        print("Trip combination data not available.")

    print("Time:", time.time() - start)
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on trip duration."""
    print('\nCalculating Trip Duration...\n')
    start = time.time()

    if 'Trip Duration' in df.columns:
        print("Total Travel Time:", df['Trip Duration'].sum())
        print("Mean Travel Time:", df['Trip Duration'].mean())
    else:
        print("Trip Duration data not available.")

    print("Time:", time.time() - start)
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start = time.time()

    if 'User Type' in df.columns:
        print("User Types:")
        print(df['User Type'].value_counts())
    else:
        print("User Type data not available.")

    if 'Gender' in df.columns:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())
    else:
        print("Gender data not available.")

    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))
    else:
        print("Birth Year data not available.")

    print("Time:", time.time() - start)
    print('-'*40)

def display_raw_data(df):
    """Displays raw data in increments of 5 rows upon user request."""
    start_loc = 0
    view_data = input("\nWould you like to view 5 rows of raw data? Enter yes or no: ").lower()
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("View more? Enter yes or no: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input("\nWould you like to restart? (yes/no): ").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()