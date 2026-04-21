import cv2
from djitellopy import tello




class Drone:
    def __init__(self):
        self.drone = tello.Tello()
        self.drone.connect()
        self.drone.streamon()

    def _process_video(self):
        while True:
            frame = self.drone.get_frame_read().frame
            
