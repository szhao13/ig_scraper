import pyautogui
import os
os.chdir(r'/Users/shelleyzhao/interview_prep/ig_scraper')
# pyautogui.screenshot(r'/Users/shelleyzhao/interview_prep/ig_scraper')
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.moveTo(100, 150)

# time.sleep(1)
# im1 = pyautogui.screenshot(region=(0, 0, 900, 1800))
# im1.save('my_screenshot.png')
# im2 = pyautogui.screenshot('my_screenshot.png')
im3 = pyautogui.screenshot()
# time.sleep(1)
pyautogui.scroll(-100)