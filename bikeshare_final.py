import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        city = input("\nWhich city would you like to analyze? Chicago, New York City or Washington? :").title()
        if city not in ('Chicago', 'New York City', 'Washington'):
            print('Sorry, not an appropriate choice. Please try again.')
            continue
        else:
            print('You have selected {}. Please continue.'.format(city))
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month would you like to filter by? January, February, March, April, May or June?\n To apply no filter, enter 'all': ").title()
        if month not in('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print('Sorry, not an appropriate choice. Please try again.')
        elif month == 'All':
            print('You have decided to apply no filter.')
            break
        else:
            ('You have selected {}. Please continue.'.format(month))
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday
    while True:
        dow = input("\nWould you like to filter the data by a particular day of the week?\n Please enter the day as follows: Monday, Tuesday, ..., Sunday.  \n To apply no filter, enter 'all': ").title()
        if dow not in('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print('Sorry, not an appropriate choice. Please try again.')
        elif dow == 'All':
            print('You have decided to apply no filter.')
            break
        else:
            ('You have selected {}.'.format(dow))
            break


    print('-'*40)
    return city, month, dow


def load_data(city, month, dow):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df_citydata = pd.read_csv(CITY_DATA[city])

    df_citydata['Start Time'] = pd.to_datetime(df_citydata['Start Time'])

    df_citydata['month'] = df_citydata['Start Time'].dt.month_name()
    df_citydata['dow'] = df_citydata['Start Time'].dt.weekday_name

    if month != 'All':
        df_citydata = df_citydata[df_citydata['month'] == month]

    if dow != 'All':
        df_citydata = df_citydata[df_citydata['dow'] == dow.title()]

    df_citydata['hour'] = df_citydata['Start Time'].dt.hour

    return df_citydata


def time_stats(df_citydata, month, dow):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_pop_month = df_citydata['month'].mode()[0]
    # TO DO: display the most common day of week
    most_pop_dow = df_citydata['dow'].mode()[0]
    # TO DO: display the most common start hour
    most_pop_hour = df_citydata['hour'].mode()[0]

    if month == 'All' and dow == 'All':
        print('The most popular month, day of week and hour is {}, {} and {}, respectively.'.format(most_pop_month, most_pop_dow, most_pop_hour))
    elif month != 'All' and dow == 'All':
        print('Based on your selected month, {}, the most popular day of week and hour is {} and {}, respectively.'.format(month, most_pop_dow, most_pop_hour))
    elif month == 'All' and dow != 'All':
        print('Based on your selected day of week, {}, the most popular month and hour is {} and {}, respectively.'.format(dow, most_pop_month, most_pop_hour))
    else:
        print('Based on your selected month, {}, and day of week, {}, the most popular hour is {}.'.format(month, dow, most_pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df_citydata):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df_citydata['Start Station'].value_counts().idxmax(axis=0)

    # TO DO: display most commonly used end station
    end_station = df_citydata['End Station'].value_counts().idxmax(axis=0)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combination = df_citydata.groupby(['Start Station', 'End Station']).size().idxmax()

    print('The most popular start station and end station are {} and {}, respectively.'.format(start_station, end_station))
    print('The most popular combination of start and end station is: ', start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df_citydata):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_sec = round(sum(df_citydata['Trip Duration']))
    total_travel_time_min = round(total_travel_time_sec/60)
    total_travel_time_h = round(total_travel_time_min/60)
    total_travel_time_d = round(total_travel_time_h/24)

    print("The total travel time is {} seconds, which corresponds to {} minutes, {} hours or {} days.".format(total_travel_time_sec, total_travel_time_min, total_travel_time_h, total_travel_time_d))

    # TO DO: display mean travel time
    mean_travel_duration_sec = round(df_citydata['Trip Duration'].mean())
    mean_travel_duration_min = round(mean_travel_duration_sec/60, 2)

    print("The mean travel time is {} seconds, which corresponds to {} minutes.".format(mean_travel_duration_sec, mean_travel_duration_min))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df_citydata):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df_citydata['User Type'].value_counts()
    print("User Types:\n", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df_citydata['Gender'].fillna('Undefinded').value_counts()
        print("\nGender Types:\n", gender)
    except KeyError:
        print('\nNo data available for the gender.')

    #TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_year = np.round(df_citydata['Birth Year'].dropna(0)).astype(int)
        earliest_year = birth_year.min()
        most_recent_year = birth_year.max()
        most_common_year = birth_year.value_counts().idxmax()
        print('\nThe earliest year of birth is {}, the most recent year is {} and the most common year is {}.'.format(earliest_year, most_recent_year, most_common_year))
    except KeyError:
        print('\nNo data available for the year of birth.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df_citydata):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs 'yes'. Iterate until user respond with a 'no'
    """
    raw_dataline = 0
    while True:
        raw_data_display = input("\nWould you like to see 5 (more) lines of raw data? Enter yes or no: ")
        if raw_data_display == 'yes':
            df_data_display = df_citydata.iloc[raw_dataline: raw_dataline + 5]
            with pd.option_context('display.max_rows', 5, 'display.max_columns', 12):
                print('\n',df_data_display)
            raw_dataline += 5
            continue
        elif raw_data_display == 'no':
            break
        else:
            print('\nSorry, not an appropriate choice. Please try again.')
            continue


def main():
    while True:
        city, month, dow = get_filters()
        df_citydata = load_data(city, month, dow)

        time_stats(df_citydata, month, dow)
        station_stats(df_citydata)
        trip_duration_stats(df_citydata)
        user_stats(df_citydata)
        raw_data(df_citydata)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
