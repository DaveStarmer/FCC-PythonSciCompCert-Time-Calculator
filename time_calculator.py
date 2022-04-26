def add_time(start, duration,startDay = None):
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if startDay == None:
      day = None
    else:
      try:
        day = days_of_week.index(startDay.capitalize())
      except ValueError:
        # day text not found
        day = None
    
    ampm = start[-2:]
    mins = int(start[-5:-3])
    hours = int(start[:-6])
    hours += (12 if ampm=="PM" else 0)

    addH = int(duration[:-3])
    addM = int(duration[-2:])

    mins += addM
  
    # add additional hours if sum of minutes is greater than 60
    addH += (mins) // 60
    mins = mins % 60

    hours += addH
    days_later = hours // 24
    hours = hours % 24

    if (hours >= 12):
        new_ampm = " PM"
        hours -= 12
    else:
      new_ampm = " AM"
    if hours == 0:
      hours = 12;
    new_time = str(hours) + ":" + "{:0>2d}".format(mins) + new_ampm
    if day is not None:
        new_time += ", " + days_of_week[(day + days_later) % 7]

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += " (" + str(days_later) + " days later)"
    return new_time