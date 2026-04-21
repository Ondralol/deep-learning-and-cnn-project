
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget

from ui.elements.generic_button import GenericButton
from ui.elements.record_button import RecordButton
from ui.widgets.activity_indicator_widget import ActivityIndicatorWidget
from ui.widgets.battery_widget import BatteryWidget
from ui.windows.popup_window_drone_controls import PopupWindowDroneControls


MAIN_STATUS_BAR_WIDGET_WIDTH = 1920
MAIN_STATUS_BAR_WIDGET_HEIGHT = 50

class StatusBarWidget(QFrame):
    """Status bar widget for the main window.
    
    Contains the connect button, drone connectivity indicator, battery status, wifi status
    and buttons to open popup windows for debug and controls."""

    def __init__(self, parent):
        super().__init__(parent)

        # Create horizontal layout and set spacing/margins
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setContentsMargins(10, 10, 10, 10)
        horizontalLayout.setSpacing(10)

        # Add connect to drone button
        self.buttonDroneConnect = GenericButton(self, "Connect to the Drone")
        self.buttonDroneConnect.clicked.connect(self.DroneConnectButtonClicked)
        horizontalLayout.addWidget(self.buttonDroneConnect)

        # Add activity dot
        horizontalLayout.addWidget(ActivityIndicatorWidget(self, 500))

        # Extra controls button to open popup window - to control drone
        self.buttonDroneControls = GenericButton(self, "Drone Controls")
        self.buttonDroneControls.clicked.connect(self.droneControlsButtonClicked)
        horizontalLayout.addWidget(self.buttonDroneControls)

        self.droneControlsPopup = PopupWindowDroneControls(self)

        # Add record button
        horizontalLayout.addWidget(RecordButton(self))

        # Add battery indicator
        self.battery = BatteryWidget(self)
        horizontalLayout.addWidget(self.battery)

        self.setLayout(horizontalLayout)
        
        self.setMaximumHeight(MAIN_STATUS_BAR_WIDGET_HEIGHT)

    # Default size
    def sizeHint(self) -> QSize:
        return QSize(MAIN_STATUS_BAR_WIDGET_WIDTH, MAIN_STATUS_BAR_WIDGET_HEIGHT)

    def droneControlsButtonClicked(self):
        self.droneControlsPopup.show()

    def DroneConnectButtonClicked(self):
        # TODO
        print("Connecting to the drone")
