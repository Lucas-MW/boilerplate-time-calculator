import math
def add_time(start, duration,day=""):
  days = ["monday","tuesday","wednesday","thursday","friday","saturday", "sunday"]
  new_time = ""
  new_h , new_m = 0, 0
  day_later = 0
  curr_day = ""
  #start
  s_time = start.split()[0]
  s_period = start.split()[1]
  s_hour = int(s_time.split(":")[0])
  s_min = int(s_time.split(":")[1])
  #duration
  d_hour = int(duration.split(":")[0])
  d_min = int(duration.split(":")[1])
  #check min
  if d_min + s_min < 60:
    new_m = str(d_min + s_min)
  else:
    new_m = str(d_min + s_min - 60)
    s_hour += 1
      
  #check hour "AM"
  if s_period == "AM":
    if d_hour + s_hour < 12:
      new_h = d_hour + s_hour
    # >= 12 AM
    else:
      if d_hour + s_hour == 12:
        new_h = 12
        s_period = "PM"
      else:
        day_later = (d_hour + s_hour) // 24
        if day_later == 0:
          new_h = (d_hour + s_hour) - 12
          s_period = "PM"
        else:
          new_h = (d_hour + s_hour) % 12
          if day_later % 2 == 0:
            s_period = "PM"
          else:
            s_period = "AM"
    #CHECK HOUR "PM"
  else:
    if d_hour + s_hour <= 12:
      new_h = d_hour + s_hour
    # > 12 PM
    else:
      s_period = "AM"
      new_h = (d_hour + s_hour) % 12
      if new_h == 0:
        new_h = 12
      
      day_later = math.ceil((d_hour + s_hour) / 24)

  #format min
  if int(new_m) < 10:
    new_m = "0" + str(new_m)

  #check third parameter: day
  if day.lower() in days:
    day = day.lower()
    if day_later == 0:
      curr_day = day.capitalize()
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period + ", " + curr_day
    elif day_later == 1:
      curr_day = days[days.index(day) + 1].capitalize()
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period + ", " + curr_day + " " + "(next day)"
    else:
      temp = (days.index(day) + day_later) % 7
      curr_day = days[temp].capitalize()
      
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period + ", " + curr_day + " " + "(" + str(day_later) + " days later)"
  #no third parameter
  else:
    #check how many days later
    if day_later == 0:
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period
    elif day_later == 1:
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period + " " + "(next day)"
    else:
      new_time = str(new_h) + ":" + str(new_m) + " " + s_period + " " + "(" + str(day_later) + " days later)"
    
  return new_time
