import pyautogui
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
# os.chdir(r'/Users/shelleyzhao/interview_prep/ig_scraper')
# pyautogui.screenshot(r'/Users/shelleyzhao/interview_prep/ig_scraper')
import time
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))

username = input()
print(username)
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.moveTo(100, 150)
# time.sleep(1)
im1 = pyautogui.screenshot(region=(0, 0, 900, 1800))
im1.save('my_screenshot.png')
# im2 = pyautogui.screenshot('my_screenshot.png')
# im2_crop = Image.open("my_screenshot.png")
# cropped = im2_crop.crop((0, 0, 800, 12000))
# cropped.show()
text = pytesseract.image_to_string(Image.open('my_screenshot.png'))
print(text)
if username in text:
	print("user found!")
else:
	print("user not found :(")
# print(pytesseract.image_to_string(Image.open('man_crop.png')))

#im3 = pyautogui.screenshot()
# time.sleep(1)
pyautogui.scroll(-5000)