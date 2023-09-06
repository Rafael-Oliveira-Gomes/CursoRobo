from PIL import ImageGrab # pip install pillow
import pyautogui
import time

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://dinorunner.com/pt/ \n")

# Esperar a pagina abrir
time.sleep(5)



def isCollision(data):

    for i in range(760, 835):
        for j in range(290, 330):
            if data[i, j] < 100:
                pyautogui.keyDown("up")
                print("pulando")
                return
    return

if __name__ == "__main__":
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
