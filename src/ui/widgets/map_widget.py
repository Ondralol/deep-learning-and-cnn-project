from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget


class MapWidget(QWidget):
    """Map showing detected objects and their positions (using heatmap)."""

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("Map showing the detected objects")
        layout.addWidget(title)

        self.map_label = QLabel("No map data")
        self.map_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.map_label.setMinimumSize(480, 360)
        self.map_label.setStyleSheet("background: #1a1a2e; color: white;")
        self.map_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.map_label)
