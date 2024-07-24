from datetime import datetime, date

def get_days_from_today(date):

        try:
            inputed_date = datetime.strptime(date, "%Y-%m-%d").date()
                    
            current_date = datetime.today().date()
            
            days_from_today = (current_date - inputed_date).days
                       
            return days_from_today
        
        except ValueError as e:
             print(e)

            
