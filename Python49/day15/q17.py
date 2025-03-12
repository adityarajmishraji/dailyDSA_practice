# # Write a Python to display calender

# import calender

# year = int(input("Enter Year : "))
# month = int(input("Enter Month : "))

# cal = calender.month(year,month)
# print(cal)

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    """Return the number of days in a given month of a year."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap year in February
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

def get_first_day_of_month(year, month):
    """Calculate the first day of the month using Zeller’s Congruence Algorithm."""
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    first_day = (1 + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7
    
    return (first_day + 6) % 7  # Adjusting to make Sunday = 0, Monday = 1, etc.

def print_calendar(year, month):
    """Print a calendar for a given month and year."""
    days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    num_days = get_days_in_month(year, month)
    first_day = get_first_day_of_month(year, month)

    # Print the calendar header
    print(f"\n{['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month - 1]} {year}")
    print(" ".join(days_of_week))

    # Print space before the first day
    print("    " * first_day, end="")

    # Print the days
    for day in range(1, num_days + 1):
        print(f"{day:2d}  ", end="")
        if (first_day + day) % 7 == 0:  # New line after Saturday
            print()
    
    print("\n")

# User Input
year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))

# Display Calendar
print_calendar(year, month)