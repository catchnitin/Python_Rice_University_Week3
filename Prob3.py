#%%

def problem3_3(month, day, year):
    
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
        
    months = ("January", "February", "March","April","May","June","July",\
              "August","September","October","November","December")
    month = month - 1 
    Month_prin = months[month]
    Date_print = Month_prin + " " + str(day) + "," + " " +str(year)
    print(Date_print)