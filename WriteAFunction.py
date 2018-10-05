def is_leap(year):
    leap = False
    x = year%4
    y = year%100
    z = year%400
    if x == 0 and y != 0:
        leap = True
    if x == 0 and y == 0 and z == 0:
        leap = True
    return leap
