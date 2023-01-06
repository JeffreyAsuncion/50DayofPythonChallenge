s = '07:05:45AM'
len_s = len(s)
AM_PM = s[-2:]

if AM_PM == 'PM':
    hour = int(s[:2]) + 12
    # hour = str(hour)
    PM = str(hour) + s[2:-2]
    print(PM)
else:
    print(s[:-2])