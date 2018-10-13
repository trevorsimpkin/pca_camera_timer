from time import sleep
from datetime import datetime, timedelta
from picamera import PiCamera


class Camera:
    def __init__(self, start_time, duration_hour, duration_min):
        self.camera = PiCamera()
        self.camera.resolution = (1296, 730)
        self.start_time = start_time
        self.duration_hour = duration_hour
        self.duration_min = duration_min
        self.fileName = self.start_time.strftime("%Y-%m-%d_%H:%M.h264")
        self.duration = self.duration_hour * 3600
        self.duration += self.duration_min * 60




    def get_start_time(self):
        print(self.start_time)

    def start_timer(self):
        print(self.start_time.strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("%d" % self.duration_min)
        while self.start_time.strftime("%Y-%m-%d %H:%M:%S") != datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
            sleep(1)
        print("They are equal")


        print("%d" % self.duration)
        self.camera.start_recording(self.filename)
        self.camera.wait_recording(self.duration)
        camera.stop_recording()
        print("time has gone by")





