import time
import pyautogui

# specify the path of the text file to read from
text_file_path = "C:\Users\rayud\Desktop\one for all\projects"
# read the contents of the text file into a string
with open(text_file_path, "r") as f:
    text = f.read()

# wait for a few seconds to give you time to switch to the text input field
time.sleep(5)

# type out the contents of the text file
pyautogui.write(text)
