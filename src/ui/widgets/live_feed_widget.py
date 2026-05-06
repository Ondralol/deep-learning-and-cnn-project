import os
import time

import cv2
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap

import numpy as np

from ui.elements.title import Title

class LiveFeedWidget(QWidget):
    """Live video feed with object detection overlay."""

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = Title(self, "Live video feed with object detection")
        layout.addWidget(title, alignment=Qt.AlignCenter)

        self.feed_label = QLabel("No feed")
        self.feed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.feed_label.setMinimumSize(960, 720)
        self.feed_label.setStyleSheet("background: black; color: white;")
        self.feed_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.feed_label)

        self.recording = False
        self.record_file_path = None
        self.video_writer = None
    
    def startRecording(self, output_dir: str = "recordings"):
        if self.recording:
            return self.record_file_path

        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.record_file_path = os.path.join(output_dir, f"drone_recording_{timestamp}.mp4")
        self.recording = True
        self.video_writer = None
        return self.record_file_path

    def stopRecording(self):
        if not self.recording:
            return None

        self.recording = False
        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None

        return self.record_file_path

    def _save_frame(self, frame: np.ndarray):
        if not self.recording:
            return

        if self.video_writer is None:
            height, width = frame.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            self.video_writer = cv2.VideoWriter(self.record_file_path, fourcc, 20.0, (width, height))
            if not self.video_writer.isOpened():
                print(f"Unable to open recording file: {self.record_file_path}")
                self.recording = False
                self.record_file_path = None
                self.video_writer = None
                return

        self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def updateFrame(self, frame: np.ndarray):
        h, w, ch = frame.shape
        img = QImage(frame.data, w, h, ch * w, QImage.Format.Format_RGB888)
        self.feed_label.setPixmap(
            QPixmap.fromImage(img).scaled(
                self.feed_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        if self.recording:
            self._save_frame(frame)
