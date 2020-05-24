from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPixmap
from datetime import datetime
from datetime import timedelta
import webbrowser
from monday import *
from tuesday import *
from wednesday import *
from thursday import *
from friday import *


app = QtWidgets.QApplication([])
dlg = uic.loadUi("Roomie.ui")
dlg.setFixedSize(dlg.size())


open_row_count = 0
next_row_count = 0

def choose_info():
    dlg.next_classes.clearContents()
    dlg.open_classes.clearContents()
    global building_choice
    day_choice = dlg.day_combo.currentText()
    building_choice = dlg.building_combo.currentText()
    print(day_choice)
    print(building_choice)
    choose_day(day_choice)

def choose_day(day):
    if day == "Monday":
        parse_options(monday)
    elif day == "Tuesday":
        parse_options(tuesday)
    elif day == "Wednesday":
        parse_options(wednesday)
    elif day == "Thursday":
        parse_options(thursday)
    elif day == "Friday":
        parse_options(friday)


def parse_options(day):
    global open_row_count, next_row_count
    open_row_count = 0
    next_row_count = 0

    for items in day:
        value = day[items]
        free_time(items, value)


def free_time(location, value):
    global open_row_count, next_row_count


    tstart = datetime.strptime('07:00', '%H:%M')
    tstop = datetime.strptime('23:59', '%H:%M')

    current = datetime.now()
    currentDT = current.strftime("%H:%M %p")
    currentDTFloat = float(current.strftime("%H.%M"))

    time_period = [(tstart , tstart)]
    free_time = []

    for t in value:
        time_period.append((t['start'], t['end']))
    time_period.append((tstop, tstop))

    for i, v in enumerate(time_period):
        if i > 0:
            if (time_period[i][0] - time_period[i-1][1]) > timedelta(seconds = 0):
                ft_start = time_period[i-1][1]
                delta = time_period[i][0] - time_period[i-1][1]
                ft_end = ft_start + delta
                free_time.append((ft_start, ft_end))

    for time_period in free_time:
        free_time_start = time_period[0].time()
        free_time_start_float = float(free_time_start.strftime("%H.%M"))
        free_time_start_formated = free_time_start.strftime("%I:%M %p")
        free_time_end = time_period[1].time()
        free_time_end_float = float(free_time_end.strftime("%H.%M"))
        free_time_end_formated = free_time_end.strftime("%I:%M %p")
        build = location[:-3]

        if free_time_end_float > currentDTFloat > free_time_start_float:
            if build == building_choice:
                print("Current open period:")
                print("{}: {} to {}".format(location,
                    free_time_start_formated, free_time_end_formated))
                dlg.open_classes.setItem(open_row_count, 0,
                    QTableWidgetItem(location))
                dlg.open_classes.setItem(open_row_count, 1,
                    QTableWidgetItem(free_time_start_formated))
                dlg.open_classes.setItem(open_row_count, 2,
                    QTableWidgetItem(free_time_end_formated))
                print(open_row_count)
                open_row_count += 1

        if free_time_start_float > currentDTFloat:
            if build == building_choice:
                print("Next open period:")
                print("{}: {} to {}".format(location,
                    free_time_start_formated, free_time_end_formated))
                dlg.next_classes.setItem(next_row_count, 0,
                    QTableWidgetItem(location))
                dlg.next_classes.setItem(next_row_count, 1,
                    QTableWidgetItem(free_time_start_formated))
                dlg.next_classes.setItem(next_row_count, 2,
                    QTableWidgetItem(free_time_end_formated))
                print(next_row_count)
                next_row_count += 1

def ig_link():
    webbrowser.open('https://www.instagram.com/roomie_application/')

def twit_link():
    webbrowser.open('https://twitter.com/RoomieApplicat1/')


dlg.building_combo.setItemData(QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)


dlg.hackathon_logo.setPixmap(QPixmap("hacktcnj.png"))
dlg.roomie_label.setPixmap(QPixmap("Roomie1.png"))
dlg.open_laptop.setPixmap(QPixmap("open_laptop.png"))
dlg.closed_laptop.setPixmap(QPixmap("closed_laptop.png"))
dlg.ig_image.setPixmap(QPixmap("ig_link.png"))
dlg.twit_image.setPixmap(QPixmap("twit_link.png"))

weekdays = ["Select Weekday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for days in weekdays:
    dlg.day_combo.addItem(days)

buildings = ["Select Building", "STEM", "Business", "Education"]
for building in buildings:
    dlg.building_combo.addItem(building)

dlg.go_button.clicked.connect(choose_info)
dlg.instagram.clicked.connect(ig_link)
dlg.twitter.clicked.connect(twit_link)

dlg.show()
app.exec()
