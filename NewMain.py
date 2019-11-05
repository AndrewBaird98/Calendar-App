import self as self
from PySide2 import QtCore, QtGui, QtWidgets
from Event import Event
import ProjectUI
import WebScraperTest
import GoogleCalendar


class MyQtAPP(ProjectUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtAPP, self).__init__()
        self.setupUi(self)
        self.EventPage()
        self.GoogleCalendarPage()


    def EventPage(self):
        self.FindEvents.clicked.connect(WebScraperTest.FindEvents(self.textBrowser))


    def GoogleCalendarPage(self):
        service = GoogleCalendar.getAPI()
        attendees = ['baird013@cougars.csusm.edu']
        currentEvent = Event("Taco Tuesday", "2019-11-28", "09:00:00-07:00", "17:00:00-07:00", "San Marcos", "CA", "$6", "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21", 'RRULE:FREQ=DAILY;COUNT=2;', attendees)

        self.AddEventsCalndar.clicked.connect(GoogleCalendar.AddEvent(service, self.textBrowser_2, currentEvent))
        self.PrintEventsCalendar.clicked.connect(GoogleCalendar.printEvents(service, 10, self.textBrowser_2))








if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtAPP()
    qt_app.show()
    app.exec_()

