from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget

class ActivityIndicatorWidget(QWidget):
    def __init__(self, parent, milliseconds: int):
        """Activity indicator dot.

        Is green when connected to the drone and red when disconnected form the drone. Activity
        from drone needs to be registered every x milliseconds in order to keep indicator active."""


        super().__init__(parent)
        self.timeout = milliseconds
        self.setStatus(False)

        # For inactivity (Needs to check every x milliseconds)
        self.inactivityTimer = QTimer()
        self.inactivityTimer.setSingleShot(True)
        self.inactivityTimer.setTimerType(Qt.PreciseTimer)
        self.inactivityTimer.timeout.connect(lambda: self.inactivityTriggered())
        self.inactivityTimer.start(self.timeout)

    def inactivityTriggered(self):
        """Triggered when the inactivity timer times out, sets the status to inactive"""
        self.setStatus(False)
        self.inactivityTimer.start(self.timeout)
        self.update()

    def activityDetected(self):
        """Called when activity is detected, resets the inactivity timer and sets the status to active"""
        self.inactivityTimer.stop()
        self.setStatus(True)
        self.inactivityTimer.start(self.timeout)
        self.update()

    def setStatus(self, status: bool):
        if status is True:
            self.color = QColor("green")
        elif status is False:
            self.color = QColor("red")
        self.update()

    def sizeHint(self) -> QSize:
        return QSize(13, 13)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.NoPen)
        radius = min(self.width(), self.height()) // 2
        painter.drawEllipse(
            (self.width() - radius * 2) // 2,
            (self.height() - radius * 2) // 2,
            radius * 2,
            radius * 2,
        )
        painter.end()