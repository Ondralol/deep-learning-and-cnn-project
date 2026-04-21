from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

STYLE_SHEET_LABEL = """
    QLabel {
        color: white;      
        font-size: 15.75px;
        font-weight: bold;
        padding: 8px;
        border-radius: 5px;
        outline: none;
        border: none;
    }
"""

LABEL_WIDTH = 90
LABEL_HEIGHT = 30


class GenericLabel(QLabel):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
        self.setText(text)
        self.setStyleSheet(STYLE_SHEET_LABEL)
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(False)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Set minimal size
        self.setMinimumSize(LABEL_WIDTH, LABEL_HEIGHT)

    # Default size
    def sizeHint(self) -> QSize:
        return QSize(LABEL_WIDTH, LABEL_HEIGHT)