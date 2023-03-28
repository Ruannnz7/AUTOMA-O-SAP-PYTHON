import pyautogui 
import time
#Entrar na transação
pyautogui.moveTo(74,48,duration=1)
pyautogui.click(74,48)
pyautogui.typewrite('/nZFIMXM10140\n', interval=0)
pyautogui.press('enter')
time.sleep(1)
#Seleção de transação (Contar a pagar)
pyautogui.moveTo(40,395,duration=2)
pyautogui.click(40,395)
time.sleep(1)
pyautogui.press('F8')
time.sleep(1)
#colocar data do documento
pyautogui.moveTo(199,145)
pyautogui.click(199, 145)
pyautogui.typewrite('10.03.2023\n', interval=0)
time.sleep(0.5)
#colocar data calendario
pyautogui.moveTo(263,340)
time.sleep(0.5)
pyautogui.moveTo(148,224)
time.sleep(0.5)
pyautogui.click(148,224)
pyautogui.typewrite('0022224446\n', interval=0)
