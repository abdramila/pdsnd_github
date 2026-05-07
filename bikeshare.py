import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter a city: ").lower()
    
    while city not in CITY_DATA:
        city = input("Invalid city. Try again: ").lower()

    print("You chose:", city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a month: ").lower()
    
    input_months = ['all', 'i want them all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    while month not in input_months:
        month = input("Invalid month. Try again: ").lower()
    
    print("You chose:", month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a day: ").lower()
    
    days = ('all', 'i want them all', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday') 
    
    while day not in days:
        day = input("Invalid day. Try again: ").lower()
    print("You chose:", day)
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month == 'i want them all':
        month = 'all'
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
         
    if day != 'all':
            df = df[df['day_of_week'] == day.lower()]   
        
    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')  
    start_time = time.time()
    
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('Most common month', months[popular_month - 1].title())
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day', popular_day.title())
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common start station', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common end station', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Both Stations'] = df['Start Station'] + df['End Station']
    most_frequent = df['Both Stations'].mode()[0]
    print('Most frequent trip', most_frequent)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum())
    print('Total travel time', total_travel_time, 'seconds')
    
    # TO DO: display mean travel time
    total_travel_time = round(df['Trip Duration'].mean())
    print('Mean travel time', total_travel_time, 'seconds')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Gender data not available for this city.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest year of birth:\n{}".format(int(df['Birth Year'].min())))
        print("Most recent year of birth:\n{}".format(int(df['Birth Year'].max())))
        print("Most common year of birth:\n{}".format(int(df['Birth Year'].mode()[0])))
    else:
        print('Birth Year data not available for this city.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Display Raw Data from  dataset"""
    
    yes_answers = ['yes','ya','yea','yes thanks','yeah thank you', 'y', 'ye', 'yeah', 'yep', 'sure']
    no_answers = ['no', 'n', 'nah', 'nope', 'no thanks', 'no thank you', 'nah thank you']
    start = 0
    while True:
        show = input("Would you like to see 5 rows of raw data? Enter yes or no: ").lower()
        while show not in yes_answers + no_answers:
            show = input("Please enter yes or no: ").strip().lower()
        if show in no_answers:
            break
        print(df.iloc[start:start+5])
        start += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        yes_answers = ['yes','ya','yea','yes thanks','yeah thank you', 'y', 'ye', 'yeah', 'yep', 'sure']
        no_answers = ['no', 'n', 'nah', 'nope', 'no thanks', 'no thank you', 'nah thank you']

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()

        while restart not in yes_answers + no_answers:
            restart = input("Please enter yes or no.\n").strip().lower()

        if restart in no_answers:
            break



if __name__ == "__main__":
	main()
