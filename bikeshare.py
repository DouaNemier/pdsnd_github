import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city 
        (str) month 
        (str) day
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city
    while True:
        city = input("Which city (Chicago, New York City, Washington)? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid entry. Please choose Chicago, New York City, or Washington.")

    # get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Month (January to June or 'all')? ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Try again.")

    # get user input for day of week
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input("Day of week or 'all'? ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Returns:
        df - Pandas DataFrame
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week + hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start = time.time()

    common_month = df['month'].mode()[0]
    common_day = df['day_of_week'].mode()[0]
    common_hour = df['hour'].mode()[0]

    print("Most Common Month:", common_month)
    print("Most Common Day:", common_day)
    print("Most Common Start Hour:", common_hour)
    
    print("Time:", time.time() - start)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start = time.time()

    print("Most Common Start Station:", df['Start Station'].mode()[0])
    print("Most Common End Station:", df['End Station'].mode()[0])

    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most Common Trip:", df['trip'].mode()[0])

    print("Time:", time.time() - start)


def trip_duration_stats(df):
    """Displays statistics on trip duration."""
    print('\nCalculating Trip Duration...\n')
    start = time.time()

    print("Total Travel Time:", df['Trip Duration'].sum())
    print("Mean Travel Time:", df['Trip Duration'].mean())

    print("Time:", time.time() - start)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start = time.time()

    print("User Types:")
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print("Time:", time.time() - start)


def display_raw_data(df):
    """Displays raw data in increments of 5 rows."""
    view = input("\nWould you like to view 5 rows of data? (yes/no): ").lower()
    start_loc = 0
    
    while view == 'yes':
        print(df.iloc[start_loc:star
        t_loc+5])
        start_loc += 5
        view = input("View more? (yes/no): ").lower()


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