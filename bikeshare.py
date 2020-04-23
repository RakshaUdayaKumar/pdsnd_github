
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

LIST_OF_MONTHS = [ 'january','february','march','april','may','june','all']

LIST_OF_DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input('Enter the name of the city that you would like to explore:').lower()
        while city not in CITY_DATA:
            print('Please enter a city among chicago, new york city and washington')
            city = input('Enter the name of the city that you would like to explore:').lower()

        print('Hello, the city chosen to explore by you is:', city)

    # get user input for month (all, january, february, ... , june)

        month = input("Please enter a month from January to June that you wish to learn about. Please input 'all' if you wish to learn about all the months:").lower()
        while month not in LIST_OF_MONTHS:
            print('Please enter a valid month')
            month = input("Please enter a month from January to June that you wish to learn about.Please input 'all' if you wish to learn about all the months:").lower()

        print('The month that you wish to learn about is:',month)

    # get user input for day of week (all, monday, tuesday, ... sunday)

        day = input("Enter the day of the week that you wish to view data about.Please enter 'all' if you wish to view data for all the days of the week:").lower()
        while day not in LIST_OF_DAYS:
            print('Please enter a valid day')
            day = input("Enter the day of the week that you wish to view data about.Please enter 'all' if you wish to view data for all the days of the week:").lower()

        print('The day of the week that you wish to explore is:', day)

        print('-'*40)
        return city, month, day
    except Exception as e:
        print('An error with your inputs occured: {}'.format(e))


# In[4]:


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
    try:
    # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int

            month = LIST_OF_MONTHS.index(month) +1

        # filter by month to create the new dataframe
            df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

        return df
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    try:
        popular_month_place = df['Start Time'].dt.month.mode()[0]
        popular_month = LIST_OF_MONTHS[popular_month_place-1].title()
        print('The most popular month is:',popular_month)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    try:
    # display the most common day of week
        popular_day = df['day_of_week'].mode()[0]
        print('Most popular day of the week is:',popular_day)
    except Exception as e:
            print('There was an Error that occurred: {}'.format(e))

    try:
    # display the most common start hour
        popular_hour = df['hour'].mode()[0]
        print('Most popular Start hour:', popular_hour)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        print('Most popular start station is', popular_start_station,'in city')
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    # display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        print('Most popular end station is', popular_end_station,'in city')
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    # display most frequent combination of start station and end station trip
    try:
        popular_start_end_comination = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        print('The most popular combination of start and end station is\n',popular_start_end_comination)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        df['time difference'] = df['End Time'] - df['Start Time']
        total_time_difference = df['time difference'].sum()
        print('the total travel time was:',total_time_difference)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))
    # display mean travel time
    try:
        mean_travel_time = df['time difference'].mean()
        print('the mean travel time was:', mean_travel_time)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('The type and number of users in city are\n', user_types)
    except Exception as e:
        print('There was an Error that occurred: {}'.format(e))

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('The number of users and their genders:\n', gender_count)
    except Exception as e:
        print('The gender details for Washington is not available')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode())
        print('\nThe oldest customer was born in\n',earliest_year_of_birth,'\nthe youngest customer was born in\n',most_recent_year_of_birth,'\nthe most frequent customers were born in\n',most_common_year_of_birth)
    except Exception as e:
        print('The birth year details for Washington is not available')
    print("\nThis took %s seconds." % (time.time() - start_time))

def data_view(df):
    wish=input('\nDo you wish to view 5 rows of raw data? Please enter yes or no\n')
    while wish == 'yes':
        print(df.head())
        wish=input('\nDo you wish to view 5 rows of raw data? Please enter yes or no\n')
    else :
        return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
