from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget


class LiveFeedWidget(QWidget):
    """Live video feed with object detection overlay."""

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("Live video feed with object detection")
        layout.addWidget(title)

        self.feed_label = QLabel("No feed")
        self.feed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.feed_label.setMinimumSize(960, 720)
        self.feed_label.setStyleSheet("background: black; color: white;")
        self.feed_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.feed_label)
