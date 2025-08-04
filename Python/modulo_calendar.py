import calendar, cleaner

cleaner.cleaning()

# Mostrar calendario anual:

# print(calendar.calendar(2023))
# calendar.prcal(2023)

# El calendario para un mes específico:
# print(calendar.month(2023, 7))

# La función setfirstweekday()
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2023, 12)

# La función weekday()
# print(calendar.weekday(2023, 12, 24)) # 6 es decir un viernes

# La función weekheader()
# print(calendar.weekheader(2))

# Comprobar si un año es bisiesto
# print(calendar.isleap(2023))
# print(calendar.leapdays(2010, 2023)) 

# Creando un objeto Calendar
# c = calendar.Calendar(calendar.SUNDAY)

# for weekday in c.iterweekdays():
    # print(weekday, end=" ")

# El método itermonthdates()
# c = calendar.Calendar()

# for date in c.itermonthdates(2023, 11):
    # print(date, end=" ")

# Otros métodos que retornan o devuelven iteradores
# c = calendar.Calendar()

# for iter in c.itermonthdays(2023, 11):
    # print(iter, end=" ")

    # El método monthdays2calendar()
# c = calendar.Calendar()

# for data in c.monthdays2calendar(2023, 12):
    # print(data)

c = calendar.Calendar()
 
for weekday in c.iterweekdays():
    print(weekday, end=" ")