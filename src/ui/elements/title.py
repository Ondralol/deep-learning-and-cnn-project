from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

STYLE_SHEET_TITLE_TEMPLATE = """
    QLabel {{
        color: white;
        font-size: {}px;
        font-weight: bold;
        padding: 10px;
        border: none;
        outline: none;
    }}
"""


TITLE_WIDTH = 200
TITLE_HEIGHT = 35


class Title(QLabel):
    def __init__(self, parent, text, fontSize=17) -> None:
        super().__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(STYLE_SHEET_TITLE_TEMPLATE.format(fontSize))

        # Set size
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(TITLE_WIDTH, TITLE_HEIGHT)
        self.setMaximumSize(2000, 70)

    # Default size
    def sizeHint(self) -> QSize:
        return QSize(TITLE_WIDTH, TITLE_HEIGHT)