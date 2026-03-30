# Author      : Lakshya Pachkhede
# Date        : 30/3/2026
# Description : Basic calendar program using Tkinter and Python's calendar module


import tkinter as tk
import calendar
from datetime import datetime


root = tk.Tk()
root.title("")



month = datetime.now().month
year = datetime.now().year


calendar_widgets = []

def draw_calender(year, month):
    global calendar_widgets

    for widget in calendar_widgets:
        widget.destroy()
    calendar_widgets = []


    month_name = calendar.month_name[month]
    title = f"{month_name} {year}"

    root.title(title + " - Lakshya Pachkhede")

    days_name = list(calendar.day_name)

    weeks = calendar.monthcalendar(year, month)

    today = datetime.now()

    title = tk.Label(root, font=("Arial", 16, "bold"), text=title)
    title.grid(row=0, column=0, columnspan=7, sticky="w")
    calendar_widgets.append(title)

    button_prev = tk.Button(root,
                   text="<",
                   bg="purple3",   
                   fg="white", 
                   command=prev    
                   )
    button_next = tk.Button(root,
                   text=">",
                   bg="purple3",
                   fg="white",  
                   command=next 
                   )


    button_prev.grid(row=0, column=5, columnspan=1,sticky="nsew", padx=2, pady=2) 
    button_next.grid(row=0, column=6, columnspan=1,sticky="nsew", padx=2, pady=2) 
    calendar_widgets.extend([button_prev, button_next])

    for c, day in enumerate(days_name):
        bg_color = "orange red" if c == 6 else "lightgray"
        cell = tk.Label(root, text=day, borderwidth=1, relief="solid", width=10, height=3, bg=bg_color)
        cell.grid(row=1, column=c, padx=2, pady=2,sticky="nsew")
        calendar_widgets.append(cell)

    for r, week in enumerate(weeks):
        for c, day in enumerate(week):
            bg_color = "orange red" if c == 6 else "white"

            if (day == today.day and
                month == today.month and
                year == today.year):
                bg_color = "#90ee90"

            cell = tk.Label(root, text=day if day != 0 else "", borderwidth=1, relief="solid", width=10, height=3, bg=bg_color)
            cell.grid(row=r+2, column=c, padx=2, pady=2,sticky="nsew")
            calendar_widgets.append(cell)



    for r in range(len(weeks) + 2):
        root.grid_rowconfigure(r, weight=1)
    for c in range(7):
        root.grid_columnconfigure(c, weight=1)


def next():
    global month, year
    month +=1 
    if (month > 12):
        month = 1
        year += 1
    draw_calender(year, month)

    

def prev():
    global month, year
    month -=1 
    if (month < 1):
        month = 12
        year -= 1
    draw_calender(year, month)



draw_calender(year, month)

root.mainloop()
