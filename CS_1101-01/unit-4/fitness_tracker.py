#!/usr/bin/env python3
'''
This is a fitness tracking program that:
    - record user exercise data (steps, minutes, and calories burned)
    - calculate the weekly averages of performed exercises
    - Display the performance summary like:
        - if daily goal were met
        - weekly average
'''
# Global Variable for name and daily goal
name = 'Usman'; dailygoal = 500

# Get system Date and Time
from datetime import datetime
Date = datetime.today()
Time = datetime.now()
hour = int(Time.strftime('%H'))

# Calculate weekly averages
def WeeklyAvg():
    step = 0.0; minutes = 0.0; calories = 0.0
    # Collect, save, extract, and calculate the weekly average stepance of a daily exercise
    for day in range(7):
        print(f"DAY {day + 1}")
        day = DailyData()
        for key, value in day.items():
            if key == 'Step':
                step += value
            elif key == 'Minutes':
                minutes += value
            else:
                calories += value
    
    # Calculate the average of steps, minutes, and calories burned respectively
    average = {
            'Steps': step / 7,
            'Minutes': minutes / 7,
            'Calories': calories / 7
            }
    
    return average

# This function collect information about a day exercise
def DailyData():
    exercise_data = {
            'Step': 0.0,
            'Minutes': 0.0,
            'Calories': 0.0
            }
    for key in exercise_data:
        if key == 'Step':
            print(f"How many steps today?")
        elif key == 'Minutes':
            print(f"How many minute(s) today?")
        else:
            print(f"How many calories burned today?")
        print("----------------")
        print("| Digits only! |")
        print("----------------", end=' ')
        exercise_data[key] = float(input('=> '))
    
    return exercise_data

# This function show perfomance summary
def Summary (user_name, average_dict):
     # Invoke DailyData() to record exercise data
    exercise_data = DailyData()
    print("- - - - - - - - - - - -")

    # Greeting by the time of the day
    if hour < 12:
        print(f"Good Morning! {user_name} :)")
    elif 12 <= hour < 18:
        print(f"Good Afternoon! {user_name} :)")
    else:
        print(f"Good Evening! {user_name} :)")
    
    # Check stepance
    if dailygoal > exercise_data['Step']:
        print("You do not complete the daily goal :(")
    elif dailygoal < exercise_data['Step']:
        print("You are extra-ordinary! :)")
    else:
        print("You did well today!")

    # Display stepance summary
    print("- - - - - - - - -")
    print("This is your performance summary for today exercise:")
    print(f"\t{Date.strftime('%b %d, %Y')} [{Time.strftime('%H:%M')}].")
    print("- - - - - - - - -")
    for key, value in exercise_data.items():
        print(f"\t{key}: {value}")
    print("- - - - - - - - -")
    print(f"This is your average performance summary for this week exercises:")
    print("- - - - - - - - -")
    for key, value in average_dict.items():
        print(f"\t{key}: {value}")
    print("- - - - - - - - -")
   
Summary(name, WeeklyAvg())
