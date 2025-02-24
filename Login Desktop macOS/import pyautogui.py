import pyautogui
import time
import subprocess

# Abre la aplicación Internxt
subprocess.run(["open", "-a", "Internxt"])
time.sleep(5)  # Espera a que la app cargue

# Simula un clic en el botón "Inicia sesión con el navegador" (ajusta las coordenadas)
pyautogui.click(1110, 935)  # Cambia las coordenadas según la ubicación del botón

# Esperar a que el navegador se abra (si redirige al navegador)
time.sleep(5)

# Simula escribir el correo y la contraseña
pyautogui.write("fatima@internxt.com")  # Reemplaza con tu correo
pyautogui.press("tab")  # Salta al campo de contraseña
pyautogui.write("Morgana.79")  # Reemplaza con tu contraseña
pyautogui.press("enter")  # Presiona Enter para iniciar sesión
