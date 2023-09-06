import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")

# Esperar a pagina abrir
time.sleep(5)

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

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\nome.png"), duration=1)
        pyautogui.typewrite(name, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\email.png"), duration=1)
        pyautogui.typewrite(email, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\telefone.png"), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\sexo.png"), duration=1)
        
        if sex=="Masculino":
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\masculino.png"), duration=1)
        else:
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\feminino.png"), duration=1)
        
        pyautogui.screenshot(f"cadastro_{name}.png")
        
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\botao_enviar.png"), duration=1)

        time.sleep(3)

pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")

