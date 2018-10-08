from datetime import datetime
from camera import Camera
from guizero import App, Text, Picture, Box, TextBox, Combo, PushButton
# Will need to do switch case on month to determin how many days of each month when entered.
#  Maybe don't show day until month chosen if possible


def schedule_camera():
    start_time_input = datetime(year=int(schedule_start_time_year.get()), month=int(schedule_start_time_month.get()),
                          day=int(schedule_start_time_day.get()), hour=int(schedule_start_time_hour.get()),
                          minute=int(schedule_start_time_minute.get()), second=0)
    duration_hour_input = int(duration_hours.get())
    duration_min_input = int(duration_minutes.get())
    pi_camera = Camera(start_time=start_time_input, duration_hour=duration_hour_input, duration_min=duration_min_input)
    pi_camera.get_start_time()
    pi_camera.start_timer()


app = App(title="PCA Traffic Counting Camera")
logo = Picture(app, image="pca.png")
schedule_camera_text = Text(app, text="Schedule Camera", font="Helvetica", size=20)
container = Box(app, layout="grid")
start_time_text = Text(container, text="Enter Start Date: ", font="Helvetica", size=20, grid=[0, 0])
start_time_text_month = Text(container, text="Month: ", font="Helvetica", size=20, grid=[1, 0])
schedule_start_time_month = Combo(container, options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], grid=[2, 0])
start_time_text_day = Text(container, text=" Day: ", font="Helvetica", size=20, grid=[3, 0])
schedule_start_time_day = Combo(container, options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], grid=[4, 0])
start_time_text_year = Text(container, text="Year: ", font="Helvetica", size=20, grid=[5, 0])
schedule_start_time_year = Combo(container, options=[2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025], grid=[6, 0])
start_time_text_hour = Text(container, text=" Hour: ", font="Helvetica", size=20, grid=[7, 0])
schedule_start_time_hour = Combo(container, options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                                                     19, 20, 21, 22, 23], grid=[8, 0])
schedule_start_time_minute = TextBox(container, grid=[9, 0])
duration_text = Text(container, text="Enter Duration Hours: ", font="Helvetica", size=20, grid=[0, 1])
duration_hours = Combo(container, options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], grid=[1, 1])
duration_minutes = Combo(container, options=[0, 15, 30, 45], grid=[1, 2])
# app.tk.attributes("-fullscreen", True)
button = PushButton(app, command=schedule_camera)

app.display()


