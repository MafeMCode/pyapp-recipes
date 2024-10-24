import datetime

def dailyRecipeNumber(number):
    
    today = datetime.date.today()
    
    dailyNumber = int(today.day) + int(today.month) + int(today.year)
    
    while dailyNumber > number:
        dailyNumber=dailyNumber-number
        
    return int(dailyNumber)