import pyautogui

pyautogui.moveTo(x = 11, y = 757); pyautogui.click()
pyautogui.typewrite("bloco de notas")
pyautogui.moveTo(x = 217, y = 250, duration= 1); pyautogui.click()
pyautogui.moveTo(x = 481, y = 686, duration=1); pyautogui.click()
pyautogui.typewrite("Escrevendo no bloco de notas!")
pyautogui.press("enter")
pyautogui.typewrite("Hello Word!")