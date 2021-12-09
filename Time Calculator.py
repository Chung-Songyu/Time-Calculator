def add_time(start, duration, start_day = False):
  (b, am_pm) = start.split(" ")
  (bh, bm) = b.split(":")
  (dh, dm) = duration.split(":")
  (bh, bm, dh, dm) = (int(bh), int(bm), int(dh), int(dm))

  fm = bm + dm
  fh = bh + dh
  if fm >=60:
    fm -= 60
    fh += 1

  next_day = ""
  not_today = ""
  if bh < 12 and fh >= 12:
    if am_pm == "AM" and fh >= 24:
      next_day = int(fh / 24)
    elif am_pm == "PM" and fh >=12:
      next_day = int((fh - 12) / 24) + 1
    if next_day == 1:
      not_today += "(next day)"
    elif next_day != "" and next_day > 1:
      not_today += "(" + str(next_day) + " days later)"

    timeofday = int(fh / 12)
    if timeofday % 2 == 1:
      if am_pm == "AM":
        am_pm = "PM"
      elif am_pm == "PM":
        am_pm = "AM"

    if fh % 12 != 0:
      fh = fh % 12
    else:
      fh = 12

  if fm < 10:
    fm = "0" + str(fm)

  week = {
    "sunday": 0,
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6
  }
  which_day = ""
  if start_day:
    start_day = start_day.lower()
    if next_day == "":
      next_day = 0
    end_day = week[start_day] + int(next_day)
    if end_day >= 7:
      end_day = int(end_day % 7)
    key = list(week.keys())
    value = list(week.values())
    which_day = key[value.index(end_day)].capitalize()

  if which_day:
    if not_today:
      return str(fh) + ":" + str(fm) + " " + am_pm + ", " + which_day + " " + not_today
    else:
      return str(fh) + ":" + str(fm) + " " + am_pm + ", " + which_day
  else:
    if not_today:
      return str(fh) + ":" + str(fm) + " " + am_pm + " " + not_today
    else:
      return str(fh) + ":" + str(fm) + " " + am_pm

# Example
print(add_time("11:06 PM", "2:02"))
