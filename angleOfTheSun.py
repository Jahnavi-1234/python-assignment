# Find the angle of the sun above the horizon knowing the time of the day.
time = input("Enter the time (HH:MM): ")
hours, minutes = map(int, time.split(':'))  # Split the input into hours and minutes and convert them to integers
if (hours < 6) or (hours > 18) or (hours == 18 and minutes > 0):  # If it is before 6 AM or after 6 PM or equal to 6
    print("I don't see the sun!") # If it is not day time it print I don't see the sun
else:
    total_minutes = (hours - 6) * 60 + minutes  #Calculate the total number of minutes that have passed since 6 AM
    # Determine the angle of the sun based on the total minutes since 6 AM
    angle = total_minutes * 0.25 #The sun moves at a rate of 0.25 degrees per minute
    print(angle)
