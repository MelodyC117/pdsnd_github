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
    print('\nHello! Let\'s explore some US bikeshare data!')

    #################################################################### | Get user input for city name | ####################################################################
    ## First letter of user input will be capitalized, rest lowercase to ensure the program run successfully ##

    while True:
        city = input("\nPlease enter a city - Chicago, New York City, or Washington: ").title()
        if city not in ['Chicago','New York City','Washington']:
            print("\nOooops! It does not appear to be one of the available cities.")
        else:
            ans_c = input('\nYou entered {}. Are you sure you are interested in {}?\nPlease enter YES to continue: '.format(city,city)).upper()
            if ans_c == 'YES':
                print("\nThank You! The city you selected is ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(city))
                break
            else:
                continue
    print()
    print("■□"*60)
    print()

    ###################################################################### | Get user input for month | ######################################################################
    ## Month will be entered as str, then converted to number to filter the data ##
    ## Frist letter of month input will be capitalized to comform with the checking list ##

    while True:
        month = input("\nPlease enter a month - January, February, March, April, May, June - or all: ").title()
        if month != 'All':
            if month not in ['January', 'February', 'March', 'April', 'May', 'June']:
                print("\nOoops! It looks like the month you entered is not one of the available months")
            else:
                ans_m = input('\nYou entered {}. Are you sure you are interested in {}?\nPlease enter YES to continue: '.format(month,month)).upper()
                if ans_m == 'YES':
                    print("\nThank You! The day you selected is ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(month))
                    break
                else:
                    continue
        else:
            ans_me = input("\nYou are interested in all months. Is it intended?\nPlease enter YES to continue: ").upper()
            if ans_me == 'YES':
                break
            else:
                continue
    print()
    print("■□"*60)
    print()

    ###################################################################### | Get user input for day | ######################################################################
    ## First letter of user input will be capitalized, rest lowercase to ensure the program run successfully ##

    while True:
        day = input("\nPlease enter a day of week - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday - or all: ").title()
        if day != 'All':
            if day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                print("\nOoops! It looks like the day you entered is not one of the weekdays.")
            else:
                ans_d = input('\nYou entered {}. Are you sure you are interested in {}?\nPlease enter YES to continue: '.format(day,day)).upper()
                if ans_d == 'YES':
                    print("\nThank You! The day of week you selected is ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(day))
                    break
                else:
                    continue
        else:
            ans_de = input("\nYou are interested in all weekdays. Is it intended?\nPlease enter YES to continue: ").upper()
            if ans_de == 'YES':
                break
            else:
                continue

    #########################################################################################################################################################################
    print()
    print('▓'*120)
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

    ################################################################## | Apply filter on City, Month, Day | ##################################################################
    df = pd.read_csv(CITY_DATA[city.lower()])

    ################################################################### | Convert start time to datetime | ###################################################################
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    ########################################################### | Filter dataframe by user speficied input | #################################################################
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'All':
        df = df[df['Day of Week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    ##################################################################### | Find the most common month | #####################################################################
    most_common_month = df['Month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[most_common_month - 1]
    print("\nThe most common month is:            ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(most_common_month))


    ################################################################## | Find the most common day of week | ##################################################################
    most_common_dow = df['Day of Week'].mode()[0]
    print("\nThe most common day of week is:      ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(most_common_dow))


    ################################################################## | Find the most common day of week | ##################################################################
    most_common_hour = df['Hour'].mode()[0]
    print("\nThe most common hour is:             ••••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••••".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print("■□"*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    ############################################################## | Find the most commonly used start station | ##############################################################
    most_common_start_station = df['Start Station'].mode()[0]
    print("\nThe most common start station is:      ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(most_common_start_station))

    ############################################################### | Find the most commonly used end station | ###############################################################
    most_common_end_station = df['End Station'].mode()[0]
    print("\nThe most common end station is:        ••••••••••••••••••••••••• [ {} ] •••••••••••••••••••••••••".format(most_common_end_station))

    #################################################### | Find the most commonly used combination of start / end station | ###################################################
    df['combination'] = df['Start Station'] + ' ] and [ ' + df['End Station']
    most_frequent_combination = df['combination'].mode()[0]
    print("\nThe most frequent combination is:      ••••••••••• [ {} ] •••••••••••".format(most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print("■□"*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    ######################################################################## | Find total travel time | ########################################################################
    total_travel_time = df['Trip Duration'].sum() / 60 / 60 / 24
    print("\nTotal travel time in days:         ••••••••••••••••••••• [ {:,.2f} days ] •••••••••••••••••••••".format(total_travel_time))

    ######################################################################## | Find mean travel time | #########################################################################
    mean_travel_time = df['Trip Duration'].mean() / 60
    print("\nAverage travel time in minutes:    ••••••••••••••••••••• [ {:.2f} minutes ] •••••••••••••••••••".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print("■□"*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    ####################################################################### | Find counts of user types | ######################################################################
    user_type_counts = df['User Type'].value_counts()
    user_type_counts = user_type_counts.map('{:,}'.format)

    print("\nBelow is a breakdown of user types by total number of users in each type: \n")
    print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")
    print(user_type_counts)
    print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

    ######################################################################### | Find counts of gener | #########################################################################
    try:
        non_null_gender = df[pd.isnull(df['Gender']) == False]
        gender_counts = non_null_gender['Gender'].value_counts()
        gender_counts = gender_counts.map('{:,}'.format)

        print("\nBelow is a breakdown of gender by total number of users in each gender: ")
        print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")
        print(gender_counts)
        print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")

        ####################################################### | Find earliest, most recent, and most common year of birth | ######################################################
        non_null_year = df[pd.isnull(df['Birth Year']) == False]
        earliest_year = int(non_null_year['Birth Year'].min())
        most_recent_year = int(non_null_year['Birth Year'].max())
        most_common_year = int(non_null_year['Birth Year'].mode())

        print()
        print("The earliest birth year is      ••• [ {} ] •••".format(earliest_year))
        print("The most recent birth year is   ••• [ {} ] •••".format(most_recent_year))
        print("The most common birth year is   ••• [ {} ] •••".format(most_common_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print()
        print("■□"*60)
    except:
        print("Looking for Gender and Birth Year Data ...\n\nSorry, there isn't any Gender and Birth Year data available.")

def show_all(df):
    while True:
        i = 1
        show_more = input("\nWould you like to see the first 5 rows of all data? Enter YES to continue: ").upper()
        if show_more == 'YES':
            print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")
            print(df[i:i+5])
            print("\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")
            i += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_all(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.upper() != 'YES':
            break


if __name__ == "__main__":
	main()
