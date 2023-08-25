


import pyautogui
import time
import mouseinfo

# print(pyautogui.size())
# print(pyautogui.position())

#mouseinfo.MouseInfoWindow()

pyautogui.hotkey('win')
time.sleep(2)
pyautogui.write('vs')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(91,307)
time.sleep(2)
pyautogui.click(336,143)
time.sleep(2)
pyautogui.write('clangd')
time.sleep(2)
pyautogui.click(336,221)


#pyautogui.moveTo(73,1055,duration=0.5) #31,1034

#pyautogui.click(94,293)
