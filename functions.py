import re
import random

# convert a date from string to integer (number of days observed since Jan 25, 2020)
def str_to_day(DATE):
    month = re.findall('^2020-([0-9]+)-', DATE)
    month = int(month[0])
    day = re.findall('^2020-[0-9]+-([0-9]+)', DATE)
    day = int(day[0])
    if month==1:
        DAY = day - 25 + 1
    elif month==2:
        DAY = 7 + day 
    elif month==3:
        DAY = 7 + 29 + day
    else:
        DAY = 7 + 29 + 31 + day 
    return DAY


# convert a date from integer to string
def day_to_str(DAY):
    if DAY<=7:
        month = 1
        day = 25 + DAY - 1 
    elif DAY<=36:
        month = 2
        day = DAY - 7
    elif DAY<=67:
        month = 3
        day = DAY - 36
    else:
        month = 4
        day = DAY - 67
    month = str(month)
    day = str(day)
    if int(day)<10:
        DATE = "2020-0"+month+"-0"+day
    else:
        DATE = "2020-0"+month+"-"+day
    return(DATE)


# randomly walk to an adjacent county from the current county
def random_step(Now, AdjM):
    options = list()
    for node in AdjM:
        if AdjM[Now][node]==1:
            options.append(node)
    return(random.choice(options))


# randomly walk from A to B and count the number of crossing borders
def random_path(A, B, AdjM):
    Now = A
    steps = 0
    while True:
        Now = random_step(Now, AdjM)
        steps += 1
        if Now==B:
            break
    return(steps)


# find the shortest path between two counties stochastically
def shortest_path(AdjM, A, B):
    # AdjM is the adjacency dataframe
    if A==B:
        return(0)
    elif AdjM[A][B]==1:
        return(1)
    else:
        distance = list()
        for i in range(100*len(AdjM.index)):
            distance.append(random_path(A,B,AdjM))
        return(min(distance))

    
# check whether the dates are incessant or not
def check_missing(date_list):
    time = [str_to_day(dd) for dd in date_list]
    if time[-1]-time[0]+1=len(time):
        return(True)
    else:
        return(False)
#
