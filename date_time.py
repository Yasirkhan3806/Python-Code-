# from datetime import datetime
# import sys

# def main():
#    print (calculating_minutes())
#     # print(today_date)
#     # userdate = get_user_date()
#     # print(userdate.split('-'))
#     # print(userdate)

# def get_user_date():
#     # while True:
#         try:
#             user_date = input("Enter your date of birth: ")
#             return (datetime.strptime(user_date,"%Y-%m-%d")).strftime("%Y-%m-%d")
#         except ValueError:
#             sys.exit("Invalid date")


            

# def get_today_date():
#     now = datetime.now()
#     return (now.strftime("%Y-%m-%d")).split("-")
    
# def calculating_minutes():
#      today_date = get_today_date()
#      user_date = get_user_date()
#      user_date_arr = user_date.split("-")
#      return 12 - 09
#     #  total_years = int(today_date[0]) - int(user_date_arr[0])
#     #  total_months = int(today_date[1]) - int(user_date_arr[1])
#     #  total_days = int(user_date[2]) - int(today_date[2])
# #      return total_years * total_months * total_days
     


# # print("Formatted Date:", formatted_date)
# if __name__ == '__main__':
#     main()
# from datetime import datetime

# # Example dates as strings
# date1_str = input("date:")
# date2_str = "2024-08-09"

# # Convert strings to datetime objects
# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# # Subtract dates to get a timedelta object
# difference = date2 - date1
# minutes = difference.days * 24 * 60
# print(difference.ye)

# print(minutes)
# 
# from datetime import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from num2words import num2words
import sys



date1_str = input("Enter your date of birth (YYYY-MM-DD): ")
date2_str = datetime.now()
try:
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please enter in YYYY-MM-DD format.")
    sys.exit()
# formatted_datetime = date2_str.strftime("%Y-%m-%d %H:%M:%S")
difference = relativedelta(date2_str, date1)
calculate_leap = difference.years / 4
minutes = difference.years * 365 * 24 * 60 + (int(calculate_leap))
minutes_in_words = num2words(minutes)
refined = minutes_in_words.replace("and","")
print(refined)

