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

import os

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

        

        def add_event(nombreBoton):
            addEventWindow = Toplevel(mainWindow)
            def save_event(seleccionHora,seleccionMinuto,seleccionAMPM, nombreEvento, seleccionColor):
                addEventWindow.destroy()
                mainWindow.destroy()
                nombreEvento = nombreEvento.replace(' ', '¶')
                # Save an event in a txt file
                fileExists = os.path.exists('EventList.txt')
                if (fileExists == True):
                    with open("EventList.txt", "a") as f:
                        f.write(str(nombreBoton) + '/' + str(currentMonth) + '/' +  str(currentYear) + ' ' + nombreEvento + '_' + seleccionHora + ':' + seleccionMinuto + ':' + seleccionAMPM + '_' + seleccionColor+ '_' +'\n')
                else:
                    with open("EventList.txt", "w") as f:
                        f.write(str(nombreBoton) + '/' + str(currentMonth) + '/' +  str(currentYear) + ' ' + nombreEvento + '_' + seleccionHora + ':' + seleccionMinuto + ':' + seleccionAMPM + '_' + seleccionColor + '_' +'\n')
                main()
            x = 0
            horas = [None] * 12
            hour = 1
            while x < 12:
                horas[x] = str(hour) 
                if(hour < 10):
                    last = str(hour) 
                    horas[x] = '0' + last
                hour += 1
                x+=1
            ampm = ['AM', 'PM']
            y = 0
            min = 0
            minutos = [None]*12
            while min < 60:
                if(min < 10):
                    last = str(min) 
                    minutos[y] = '0' + last
                else: 
                    minutos[y] = str(min) 
                min+=5
                y+=1

            addEventWindow.title('Añadir Evento')
            addEventWindow.config(width = 300, height = 200)
            seleccionHora = tk.StringVar(addEventWindow)

            tk.Label(addEventWindow, text = 'Nombre:', fg ='#000000', font = ('DS-DIGIB.TTF', 14)).place(x = 20, y = 10)
            nombreEvento = tk.Entry(addEventWindow, width=25, border = 1)

            tk.Label(addEventWindow, text = 'Hora:', fg ='#000000', font = ('DS-DIGIB.TTF', 15)).place(x = 20, y = 50)
            seleccionHora.set(horas[0])
            menuhoras = tk.OptionMenu(addEventWindow, seleccionHora, *horas)

            seleccionMinuto = tk.StringVar(addEventWindow)
            seleccionMinuto.set(minutos[0])
            menuminutos = tk.OptionMenu(addEventWindow, seleccionMinuto, *minutos)

            seleccionAMPM = tk.StringVar(addEventWindow)
            seleccionAMPM.set(ampm[0])
            menuampm = tk.OptionMenu(addEventWindow, seleccionAMPM, *ampm)

            tk.Label(addEventWindow, text = 'Color:', fg ='#000000', font = ('DS-DIGIB.TTF', 15)).place(x = 20, y = 90)
            colores = ['#EDBB99', '#AED6F1', '#ABEBC6']
            colors = 0
            positionx = 100
            
            def save_eventColor(color, botonColor, nombreDeBotonSeleccionado, seleccionDeColor):
                nombreBoton = addEventWindow.nametowidget(botonColor)
                if(nombreDeBotonSeleccionado != botonColor and nombreDeBotonSeleccionado[0] != None):
                    seleccionAnterior = addEventWindow.nametowidget(nombreDeBotonSeleccionado[0])
                    seleccionAnterior.config(width= 5, height = 2)
                nombreBoton.config(width= 2, height = 1)
                nombreDeBotonSeleccionado[0] =  botonColor
                seleccionDeColor[0] = color
                print(seleccionDeColor)

            nombreDeBotonSeleccionado = [None]*1
            seleccionDeColor = [None]*1
            while colors < 3:
                
                tk.Button(addEventWindow, border = 0, name = str(colors), bg = colores[colors], width= 5, height = 2, command = lambda color = colores[colors], nombreboton = colors: save_eventColor(color, nombreboton,nombreDeBotonSeleccionado,seleccionDeColor)).place(x = positionx, y = 90)
                colors += 1
                positionx += 50
           
            tk.Button(addEventWindow, text =' Guardar Evento', bg = '#CACFD2', border = 0, command = lambda: save_event(seleccionHora.get(), seleccionMinuto.get(), seleccionAMPM.get(), nombreEvento.get(), seleccionDeColor[0])).place(x = 110, y = 150)
            # ↓ ↑
            # menuhoras["borderwidth"] = 0
            # menuminutos["borderwidth"] = 0
            # menuampm["borderwidth"] = 0
            menuhoras.place(x = 100, y = 50)
            menuminutos.place(x = 150, y = 50)
            menuampm.place(x = 200,y = 50)
            nombreEvento.place(x = 110, y = 16)

        def show_event(diaDeEvento, evento):
            showEventWindow = Toplevel(mainWindow)
            showEventWindow.title('Evento del Dia')
            showEventWindow.config(width = 500, height = 200)
            eventDate = evento[0]
            eventName = evento[1]
            eventName = eventName.split('_')
            eventHour = eventName[1]
            eventName = eventName[0] 
            eventName = eventName.replace('¶', ' ')
            
            tk.Label(showEventWindow, text = 'Nombre del Evento: ', fg ='#000000', font = ('DS-DIGIB.TTF', 15)).place(x = 10, y = 20)
            tk.Label(showEventWindow, text = eventName, fg ='#979A9A', font = ('DS-DIGIB.TTF', 15)).place(x = 200, y =20)

            tk.Label(showEventWindow, text = 'Fecha del Evento: ', fg ='#000000', font = ('DS-DIGIB.TTF', 15)).place(x=10,y=60)
            tk.Label(showEventWindow, text = eventDate, fg ='#979A9A', font = ('DS-DIGIB.TTF', 15)).place(x = 200, y = 60)

            tk.Label(showEventWindow, text = 'Hora del Evento: ', fg ='#000000', font = ('DS-DIGIB.TTF', 15)).place(x=10,y=100)
            tk.Label(showEventWindow, text = eventHour, fg ='#979A9A', font = ('DS-DIGIB.TTF', 15)).place(x = 200, y = 100)

            #tk.Button(showEventWindow, text = 'Add an Event', command = lambda: add_event(diaDeEvento))

        numDias = 31
        if(currentMonth == 2):
            numDias = 28
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
            rfile = 'EventList.txt'
            
            while day < numDias:
                while week < 7:
                    if(day == today.day and currentMonth == today.month and currentYear == today.year):
                        tk.Button(mainWindow, text = day, name = str(day), bg = '#CACFD2', border = 0, width= 5, height = 2, command = lambda dia = day: add_event(dia)).place(x = posx + 600, y = posy)
                        if(delete != None):
                            deleteMonthDays()
                    else:
                        tk.Button(mainWindow, text = day, name = str(day), border = 0, width= 5, height = 2 , command = lambda dia = day: add_event(dia)).place(x = posx + 600, y = posy)
                        if(delete != None):
                            deleteMonthDays()
                    with open(rfile) as f:
                        lines = f.readlines()
                    i = 0
                    while i < len(lines):
                        date = lines[i].split(' ')
                        eventDayInfo = date[0]
                        eventDayInfo = eventDayInfo.split('/')
                        eventDay = eventDayInfo[0]
                        eventMont = eventDayInfo[1]
                        eventYear = eventDayInfo[2]

                        colorEvent = date[1].split('_')
                        colorEvent = colorEvent[2]
                        if(eventMont == str(currentMonth)):
                            if(eventDay == str(day)):
                                tk.Button(mainWindow, text = day, name = str(day), bg = colorEvent, border = 0, width= 5, height = 2, command = lambda dia = day, evento=date: show_event(dia, evento)).place(x = posx + 600, y = posy)
                                if(delete != None):
                                    deleteMonthDays()
                                i += 1
                        i += 1
                    if(day >= numDias):
                        break
                    week += 1
                    day +=1
                    posx += 50
                    i +=1
                week = 0
                posx = 0
                posy += 45

        configure_day(None) 
        # Detect Current Month/Year
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
        # Show Buttons:
        # -> Forward
        # -> Back
        # -> Current Month/Year
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