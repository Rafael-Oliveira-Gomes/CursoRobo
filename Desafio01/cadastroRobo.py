import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")

# Esperar a pagina abrir
time.sleep(0.5)

with open("membros.csv") as f:
    next(f)
    
    for line in f:
        line = line.strip()
        
        # Verifique se a linha não está em branco antes de processá-la
        if line:
            line = line.split(";")
            print("Dados: ", line)

            name = line[0]
            sex = line[1]
            email = line[2]
            phone = line[3]

            # Resto do seu código continua aqui...






        pyautogui.moveTo(x = 590, y = 262); pyautogui.click(pyautogui.locateCenterOnScreen("img\\nome.png"), duration=0.5)
        pyautogui.typewrite(name, interval=0.25)
        
        pyautogui.moveTo(x = 719, y = 323); pyautogui.click(pyautogui.locateCenterOnScreen("img\\email.png"), duration=0.5)
        pyautogui.typewrite(email, interval=0.25)

        pyautogui.moveTo(x = 713, y = 369); pyautogui.click(pyautogui.locateCenterOnScreen("img\\telefone.png"), duration=0.5)
        pyautogui.typewrite(phone, interval=0.25)

        pyautogui.moveTo(x = 603, y = 427); pyautogui.click(pyautogui.locateCenterOnScreen("img\\sexo.png"), duration=0.5)
        
        if sex=="Masculino":
            pyautogui.moveTo(x = 462, y = 460); pyautogui.click()
            
        else:
           pyautogui.moveTo(x = 461, y = 482); pyautogui.click()
        
        pyautogui.screenshot(f"cadastro_{name}.png")
        
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\botao_enviar.png"), duration=0.5)

        time.sleep(1)

pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")