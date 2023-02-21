import pyautogui
import pyperclip
import time
#uma automação so que funciona somete no meu pc

pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")
time.sleep(4)
pyperclip.copy("**")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=808, y=554)
pyperclip.copy('4861582')
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=789, y=706)
pyperclip.copy('senha')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=31, y=162)
time.sleep(5)
pyautogui.click(x=339, y=681)
time.sleep(3)
pyautogui.click(x=236, y=863)