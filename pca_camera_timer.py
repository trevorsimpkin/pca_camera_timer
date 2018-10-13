from datetime import datetime
from camera import Camera
import sys
# Will need to do switch case on month to determin how many days of each month when entered.
#  Maybe don't show day until month chosen if possible


def schedule_camera(start_time_init, duration_hour_init, duration_min_init):
    pi_camera = Camera(start_time=start_time_init, duration_hour=duration_hour_init, duration_min=duration_min_init)
    pi_camera.start_timer()

file = open("schedule.pca","r")
file_lines = file.readlines()
schedule_arr = []
innerarr = []
for x in file_lines:
    components = x.split()
    innerarr.append(datetime(year=int(components[0]), month=int(components[1]),
                          day=int(components[2]), hour=int(components[3]),
                          minute=int(components[4]), second=0))
    innerarr.append(int(components[5]))
    innerarr.append(int(components[6]))
    schedule_arr.append(innerarr)
    innerarr = []

for schedule in schedule_arr:
    schedule_camera(schedule[0], schedule[1], schedule[2])
