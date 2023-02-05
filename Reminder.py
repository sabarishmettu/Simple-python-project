
import time
import win10toast

# create an instance of ToastNotifier
toast = win10toast.ToastNotifier()

# set the time for the reminder
reminder_time = 10 # time in seconds

# set the reminder message
reminder_message = 'It is time for your reminder!'

# wait for that amount of time
time.sleep(reminder_time)

# show the reminder notification
toast.show_toast(reminder_message, duration=10)