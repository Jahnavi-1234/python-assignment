time = input("Enter the time (HH:MM): ")
hours, minutes = map(int, time.split(':'))
if (hours < 6) or (hours > 18) or (hours == 18 and minutes > 0):
    print("I don't see the sun!")
else:
    total_minutes = (hours - 6) * 60 + minutes
    angle = total_minutes * 0.25
    print(angle)
