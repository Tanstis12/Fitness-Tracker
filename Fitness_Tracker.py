#Thomas Anstis
#02/11/2025
#Fitness Tracker

run_time = 0
cycle_time = 0
swim_time = 0

activity = input("What activity would you like to input today (Run/Cycle/Swim)? ")

if activity.lower() == "run":
    run_goal = float(input("How many minutes of running are you aiming to do? "))
    run_minutes = float(input("How many minutes did you actually run for? "))
    run_time = run_time + run_minutes
    print(f"You ran {run_time}/{run_goal} minutes")
    if run_minutes < run_goal:
        print("Try to run futher next time!")
    else:
        print("Congratulations for Reaching your goal!")
elif activity.lower() == "cycle":
    cycle_goal = float(input("How many minutes of cycling are you aiming to do? "))
    cycle_minutes = float(input("How many minutes did you actually cycle for? "))
    cycle_time = cycle_time + cycle_minutes
    print(f"You cycled {cycle_time}/{cycle_goal} minutes")
    if cycle_minutes < cycle_goal:
        print("Try to cycle futher next time!")
    else:
        print("Congratulations for Reaching your goal!")
elif activity.lower() == "swim":
    swim_goal = float(input("How many minutes of swimming are you aiming to do? "))
    swim_minutes = float(input("How many minutes did you actually swim for? "))
    swim_time = swim_time + swim_minutes
    print(f"You swam {swim_time}/{swim_goal} minutes")
    if swim_minutes < swim_goal:
        print("Try to swim futher next time!")
    else:
        print("Congratulations for Reaching your goal!")
else:
    print("Please enter a valid activity")


#Fitness Goal Tracker (Python)
#Developed a console-based fitness tracker that allows users to log running, cycling, or swimming sessions.
#The program compares actual performance against user-defined goals and provides motivational feedback
#. Demonstrated proficiency in Python fundamentals including data types, conditional logic, user input handling, and basic error management.
#Designed with cumulative tracking and modular structure for future scalability.
