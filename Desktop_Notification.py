import time
from plyer import notification

while True:
    notification.notify(
        title="Take a break",
        message="It's been an hour. Time to take a break!",
        timeout=10
    )
    time.sleep(3600) # sleep for an hour
