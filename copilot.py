#Laura Collins
#V00763363
#Date: 2026-02-08
from datetime import datetime, date

birthday =input("Enter your birthday (YYYY-MM-DD):")
today = date.today()

# Parse the dates using strptime
birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
 # today is already a date object
# Calculate the difference in days
days_difference = abs((today - birthday).days)


print("Number of days between today and your birthday:", days_difference)

#Test case 1: Invalid Input by using Feb 30 which doesn't exist. 