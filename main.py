import datetime

def get_days_from_today(date):
    try:
       
        inputed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        # print(inputed_date, type(inputed_date))
        today = datetime.today()
        print(today)


    except NameError:
        print(f'{date} is not in a particular format')

date = "5"
# get_days_from_today(date)