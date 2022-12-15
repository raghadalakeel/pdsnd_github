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
    City = input(' enter the name of the city you want: Chicago, New York City , Washington ')
    City = City.casefold()
    while City not in CITY_DATA:
        City = input(' the city name is not valid please try again')
        City = City.casefold()
        
       
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.casefold()
    while month not in months:
        month = input(' the name of the month is not valid please try again')
        month = month.casefold()
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input(' enter the day you want from Sunday to monday or just enter "all"  : ')
    day = day.casefold()
    while day not in days:
        day = input('the name of the day is not valid please try again')
        day = day.casefold()

    
    print('='*50)
    return City, month, day


def load_data(City, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading data file into a dataframe.
    df = pd.read_csv(CITY_DATA[City])

    
    
    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
   
    # Extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    
    # Filtering by month if applicable
    if month != 'all':
        # Useing the index of the months list to get corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filtering by month to create new dataframe
        df = df[df['month'] == month]

        
        
    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating  Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Converting the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    
    # TO DO: display the most common month
    # Extracting month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # Finding the most common month of the year from 1 to 12
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Popular Month is :', months[popular_month-1])

    
    
    # TO DO: display the most common day of week
    # Extracting dayofweek from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # Finding the most common day of the week from 0 to 6
    popular_day = df['day_of_week'].mode()[0]
    days = [ 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    print(' most Popular Day is:', days[popular_day])

    
    
    # TO DO: display the most common start hour
    # Extracting hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # Finding the most common hour from 0 to 23
    popular_hour = df['hour'].mode()[0]
    print('most Popular Start Hour is :', popular_hour)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\ Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    

    # TO DO: display most commonly used start station
    print('most Popular Start Station is : ', df['Start Station'].mode()[0])
        
    
    # TO DO: display most commonly used end station
    print('most Popular End Station: ', df['End Station'].mode()[0])
    
    
    
    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start station and End Station trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    
    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())

    
    
    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n')
        
        
        
    # TO DO: Display earliest, most recent, and most common year of birth 
    if 'Birth Year' in df.columns:
        print('earliest year of Birth:', df['Birth Year'].min())
        print('most Recent year of Birth:', df['Birth Year'].max())
        print('most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def main():
    while True:
        City, month, day = get_filters()
        df = load_data(City, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        #To prompt the user whether they would like want to see the raw data
        enter = ['y','n']
        user_input = input('Would you like to see the raw data? (Enter:Yes/No).\n')
        
        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(_df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see raw data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           

                
                
        restart = input('\nWould you like to restart? (Enter:Yes/No).\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('BYE!')
            break


if __name__ == "__main__":
	main()
