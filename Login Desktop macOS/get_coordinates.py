import pyautogui
import time

print("📌 Mueve el cursor sobre el botón 'Log in' y espera 5 segundos...")
time.sleep(5)
x, y = pyautogui.position()  # Captura las coordenadas del botón "Log in"
print(f"✅ Coordenadas capturadas: x={x}, y={y}")