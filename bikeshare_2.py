import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
a=[]
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
    city=input("would you like to see data for chicago,new york or  washington?\n")
    while(city  != 'chicago' and city  != 'new york city' and city  != 'washington' ):
        city=input("please choose correctly between chicago, new york city, washington\n")  
    a.append(city)
    # get user input for month (all, january, february, ... , june)
    month=input("would you like specific month from january to june or you want all?\n")
    list = ["all","january","february","march","april","may","june"]
    while(not list.__contains__(month) ):
        month=input("please choose correctly between all,january,february,march,april,may,june,\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("would you like specific day in the week or not if so type all\n")
    list = ["all","monday","tuesday","wednsday","thursday","friday","saterday","sunday"]
    while(not list.__contains__(day) ):
        day=input("please choose correctly between all,monday,tuesday,wednsday,thursday,friday,saterday,sunday\n")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable
    Args:
        (str) city - name of the city to analyze
        
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df= pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name
    df['hour']=df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df=df[df['month']==month]
    if day !='all':
        df=df[df['day']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month:' ,df['month'].mode()[0],'    ')

    # display the most common day of week
    print('the most common day:' ,df['day'].mode()[0], '    ')

    # display the most common start hour
    print('the most common hour:' ,df['hour'].mode()[0],'\n')

    print("\nThis took %s seconds:" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most common used start station:' ,df['Start Station'].mode()[0], '    ')

    # display most commonly used end station
    print('the most common used end station:' ,df['End Station'].mode()[0], '    ')

    # display most frequent combination of start station and end station trip
    df['start_end station']=df['Start Station']+df['End Station']
    print('the most frequent combination of start station and end station trip:' ,df['start_end station'].mode()[0],'\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total travel time: ',df['Trip Duration'].sum() , '    ')

    # display mean travel time
    print('the mean travel time: ',df['Trip Duration'].mean() , '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types',df.groupby('User Type')['User Type'].count(),'    '   )
    # Display counts of gender
    if not a.__contains__('washington'):
        print('counts of Gernder',df.groupby('Gender')['Gender'].count(),'    ')

    # Display earliest, most recent, and most common year of birth
        print('earliest year of birth:' , int(df['Birth Year'].min()) , '   most recent year of birth:',int(df['Birth Year'].max()) ,'most common year of birth:',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data != 'no' or start_loc+5 < df.size()):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
