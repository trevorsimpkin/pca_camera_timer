from datetime import datetime
from camera import Camera
import sys
# Will need to do switch case on month to determin how many days of each month when entered.
#  Maybe don't show day until month chosen if possible


def schedule_camera(start_time_init, duration_hour_init, duration_min_init):
    pi_camera = Camera(start_time=start_time_init, duration_hour=duration_hour_init, duration_min=duration_min_init)
    pi_camera.start_timer()


start_time = datetime(year=int(sys.argv[1]), month=int(sys.argv[2]),
                      day=int(sys.argv[3]), hour=int(sys.argv[4]),
                      minute=int(sys.argv[5]), second=0)
duration_hour = int(sys.argv[6])
duration_min = int(sys.argv[7])
schedule_camera(start_time, duration_hour, duration_min)


