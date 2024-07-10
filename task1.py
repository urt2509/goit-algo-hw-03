from datetime import datetime, date
# date = None

def get_days_from_today(date):

   while True:
        
        date = input('Enter your date in format "Year-month-day": ')
        
        try:
            inputed_date = datetime.strptime(date, "%Y-%m-%d").date()
                    
            current_date = datetime.today().date()
            
            days_from_today = (current_date - inputed_date).days
            print(f"The number of days from today: {days_from_today}")

            return days_from_today
        
        except ValueError:
            print(f'Your date {date} is in a wrong format. Please, enter a valid date in format "Year-month-day"')
            
get_days_from_today(date)
