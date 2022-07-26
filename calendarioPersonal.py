# GUI
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Add a costume font
# import pyglet

# Get current time
import time
import calendar
from datetime import date

def main():
    mainWindow = tk.Tk()
    mainWindow.title('Calendario Personal')
    mainWindow.config(width = 999, height = 400)
    mainWindow.resizable(False, False)
    # Shows hour/weekday/day/month/year
    def show_date(mainWindow):
        # Get current time
        today = time.ctime()
        # Separates date's elements
        today = today.split(' ')
        # Weekday, numDay, month, year
        todayDate = today[0] + ' ' + today[2] + ' ' + today[1] + ' ' + today[4]
        # Use a costum font
        # pyglet.font.add_file('DS-DIGIB.TTF')
        tk.Label(mainWindow, text = today[3], font = ('DS-DIGIB.TTF', 90)).place(x = 40, y = 80)
        tk.Label(mainWindow, text = todayDate, fg ='#B3B6B7', font = ('DS-DIGIB.TTF', 25)).place(x = 150, y = 220)
        # Returns current date with weekday and month
        return todayDate

    # Shows entire Calendar
    def show_calendar(mainWindow, currentMonth, currentYear):
        
        today = date.today()
        if(currentMonth == None):
            currentYear = today.year
            currentMonth = today.month
            dateName = calendar.month_name[today.month]
            year = str(today.year)
            
            dateName = dateName + ' ' + year
        else:
            dateName = calendar.month_name[currentMonth]
            year = str(currentYear)
            dateName = dateName + ' ' + year

        
        numDias = 31
        a = 10
        i = 0
        # get the first-day of the month
        firstDay = calendar.monthrange(currentYear, currentMonth)
        weekDay = int(firstDay[0])

        def configure_day(delete):
            week = weekDay 
            day = 1
            posx = week * 50
            posy = 90
            # Show every day in the week/month selected  
            def deleteMonthDays():
                deletedDay = 1
                while deletedDay <= numDias:
                    killday = mainWindow.nametowidget(deletedDay)
                    killday.place_forget()
                    deletedDay += 1

            while day < numDias:
                while week < 7:
                    if(day == today.day and currentMonth == today.month):
                        tk.Button(mainWindow, text = day, name = str(day), bg = '#CACFD2', border = 0, width= 5, height = 2).place(x = posx + 600, y = posy)
                        if(delete != None):
                            deleteMonthDays()
                    else:
                        tk.Button(mainWindow, text = day, name = str(day), border = 0, width= 5, height = 2 ).place(x = posx + 600, y = posy)
                        if(delete != None):
                            deleteMonthDays()
                    if(day >= numDias):
                        break
                    week += 1
                    day +=1
                    posx += 50
                week = 0
                posx = 0
                posy += 45

        configure_day(None) 
        def year_comprobation(mainWindow, currentMonth, currentYear):
            if(currentMonth > 12):
                configure_day('1')
                show_calendar(mainWindow, 1, currentYear + 1)
            elif(currentMonth == 0):
                configure_day('1')
                show_calendar(mainWindow, 12, currentYear - 1)
            else:
                configure_day('1')
                show_calendar(mainWindow, currentMonth, currentYear)

        tk.Button(mainWindow, text = dateName, fg ='#000000', border = 0, justify = 'center', width = 14, font = ('DS-DIGIB.TTF', 24)).place(x = 640, y = 0)
        tk.Button(mainWindow, text= '◄', fg ='#000000', border = 0, font = ('DS-DIGIB.TTF', 24), command = lambda: year_comprobation(mainWindow, currentMonth - 1, currentYear)).place(x = 600, y = 0)
        tk.Button(mainWindow, text= '►', fg ='#000000', border = 0, font = ('DS-DIGIB.TTF', 24), command = lambda: year_comprobation(mainWindow, currentMonth + 1, currentYear)).place(x = 895, y = 0)
        # Show dayweeks over the columns
        while i < 8:
            if(i == 0):
                tk.Label(mainWindow, text = 'Mo', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 1):
                tk.Label(mainWindow, text = 'Tu', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 2):
                tk.Label(mainWindow, text = 'We', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 3):
                tk.Label(mainWindow, text = 'Th', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 4):
                tk.Label(mainWindow, text = 'Fr', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 5):
                tk.Label(mainWindow, text = 'Sa', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            elif(i == 6):
                tk.Label(mainWindow, text = 'Su', fg ='#979A9A', font = ('DS-DIGIB.TTF', 12)).place(x = a + 600, y = 60)
            a += 50
            i += 1
        
    # Bucle with tkinter mainloop()
    show_calendar(mainWindow, None, None)
    def myMainLoop():
        show_date(mainWindow)
        mainWindow.after(1, myMainLoop)
    mainWindow.after(1, myMainLoop)
    mainWindow.mainloop()

main()