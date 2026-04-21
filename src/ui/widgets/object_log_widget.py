from PySide6.QtWidgets import QLabel, QListWidget, QVBoxLayout, QWidget


class ObjectLogWidget(QWidget):
    """Scrollable log of detected objects with timestamps."""

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("Detected objects")
        layout.addWidget(title)

        self.log = QListWidget()
        layout.addWidget(self.log)

    def add_entry(self, label: str, timestamp: str):
        self.log.addItem(f"[{timestamp}] {label}")
