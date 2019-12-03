from PySide2 import QtCore, QtGui, QtWidgets
from Event import Event
import ProjectUI
import GoogleCalendar
import EventManager
import ProjectUI2

class MyQtAPP(ProjectUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtAPP, self).__init__()
        self.setupUi(self)
        self.ui = ProjectUI2.Ui_EventWindow()
        self.window = QtWidgets.QMainWindow()

        #self.AddEventsCalndar.clicked.connect(self.GoogleAddEvent)
        self.PrintEventsCalendar.clicked.connect(self.GooglePrintEvent)

        self.labelList = []
        self.FavoritesLabelList = []
        self.FavoritesEventThere = []
        EventManager.FindEvents()
        self.EventPage()
        for i in range(len(self.labelList)):
            self.labelList[i].mousePressEvent = lambda event, x=i: self.oneEventInfo(x)

        self.googleClanderpermission = False
        self.DarkModeButton.toggled.connect(self.DarkMode)


    def EventPage(self):
        for e in EventManager.FullEventList:
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setMinimumSize(QtCore.QSize(0, 40))
            label.setCursor(QtCore.Qt.PointingHandCursor)
            label.setStyleSheet("background-color: rgb(255, 255, 255);")
            label.setMargin(6)
            label.setWordWrap(True)
            label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
            label.setObjectName("label")
            label.setText(e.name + "\n    " + e.date)
            self.verticalLayout_2.addWidget(label)
            self.labelList.append(label)

    def oneEventInfo(self, i):
        self.ui.setupUi(self.window)
        EventManager.EventInfoDisplay(EventManager.FullEventList[i], self.ui.textBrowser,EventManager.FullEventList,i)
        self.window.show()
        self.ui.AddToFavoritesButton.clicked.connect(lambda: self.AddToFavorites(i))
        self.ui.AddToCalendarButton.clicked.connect(lambda: self.GoogleAddEvent(i))

    def AddToFavorites(self, i):
        for x in self.FavoritesEventThere:
            if x == i:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("This Event Is Already in Favorites")
                msg.setWindowTitle("Favorite Events")
                msg.exec_()
                return

        label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        label.setMinimumSize(QtCore.QSize(0, 40))
        label.setCursor(QtCore.Qt.PointingHandCursor)
        label.setStyleSheet("background-color: rgb(255, 255, 255);")
        label.setMargin(6)
        label.setWordWrap(True)
        label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        label.setObjectName("label")
        label.setText(EventManager.FullEventList[i].name + "\n    " + EventManager.FullEventList[i].date)
        self.verticalLayout.addWidget(label)
        self.FavoritesLabelList.append(label)
        self.FavoritesEventThere.append(i)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("The Event Was Added to Favorites")
        msg.setWindowTitle("Favorite Events")
        msg.exec_()

        for i in range(len(self.FavoritesEventThere)):
            self.FavoritesLabelList[i].mousePressEvent = lambda event, y=i, z=self.FavoritesEventThere[i]: self.RemoveFromFavorites(event, y, z)

        self.DarkMode()

    def RemoveFromFavorites(self,event, y, z):
        if event.button() == QtCore.Qt.RightButton:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setText("Do You Want To Remove This Event?")
            msg.setWindowTitle("Favorite Events")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            reply = msg.exec_()
            if reply == QtWidgets.QMessageBox.Yes:
                self.FavoritesLabelList[y].hide()
                self.FavoritesLabelList.pop(y)
                self.FavoritesEventThere.pop(y)
            else:
                return
        elif event.button() == QtCore.Qt.LeftButton:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setText("Do You Need More Info about This Event?")
            msg.setWindowTitle("Favorite Events")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            reply = msg.exec_()
            if reply == QtWidgets.QMessageBox.Yes:
                self.oneEventInfo(z)
            else:
                return

    def GoogleAddEvent(self, i):
        if self.googleClanderpermission == False:
            self.service = GoogleCalendar.getAPI()
            self.googleClanderpermission = True
        findDateandTime = self.ui.dateTimeEdit.dateTime()
        StringDateTime = str(findDateandTime.toString("yyyy-MM-ddThh:mm:ss"))
        GoogleCalendar.AddEvent(self.service, self.textBrowser_2, EventManager.FullEventList[i], StringDateTime)

    def GooglePrintEvent(self):
        if self.googleClanderpermission == False:
            self.service = GoogleCalendar.getAPI()
            self.googleClanderpermission = True
        GoogleCalendar.printEvents(self.service, 25, self.textBrowser_2)





    def DarkMode(self):
        if self.DarkModeButton.isChecked() == True:
            self.centralwidget.setStyleSheet("background-color: rgb(51, 51, 51);")
            self.frame.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                     "border-color: rgb(204, 204, 204);\n"
                                     "")
            self.SearchButton.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.searchBar.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                         "color: rgb(230, 230, 230);\n"
                                         "selection-background-color: rgba(102, 204, 255, 243);")
            self.DarkModeButton.setStyleSheet("color: rgb(230, 230, 230);\n"
                                           "")
            self.toolButton.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.HomeWidget.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.AllEventsTab.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollArea.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollArea_2.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(76, 76, 76);")
            self.textBrowser_2.setStyleSheet("background-color: rgb(128, 128, 128);\n"
                                             "color: rgb(255, 255, 255);")
            #self.AddEventsCalndar.setStyleSheet("background-color: rgb(128, 0, 64);\n"
            #                                    "color: rgb(255, 255, 255);")
            self.PrintEventsCalendar.setStyleSheet("background-color: rgb(128, 0, 64);\n"
                                                   "color: rgb(255, 255, 255);")
            self.frame_2.setStyleSheet("background-color: rgb(25, 25, 25);")
            for i in self.labelList:
                i.setStyleSheet("background-color: rgb(128, 128, 128);\n"
                                           "color: rgb(255, 255, 255);")
            for i in self.FavoritesLabelList:
                i.setStyleSheet("background-color: rgb(128, 128, 128);\n"
                                           "color: rgb(255, 255, 255);")

        else:
            self.centralwidget.setStyleSheet("default")
            self.frame.setStyleSheet("default")
            self.SearchButton.setStyleSheet("default")
            self.searchBar.setStyleSheet("default")
            self.DarkModeButton.setStyleSheet("default")
            self.toolButton.setStyleSheet("default")
            self.HomeWidget.setStyleSheet("default")
            self.EventsWidget.setStyleSheet("default")
            self.FavoritesEventsTab.setStyleSheet("default")
            self.EventTab.setStyleSheet("default")
            self.AllEventsTab.setStyleSheet("default")
            self.CalendarTab.setStyleSheet("default")
            self.textBrowser_2.setStyleSheet("default")
            #self.AddEventsCalndar.setStyleSheet("default")
            self.PrintEventsCalendar.setStyleSheet("default")
            self.frame_2.setStyleSheet("background-color: rgb(7, 64, 128);")
            self.scrollArea.setStyleSheet("default")
            self.scrollAreaWidgetContents.setStyleSheet("default")
            self.scrollArea_2.setStyleSheet("default")
            self.scrollAreaWidgetContents_2.setStyleSheet("default")
            for i in self.labelList:
                i.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
            for i in self.FavoritesLabelList:
                i.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtAPP()
    qt_app.show()
    app.exec_()

