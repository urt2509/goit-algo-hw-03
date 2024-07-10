import random

def get_numbers_ticket(min, max, quantity):
  

    if min >= 0 and max <= 1000 and min <= quantity <= max: #Check parameters of function
        tickets_set = set(random.sample(range(min, max + 1), quantity)) #Create unordered without duplicates set of random numbers in range min-max  
        sorted_tickets = sorted(tickets_set)     #Sort set of numbers   
        return sorted_tickets

    else:
        print("Only integers are allowed. \nEnter values of min more than 0, " 
              "max less or equal to 1000 and quantity between min and max")
        return []

lottery_numbers = get_numbers_ticket(1, 25, 100)
if not lottery_numbers:
    print("Your lottery numbers: ") 
else: 
    print(f"Your lottery numbers: {lottery_numbers}")