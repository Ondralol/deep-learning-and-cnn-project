from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QSizePolicy

STYLE_SHEET_RECORD_BUTTON_NOT_RECORDING = """
    QPushButton {
        background-color: #2ecc71;
        color: white;
        font-size: 15px;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #27ae60;
    }

    QPushButton:pressed {
        background-color: #1e8449;
    }
"""


STYLE_SHEET_RECORD_BUTTON_RECORDING = """
    QPushButton {
        background-color: #E53935;
        color: white;
        font-size: 15px;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #D32F2F;
    }

    QPushButton:pressed {
        background-color: #B71C1C;
    }
"""


BUTTON_WIDTH = 200
BUTTON_HEIGHT = 25


class RecordButton(QPushButton):
    """Starts/Stops drone video recording"""
    def __init__(self, parent, startRecordingCallback=None, stopRecordingCallback=None):
        super().__init__(parent)
        self.isRecording = False
        self.startRecordingCallback = startRecordingCallback
        self.stopRecordingCallback = stopRecordingCallback

        self.setText("Start Recording")
        self.setMinimumHeight(25)
        self.setFont(QFont("Arial", 12, QFont.Bold))

        # Disable ability to use keyboard to accidentally trigger buttons
        self.setFocusPolicy(Qt.NoFocus)

        # Sizing policy
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.clicked.connect(self.toggleRecording)
        self.setStyleSheet(STYLE_SHEET_RECORD_BUTTON_NOT_RECORDING)

        # UX timer
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.updateStyle)

    def toggleRecording(self):
        """Toggle between start and stop recording"""
        # Reset timer
        self.timer.stop()

        if not self.isRecording:
            self.setText("Starting the recording")
            self.setStyleSheet(STYLE_SHEET_RECORD_BUTTON_RECORDING)
            if self.startRecordingCallback:
                self.startRecordingCallback()
        else:
            self.setText("Saving the recording")
            self.setStyleSheet(STYLE_SHEET_RECORD_BUTTON_NOT_RECORDING)
            if self.stopRecordingCallback:
                self.stopRecordingCallback()

        # Change state
        self.isRecording = not self.isRecording
        self.timer.start(1500)  # 1.5 seconds to update the style

    def updateStyle(self):
        """Update button appearance based on recording state"""
        if self.isRecording:
            self.setText("Stop Recording")
        else:
            self.setText("Start Recording")

    # Default size
    def sizeHint(self) -> QSize:
        return QSize(BUTTON_WIDTH, BUTTON_HEIGHT)